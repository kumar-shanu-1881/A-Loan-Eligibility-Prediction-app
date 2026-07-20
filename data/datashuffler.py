import pandas as pd

def merge_and_shuffle(excel_1, excel_2, csv_1, output_filename):
    print("Reading files...")
    # Read the two Excel files
    df1 = pd.read_excel(excel_1)
    df2 = pd.read_excel(excel_2)
    
    # Read the CSV file
    df3 = pd.read_csv(csv_1)
    
    print("Merging files...")
    # Merge the three dataframes together
    # ignore_index=True ensures the new dataframe has a fresh continuous index
    merged_df = pd.concat([df1, df2, df3], ignore_index=True)
    
    print("Shuffling rows...")
    # Shuffle the rows randomly
    # frac=1 means return 100% of the rows in a random order
    shuffled_df = merged_df.sample(frac=1).reset_index(drop=True)
    
    print(f"Saving to {output_filename}...")
    # Save the final dataframe to a new CSV file
    # If you prefer to save it as an Excel file, use: shuffled_df.to_excel(output_filename, index=False)
    shuffled_df.to_csv(output_filename, index=False)
    
    print("Done!")

# --- Configuration ---
# Replace these with your actual file paths
EXCEL_FILE_1 = 'PROJECTS\Loan Eligibility Prediction\data\synthetic_loan_dataset_75000.xlsx'
EXCEL_FILE_2 = 'PROJECTS\Loan Eligibility Prediction\data\synthetic_loan_dataset_50000.xlsx'
CSV_FILE = 'PROJECTS\Loan Eligibility Prediction\data\Loan_default.csv'
OUTPUT_FILE = 'new_Loan_Default.csv'

if __name__ == "__main__":
    merge_and_shuffle(EXCEL_FILE_1, EXCEL_FILE_2, CSV_FILE, OUTPUT_FILE)