import os
import joblib
import pandas as pd
import scipy.stats as stats
from sklearn.linear_model import LogisticRegression
from imblearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE
from feature_Engineering import featureEng
from data_preprocessing import preprocessing
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.metrics import classification_report, roc_auc_score, accuracy_score


print("Loading clean CSV file ")
url=r"C:\Users\bnsah\OneDrive\文档\PROJECTS(FINAL)\PROJECTS\Loan Eligibility Prediction\data\cleaned_data.csv"

# read the csv file 
df=pd.read_csv(url)

# doing the feature engineering 
df=featureEng(df)

# Seaprating the target and the features 
x=df.drop(columns=["Default"])
y=df['Default']

# splitting the data into training and testing set 
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42,stratify=y)

# applying the data precessing to the training data 
preprocessor=preprocessing(x_train)


# building model pipeline 
tuning_pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('smote', SMOTE(random_state=42)),
    ('model', LogisticRegression(
        random_state=42,
    ))
])


# configuring the hyper parameter tuning grid
param_distributions = {
    "model__C": stats.loguniform(1e-3, 1e2),
    "model__penalty": ["l1", "l2"],
    "model__max_iter":[1000,2000],
    "model__solver": ["saga","liblinear"]
}


# using hyper parameter tuning using RandomizedSearchCV (3-fold cross validation)
random_search=RandomizedSearchCV(
    estimator=tuning_pipeline,
    param_distributions=param_distributions,
    n_iter=50,  #runs till 10 iteration
    scoring='roc_auc',
    cv=3,
    random_state=42,
    n_jobs=-1,
    verbose=1
)


# Run the search on raw training data
random_search.fit(x_train, y_train)

print(f"Best Mathematical ROC-AUC Score: {random_search.best_score_:.4f}")
print(f"Optimized Parameters Found: {random_search.best_params_}")

# Extract the winning model configuration
best_pipeline = random_search.best_estimator_

print("\nEvaluating final optimized pipeline on unseen Test Data...")
preds = best_pipeline.predict(x_test)
probs = best_pipeline.predict_proba(x_test)[:, 1]

print("\n------------------- Final Tuned Logistic Regression Results -------------------")
print(f"ROC-AUC Score: {roc_auc_score(y_test, probs):.4f}")
print(f"Overall Accuracy Score: {accuracy_score(y_test, preds)*100:.2f}%")
print(classification_report(y_test, preds))

# Ensure the src directory exists 
os.makedirs("src", exist_ok=True)

# Save the absolute winner
print("\nExporting binary artifacts for web deployment...")
joblib.dump(
    best_pipeline,
    "PROJECTS/Loan Eligibility Prediction/src/loan_production_pipeline.pkl"
)
print("Success! Master pipeline saved to: PROJECTS\Loan Eligibility Prediction\src/loan_production_pipeline.pkl")