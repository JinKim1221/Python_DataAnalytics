import numpy as np
import pandas as pd
import sqlite3

# Using the given sqlite3 connection:
# - Select `TYPE`, `MONTH`, `DAY` and `NEIGHBOURHOOD` from the `van_crimes` table, but only the crime observations from `Stanley Park` or `West End`. Store the information in a `van_crimes_df` DataFrame.
# - Store the count of crimes per `TYPE` in a `crime_types_count` variable.

# create a new connection to a db in memory
conn = sqlite3.connect(':memory:')

# create a cursor
c = conn.cursor()

# restore the given van_crime_2003.sql dump
c.executescript(open('files/van_crime_2003.sql', 'r').read())

# your code goes here

van_crimes_df =pd.read_sql('select TYPE, MONTH, DAY, NEIGHBOURHOOD from van_crimes where neighbourhood == "Stanley Park" or neighbourhood == "West End"', conn)
crime_types_count = van_crimes_df['TYPE'].value_counts()
print(crime_types_count)