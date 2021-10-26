import numpy as np
import pandas as pd

col_names = ['Title', 'Air date', 'Production code', 'Season', 'Number in season',
             'Number in series', 'US viewers (million)', 'Views', 'IMDB rating']
             
# Requirements
#- Use correct separator as data is tabular separated.
#- Use the following `col_names` list as column names.
#- Load just `Title`, `Air date`, `Production code` and `IMDB rating`.
#- Don't load the first empty columns.
#- Set `Production code` as index.
#- Null values are encoded as `no_val` values, be careful with that when loading the data.
#- Parse the `Air date` columns as Date.

using_col = ['Title', 'Air date', 'Production code', 'IMDB rating']

simpson_df = pd.read_csv('files/simpsons-episodes.tsv',
                     sep='\t',
                     encoding='UTF-8',
                     header=None, # no header was defined
                     names=col_names,
                     usecols=using_col,
                     skiprows=1,
                     index_col='Production code',
                     parse_dates=['Air date'],
                     na_values=['no_val'])

print(simpson_df.head())