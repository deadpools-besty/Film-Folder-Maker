import pandas as pd
from openpyxl import load_workbook
from openpyxl.worksheet.table import Table, TableStyleInfo
import os
import sys

#potential for command line arguments that take in media directory and excel file
def main():

    excel_file = 'sample_shot_sheet.xlsx'
    folder_path = ''
    table_name = 'Table2'

    wb = load_workbook(filename=excel_file)
    ws = wb.active
    tb = ws.tables['Table2']
    return


if __name__ == '__main__':
    main()
