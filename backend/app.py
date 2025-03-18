from flask import Flask, jsonify
from flask_cors import CORS
from dataProcessing import fetch_fpl_data  # Import your function
from teamSelection import build_best_team  # Import your function

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "welcome to FPL API"})

@app.route('/best_team')
def best_team():
    players = fetch_fpl_data()
    team = build_best_team(players)
    return jsonify(team)

if __name__=="__main__":
    app.run(debug=True)
