import pandas as pd 
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load the raw data
url=r"C:\Users\bnsah\OneDrive\文档\PROJECTS(FINAL)\PROJECTS\Loan Eligibility Prediction\data\cleaned_data.csv"
df=pd.read_csv(url)

def preprocessing(X):

    cat_cols = X.select_dtypes(include='object').columns
    num_cols=X.select_dtypes(include=['int64','float64']).columns

    num_transformer = Pipeline(steps=[
        ("scaler", StandardScaler())
    ])

    cat_transformer = Pipeline(steps=[
        ("onehot", OneHotEncoder(handle_unknown="ignore"))
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", num_transformer, num_cols),
            ("cat", cat_transformer, cat_cols)
        ]
    )

    # X_processed = preprocessor.fit_transform(X)
    
    return preprocessor

if __name__=="__main__":
    preprocessing(df)
