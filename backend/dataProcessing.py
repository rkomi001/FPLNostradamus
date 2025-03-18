from gc import is_finalized
from itertools import count

import requests
def fetch_fpl_data():
# URL of a public API
    url ="https://fantasy.premierleague.com/api/bootstrap-static/"
# Sending a GET request
    response = requests.get(url)

# Check if the request was successful
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data. Status code: {response.status_code}")
        # Convert response to JSON
    data = response.json()
        #print(response.json())
    #print(data.keys())
    players = data["elements"]
    teams = {team["id"]: team["name"] for team in data["teams"]}
    positions = {1: "GKP", 2: "DEF", 3: "MID", 4: "FWD", 5:"MNG"}

    player_list = []
    for player in players:
        player_info = {
        "name": player["first_name"]+" "+player["second_name"],
        "team": teams[player["team"]],
        "position": positions[player["element_type"]],
        "form": float(player["form"]) if player["form"] else 0,
        "ppg": player["points_per_game"],
        "cost": player["now_cost"]/10,
        "total_points": player["total_points"],
        "xPoints": float(player["form"])

        }
        player_list.append(player_info)
    return player_list