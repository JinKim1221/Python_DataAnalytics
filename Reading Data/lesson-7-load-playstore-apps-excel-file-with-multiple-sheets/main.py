import numpy as np
import pandas as pd
# Requirements
# Using the `playstore.xlsx` Excel file from the given `data_url` and:
# - Save in a `playstore_df` variable the `Google_playstore` sheet. Use the first column as index.
# - Save in a `content_id_df` variable the `Content_ID` sheet. Use `Content_ID` as index.

data_url = 'https://github.com/ine-rmotr-projects/project-files/files/4086772/playstore.xlsx'
playstore_df = pd.read_excel( data_url,
                              sheet_name='Google_playstore',
                              index_col=[0])

content_id_df = pd.read_excel( data_url,
                               sheet_name='Content_ID',
                               index_col='Content_ID')

# Same result; but different function of reading excel file
# file = pd.ExcelFile(data_url)
# playstore_df = file.parse(index_col=0)
# content_id_df = file.parse('Content_ID', 
#                           index_col='Content_ID')

    