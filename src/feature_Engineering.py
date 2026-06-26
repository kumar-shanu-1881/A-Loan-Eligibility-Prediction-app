import pandas as pd
import numpy as np

# Load the raw data
url=r"C:\Users\bnsah\OneDrive\文档\PROJECTS(FINAL)\PROJECTS\Loan Eligibility Prediction\data\cleaned_data.csv"
df=pd.read_csv(url)

# print(df.head())
# print(df.columns)
def featureEng(df):
    df['Income_Loan_Ratio'] = df['Income'] / df['LoanAmount']
    df["Employment_Stability"] = df["MonthsEmployed"] / 12
    df["High_DTI_Flag"] = (df["DTIRatio"] > 0.4).astype(int)
    def credit_bucket(score):
        if score < 580:
            return "Poor"
        elif score < 670:
            return "Fair"
        elif score < 740:
            return "Good"
        else:
            return "Excellent"

    df["credit_score_category"] = df["CreditScore"].apply(credit_bucket)

    df["log_loan_amount"] = np.log1p(df["LoanAmount"])
    df["log_income"] = np.log1p(df["Income"])

    df.drop(columns=[
        "MonthsEmployed"
    ], inplace=True)

    return df

if __name__=="__main__":
    featureEng(df)