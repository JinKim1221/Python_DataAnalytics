import numpy as np
import pandas as pd
import json
from pandas.io.json import json_normalize

with open('files/artists.json') as file:
    json_dict = json.load(file)


artists = pd.json_normalize(json_dict)

biography = pd.json_normalize(json_dict,
                           record_path='bio',
                           meta=['name'])
print(biography)
