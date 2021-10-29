import numpy as np
import pandas as pd

# This exercise will take a few steps to complete successfully. Have a look at the `artists.json` file before starting so you have an idea of the structure and information contained.

# - Read the `artists.json` into an `artists` DataFrame variable, without using `json_normalize`.
# - Remove the `bio` column.
# - Set the `name` column as index.
# - Save it as `artists.csv` keeping the index.

artists = pd.read_json('files/artists.json')

artists = artists.drop(columns="bio").set_index('name')
print(artists.head())

artists.to_csv('artists.csv')
# for col in artists.columns:
#     print(col)