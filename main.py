import pandas as pd
from openpyxl import load_workbook
from openpyxl.worksheet.table import Table, TableStyleInfo
import os
import sys

#potential for command line arguments that take in media directory and excel file
def main():

    excel_file = 'sample_shot_sheet.xlsx'
    folder_path = ''

    required_columns = ['Camera', 'Film Brand', 'Film Stock', 'Load Date', 'Unload Date']
    
    try:
        df = pd.read_excel(excel_file, sheet_name=1)
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return
    


    # check if all required columns are present
    if not all(col in df.columns for col in required_columns):
        print("Error: Required columns are missing from the Excel file.")
        return
    # once we have the table, we'll filter out empty loaded dates and unload dates with none
    df_filtered = df[df['Unload Date'] != 'INCOMPLETE']
    
    
    # get rid of rows that have been developed and scanned already
    df_filtered = df_filtered[df_filtered['Developed'].isna()]
    df_filtered = df_filtered[df_filtered['Scanned'].isna()]



    print(df_filtered)
  

    # start at folder photography/2026/film then direct to the correct folder for the camera or make folder for camera if it does not exist

    # folder naming convention is | Film brand | film stock | roll start date in YYYY-MM-DD | roll end date


    
    return


if __name__ == '__main__':
    main()
