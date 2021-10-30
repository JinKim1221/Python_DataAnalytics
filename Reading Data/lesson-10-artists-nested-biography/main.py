from os import sep
from sys import path
import numpy as np
import pandas as pd
import json
from pandas.io.json import json_normalize

# This exercise will take a few steps to complete successfully. Have a look at the `artists.json` file before starting so you have an idea of the structure and information contained.

# - Read the `artists.json` into an `artists` DataFrame variable, using `json_normalize`. Keep the default index.
# - Using the `bio` column, create a new `biography` DataFrame variable with the bio of each artist.
# - When creatng the `biography` DataFrame also add the `name` column.



with open('files/artists.json') as file:
    json_dict = json.load(file)

artists = pd.json_normalize(json_dict)
biography = json_normalize(json_dict, sep='_', record_path='bio', meta=['name'])


print(biography)
