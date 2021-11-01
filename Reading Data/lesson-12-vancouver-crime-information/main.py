import numpy as np
import pandas as pd
import sqlite3

# Requirements
# Using the given sqlite3 connection:
# - Store all the crimes committed after 18:00 h in a `late_crimes` variable.
# - Store the number of crimes committed on the month with most crimes in a `dangerous_month_crimes` variable.
# create a new connection to a db in memory

conn = sqlite3.connect(':memory:')

# create a cursor
c = conn.cursor()

# restore the given van_crime_2003.sql dump
c.executescript(open('files/van_crime_2003.sql', 'r').read())

# your code goes here

df = pd.read_sql('SELECT * FROM van_crimes ', conn)

late_crimes = df.loc[df['HOUR'] > 18]

dangerous_month_crimes = df.loc[:, ['MONTH','TYPE']].value_counts().head(1)
print(dangerous_month_crimes)
