import pandas as pd
from openpyxl import load_workbook
from openpyxl.worksheet.table import Table, TableStyleInfo
import os
import sys
from openpyxl.worksheet.filters import (
    FilterColumn,
    CustomFilter,
    CustomFilters,
    DateGroupItem,
    Filters,
    BlankFilter
    )
#potential for command line arguments that take in media directory and excel file
def main():

    excel_file = 'sample_shot_sheet.xlsx'
    folder_path = ''
    table_name = 'Table2'

    wb = load_workbook(filename=excel_file)
    ws = wb.active
    tb = ws.tables['Table2']
    # once we have the table, we'll filter out empty loaded dates and unload dates with none
    
    blank = BlankFilter()
    
    # filter for rows that have not been dev'd yet. this is how we'll control which folders are made

    # start at folder photography/2026/film then direct to the correct folder for the camera or make folder for camera if it does not exist

    # folder naming convention is Film brand, film stock, roll start date in YYYY-MM-DD, roll end date


    print(tb)
    return


if __name__ == '__main__':
    main()
