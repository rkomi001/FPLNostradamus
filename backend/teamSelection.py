import pulp as p
from pulp import LpMaximize, LpProblem, LpVariable, lpSum


def build_best_team(player_list):
    player_list = [player for player in player_list if
                player["position"] in {"GKP", "DEF", "MID", "FWD"}]
    #
    sorted_players = sorted(player_list, key=lambda x: x["xPoints"], reverse=True)

    position_groups = {"GKP": [], "DEF": [], "MID": [], "FWD": []}

    for player in sorted_players:
        position_groups[player["position"]].append(player)

    #Definisanje problema Maksimizacije

    model = LpProblem("model",LpMaximize)

    #Upravljacke promenjive

    player_vars = {player["name"]: LpVariable(player["name"], cat="Binary") for player in player_list}
    #print(player_vars)

    #Funkcija
    model += lpSum(player["xPoints"] * player_vars[player["name"]] for player in player_list), "Ukupno poena"

    #Ogranicenja za cenu
    model += lpSum(player["cost"]*player_vars[player["name"]] for player in player_list)<=100, "Limit budzeta"

    #Ogranicenje za ukupan broj igraca
    model+= lpSum(player_vars[player["name"]] for player in player_list)==11, "Maksimalan broj igraca"

    model += lpSum(player_vars[player["name"]] for player in player_list if player["position"] == "GKP") == 1, "GK_Constraint"
    model += lpSum(player_vars[player["name"]] for player in player_list if player["position"] == "DEF") >= 3, "Min_DEF"
    model += lpSum(player_vars[player["name"]] for player in player_list if player["position"] == "DEF") <= 5, "Max_DEF"
    model += lpSum(player_vars[player["name"]] for player in player_list if player["position"] == "MID") >= 2, "Min_MID"
    model += lpSum(player_vars[player["name"]] for player in player_list if player["position"] == "MID") <= 5, "Max_MID"
    model += lpSum(player_vars[player["name"]] for player in player_list if player["position"] == "FWD") >= 1, "Min_FWD"
    model += lpSum(player_vars[player["name"]] for player in player_list if player["position"] == "FWD") <= 3, "Max_FWD"


    #print(model)

    model.solve()

    team = [player for player in player_list if player_vars[player["name"]].value()==1]

    print("\n🏆 Best Fantasy Team of the Week 🏆")
    for player in team:
        print(f"{player['name']} ({player['position']}): xPoints {round(player['xPoints'], 2)}")

    return team