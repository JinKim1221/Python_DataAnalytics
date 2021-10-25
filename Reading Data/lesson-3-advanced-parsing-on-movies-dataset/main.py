import numpy as np
import pandas as pd
# Requirements
#- Use the appropriate separator.
#- The given data doesn't have a defined header. Use the column names given in the `column_names` variable.
#- Missing values are encoded as `?` characters. Parse those values as `NaN` objects.
#- The `budget` column has commas separating the thousands, make sure the column is of float data type.
#- The index of the DataFrame should be represented by the `movie_title` column.
column_names = ['color', 'director_name', 'num_critic_for_reviews', 'duration',
                'gross', 'movie_title', 'num_user_for_reviews',	'country',
                'cotent_rating', 'budget', 'title_year', 'imdb_score', 'genre']

movies = pd.read_csv('../files/movies.csv',
                     sep='|', #each column is divided by '|'
                     header=None, # no header was defined
                     names=column_names, #given columns' name
                     thousands=',', # make sure column 'budget' is of float data type.
                     na_values='?', # value'?' is replaced to 'NaN'
                     index_col='movie_title')


print(movies['budget'].dtype)