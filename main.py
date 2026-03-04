import pandas as pd
import openpyxl as pyxl
import os
import sys

#potential for command line arguments that take in media directory and excel file
def main():

    excel_file = 'sample_shot_sheet.xlsx'
    folder_path = ''

    df = pyxl.load_workbook(excel_file)
    df1 = df.active

    for row in range(0, df1.max_row):
        for col in df1.iter_cols(1, df1.max_column):
            print(col[row].value)


    return


if __name__ == '__main__':
    main()
