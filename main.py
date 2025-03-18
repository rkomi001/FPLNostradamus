from backend.dataProcessing import fetch_fpl_data
from backend.teamSelection import build_best_team

def main():
    print("Fetching FPL data...")
    players = fetch_fpl_data()

    print("Building best team...")
    best_team = build_best_team(players)

if __name__ == "__main__":
    main()