import numpy as np
import pandas as pd

column_names = ['color', 'director_name', 'num_critic_for_reviews', 'duration',
                'gross', 'movie_title', 'num_user_for_reviews',	'country',
                'cotent_rating', 'budget', 'title_year', 'imdb_score', 'genre']

# Requirements
# 1. Use the appropriate separator.
# 2. The given data doesn't have a defined header. Use the column names given in the `column_names` variable.
# 3. Skip the first 3 rows.

movies = pd.read_csv('../files/movies.csv',
                     sep='|', #each column is divided by '|'
                     header=None, # no header was defined
                     names=column_names, #given columns' name
                     skiprows=3) # skip 3 rows

print(movies.head())