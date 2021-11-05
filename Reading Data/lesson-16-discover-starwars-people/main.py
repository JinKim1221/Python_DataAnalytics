from os import startfile
import numpy as np
import pandas as pd
import requests

# Requirements 
# - Using the _requests_ library make a GET request to https://swapi.co/api/people/?format=json to get the `people` of StarWars universe.
# - Store the JSON response into a `starwars_people_df` DataFrame variable.
# - Filter blue-eyed characters on `blue_eyed_people_df`.
# > SWAPI is a StarWars REST API with information about  `people`, `films`, `starships` and `planets` within the StarWars universe.


req = requests.get('https://swapi.dev/api/people')
json_dict = req.json()

starwars_people_df = pd.DataFrame.from_dict(json_dict['results'])
print(starwars_people_df.columns)

blue_eyed_people_df = starwars_people_df.loc[starwars_people_df['eye_color'] == 'blue']
print(blue_eyed_people_df)