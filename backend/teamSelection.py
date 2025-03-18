import pulp as p

def build_best_team(player_list):
    player_list = [player for player in player_list if
                player["position"] in {"GKP", "DEF", "MID", "FWD"}]
    #
    sorted_players = sorted(player_list, key=lambda x: x["xPoints"], reverse=True)

    position_groups = {"GKP": [], "DEF": [], "MID": [], "FWD": []}

    for player in sorted_players:
        position_groups[player["position"]].append(player)

    itb = 100
    team = []
    team.extend(position_groups["GKP"][:1])
    itb = itb - position_groups["GKP"][0]['cost']

    team.extend(position_groups["DEF"][:3])
    itb = itb - position_groups["DEF"][0]['cost']
    itb = itb - position_groups["DEF"][1]['cost']
    itb = itb - position_groups["DEF"][2]['cost']

    team.extend(position_groups["MID"][:2])
    itb = itb - position_groups["MID"][0]['cost']
    itb = itb - position_groups["MID"][1]['cost']

    team.extend(position_groups["FWD"][:1])

    print(round(itb))

    all_remaining = position_groups["GKP"][1:] + position_groups["DEF"][3:] + position_groups["MID"][3:] + position_groups["FWD"][1:]

    nDEF = 3
    nMID = 2
    nFWD = 1
    remaining = 4

    for player in all_remaining:
        if remaining > 0:
            if player["position"] == "GKP":
                continue  # Skip extra goalkeepers

            elif player["position"] == "DEF" and nDEF < 5:
                team.append(player)
                nDEF += 1
                remaining -= 1

            elif player["position"] == "MID" and nMID < 5:
                team.append(player)
                nMID += 1
                remaining -= 1

            elif player["position"] == "FWD" and nFWD < 3:
                team.append(player)
                nFWD += 1
                remaining -= 1

    print("\n🏆 Best Fantasy Team of the Week 🏆")
    for player in team:
        print(f"{player['name']} ({player['position']}): xPoints {round(player['xPoints'], 2)}")

    return team