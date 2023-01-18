from time import sleep

import requests
import json
from pprint import pprint


def res_look(lteam, lleague, ldate):

    if lleague == "NBA":
        url = "https://api.sportradar.com/nba/trial/v7/en/games/" + ldate + "/schedule.json?api_key=vd86r5thtnug6e4zccvgwb4r"
    elif lleague == "MLB":
        url = "https://api.sportradar.com/mlb/trial/v7/en/games/" + ldate + "/boxscore.json?api_key=3ughsyzsev7zv77nbmmcae5q"
    elif lleague == "NHL":
        url = "https://api.sportradar.us/nhl/trial/v7/en/games/" + ldate + "/schedule.json?api_key=aahfrx7shknnmup4tkrbc5rk"
    elif lleague == "NFL":
        url = "https://api.sportradar.com/mlb/trial/v7/en/games/" + ldate + "/boxscore.json?api_key=3ughsyzsev7zv77nbmmcae5q"
        return
    elif lleague == "MLS":
        url = "https://api.sportradar.com/mlb/trial/v7/en/games/" + ldate + "/boxscore.json?api_key=3ughsyzsev7zv77nbmmcae5q"
        return

    # print(url)

    game_count = 0
    response = requests.get(url)

    if response.text == "<h1>Developer Over Qps</h1>":
        sleep(1)
        response = requests.get(url)

    # print("len response " + str(len(response.text)))

    res = json.loads(response.text)
    # pprint(res)

    if lleague == "MLB":
        if 'games' in res['league']:
            game_count = len(res['league']['games'])
        else:
            game_count = 0
    elif lleague == "NBA" or lleague == "NHL":
        if 'games' in res:
            game_count = len(res['games'])
        else:
            game_count = 0

    current_game = 0

    while current_game < game_count:

        if lleague == "MLB":
            home = res['league']['games'][current_game]['game']['home']['abbr']
            away = res['league']['games'][current_game]['game']['away']['abbr']
            home_text = res['league']['games'][current_game]['game']['home']['market'] + " " + res['league']['games'][current_game]['game']['home']['name']
            away_text = res['league']['games'][current_game]['game']['away']['market'] + " " + res['league']['games'][current_game]['game']['away']['name']
            home_score = res['league']['games'][current_game]['game']['home']['runs']
            away_score = res['league']['games'][current_game]['game']['away']['runs']
        elif lleague == "NBA" or lleague == "NHL":
            home = res['games'][current_game]['home']['alias']
            away = res['games'][current_game]['away']['alias']
            home_text = res['games'][current_game]['home']['name']
            away_text = res['games'][current_game]['away']['name']
            if res['games'][current_game]['status'] != 'unnecessary':
                home_score = res['games'][current_game]['home_points']
                away_score = res['games'][current_game]['away_points']

        if home == lteam:
            if home_score > away_score:
                result = "and won " + str(home_score) + " to " + str(away_score)
            else:
                result = "and lost " + str(away_score) + " to " + str(home_score)
            print(home_text, "played", away_text, result, "- home game")
        if away == lteam:
            if home_score > away_score:
                result = "and lost " + str(home_score) + " to " + str(away_score)
            else:
                result = "and won " + str(away_score) + " to " + str(home_score)
            print(away_text, "played", home_text, result, "- away game")
        current_game = current_game + 1