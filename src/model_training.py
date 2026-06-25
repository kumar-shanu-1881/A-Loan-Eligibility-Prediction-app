# modules imports 
import pandas as pd 
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from imblearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE
from data_preprocessing import preprocessing
from feature_Engineering import featureEng
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score,accuracy_score


# load the cleaned data 
df=pd.read_csv(r'C:\Users\bnsah\OneDrive\文档\PROJECTS(FINAL)\PROJECTS\Loan Eligibility Prediction\data\cleaned_data.csv')

# Adding features in data frame using feature engineering 
df=featureEng(df)

# seaprating the data from df 
X=df.drop(columns=["Default"])
y=df['Default']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y   # IMPORTANT for imbalance
)


# send data for preprocess
preprocessor=preprocessing(X_train)

X_train_processed = preprocessor.fit_transform(X_train)

X_test_processed = preprocessor.transform(X_test)

# Apply SMOTE only to the already-processed training data
smote = SMOTE(random_state=32)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train_processed, y_train)

print(f"Checking the class distribution for the data : {y_train_resampled.value_counts()}\n")

neg=(y_train==0).sum()
pos=(y_train==1).sum()
# Defining the models in the 
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),  # base line model for classification algorithm
    "Random Forest": RandomForestClassifier(
        class_weight='balanced',
        random_state=42),  #Random forest learn complex patterns easily  
    "XGBoost": XGBClassifier(      #XGBClassifier learns from complex patterns and build trees sequentially 
        eval_metric="logloss", 
        random_state=42, 
        # device="cuda" # Keeping this to gpu
        scale_pos_weight=neg/pos, # Forces XGBoost to treat 1 default as important as 10 safe loans
        max_depth=4
    )
}

# Evaluate loop
for name, model in models.items():
    model.fit(X_train_resampled, y_train_resampled)
    preds = model.predict(X_test_processed)
    probs = model.predict_proba(X_test_processed)[:, 1]

    print(f"\n----------------- {name} -----------------")
    print(f"ROC-AUC Score: {roc_auc_score(y_test, probs):.4f}")
    print(f"Accuracy Score:- {accuracy_score(y_test,preds)*100:.2f}%")
    print(classification_report(y_test, preds))

