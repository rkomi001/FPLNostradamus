import requests

from dataProcessing import fetch_fpl_data


def fetch_my_team():
    session = requests.session()

    headers = {"User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1; PRO 5 Build/LMY47D)", 'accept-language': 'en'}

    data = {"login": "djordjemirkovic001@gmail.com", "password": "Mirkolol22!", "app": "plfpl-web",
            "redirect_uri": "https://fantasy.premierleague.com/a/login"}

    url = "https://users.premierleague.com/accounts/login/"

    res = session.post(url, data=data, headers=headers)

    team_url = "https://fantasy.premierleague.com/api/my-team/7659234/"

    res = session.get(team_url)
    data = res.json()  # Convert response to JSON
    team = data["picks"]  # Now access the "picks" key

    players = fetch_fpl_data()

    player_dict = {p["id"]: p for p in players}
    for selected_player in team:
        player_id = selected_player["element"]

        if player_id in player_dict:
            selected_player.update(player_dict[player_id])



    return team