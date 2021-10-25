import pandas as pd

movies = pd.read_csv('../files/movies.csv',
                     sep='|', #each column is divided by '|'
                     header=None, # no header was defined
                     skiprows=3) # skip 3 rows

def test_budget():
    assert movies.loc[:, 'budget'].min() == 105000000.0

test_budget()