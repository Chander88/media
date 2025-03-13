import pandas as pd
import os
import glob

# Create output directory if it doesn't exist
output_dir = "csv_output"
os.makedirs(output_dir, exist_ok=True)

# Find all Excel files
excel_files = glob.glob("*.xlsx")

for excel_file in excel_files:
    # Read the Excel file
    df = pd.read_excel(excel_file)
    
    # Convert to CSV
    csv_filename = os.path.join(output_dir, os.path.splitext(excel_file)[0] + ".csv")
    df.to_csv(csv_filename, index=False)

print("Excel files converted to CSV successfully!")

