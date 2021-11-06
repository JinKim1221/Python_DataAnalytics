import numpy as np
import pandas as pd
import requests

# Requirements
# - Read and store in a `fifa_df` DataFrame the HTML table found in the `fifa_players.html` file 
#   that contains the top 30 FIFA players as of Oct. 30, 2019. 
#   The `fifa_players.html` file is a dump generated from this URL: https://www.fifaindex.com/players/top/fifa20_363/
# - Remove the first two columns and the last one from the resulting `fifa_df` DataFrame, as they are `Unnamed` and filled with `NaN` objects.
# - Create a `most_hits_player` variable containing the player with the most amount of `Hits`.

fifa_df = pd.read_html('files/fifa_players.html', encoding='utf-8')

fifa_df = fifa_df[0].iloc[:, 2:-1]
most_hits_player = fifa_df.sort_values('Hits', ascending=False).head(1)

print(fifa_df)