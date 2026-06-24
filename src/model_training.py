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
X=df.drop(columns=["default"])
y=df['default']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y   # IMPORTANT for imbalance
)


# send data for preprocess
preprocessor=preprocessing(X)


# data resampling to balance the classes
smote=SMOTE(random_state=32)
x_re,y_re=smote.fit_resample(X_train,y_train)
print(y_re.value_counts())


# Defining the models in the pipeline
pipelines = {
    "Logistic Regression": Pipeline([
        ('preprocessor', preprocessor),
        ('smote', SMOTE(random_state=32)),
        ('model', LogisticRegression(max_iter=1000))
    ]),
    "Random Forest": Pipeline([
        ('preprocessor', preprocessor),
        ('smote', SMOTE(random_state=32)),
        ('model', RandomForestClassifier(random_state=42))
    ]),
    "XGBoost": Pipeline([
        ('preprocessor', preprocessor),
        ('smote', SMOTE(random_state=32)),
        ('model', XGBClassifier(eval_metric="logloss", random_state=42))
    ])
}

# Evaluate loop
for name, model in pipelines.items():
    model.fit(x_re, y_re)
    preds = model.predict(X_test)
    probs = model.predict_proba(X_test)[:, 1]

    print(f"\n----------------- {name} -----------------")
    print(f"ROC-AUC Score: {roc_auc_score(y_test, probs):.4f}")
    print(f"Accuracy Score:- {accuracy_score(y_test,preds)*100:.2f}%")
    print(classification_report(y_test, preds))