<<<<<<< HEAD
from time import sleep
=======
# import http.client
#
# conn = http.client.HTTPSConnection("api.sportradar.com")
#
# conn.request("GET", "/mlb/trial/v7/en/games/2023/01/16/boxscore.xml?api_key=6ujezamjxp3hfhdqxqefkygg")
#
# res = conn.getresponse()
# data = res.read()
#
# print(data.decode("utf-8"))
>>>>>>> origin/main

import requests
import json
from pprint import pprint

<<<<<<< HEAD

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
=======
# leagues = ["mlb", "nba", "nhl", "nba"];
# leagueapis = ["3ughsyzsev7zv77nbmmcae5q", "aahfrx7shknnmup4tkrbc5rk", "aahfrx7shknnmup4tkrbc5rk", "6ujezamjxp3hfhdqxqefkygg"]
resultdate = "2023/1/13"
leagues = ["mlb", "nba"] #, "nhl", "nfl"];
leagueurl = ["https://api.sportradar.com/mlb/trial/v7/en/games/" + resultdate + "/boxscore.json?api_key=3ughsyzsev7zv77nbmmcae5q",
             "https://api.sportradar.com/nba/trial/v7/en/games/" + resultdate + "/schedule.json?api_key=vd86r5thtnug6e4zccvgwb4r",
             # "https://api.sportradar.us/nhl/trial/v7/en/games/" + resultdate + "/schedule.json?api_key=aahfrx7shknnmup4tkrbc5rk"
             # "https://api.sportradar.us/nfl/official/trial/v7/en/games/" + resultdate + "/{nfl_season_week}/schedule.{format}?api_key={your_api_key}"
]

# https://api.sportradar.us/nhl/{access_level}/{version}/{language_code}/games/{year}/{month}/{day}/schedule.{format}?api_key={your_api_key}

result = 0
currentgame = 0
gamecount = 0
leaguecount = len(leagues)
currentleague = 0
leagueacronym = 0

while currentleague < leaguecount:
    url = leagueurl[currentleague]
    currentleaguename = leagues[currentleague]
    print(currentleaguename)
    # print(url)
    # currentleague = currentleague + 1
    response = requests.get(url)
    # print(response.text)
    # print("got here")
    # res= response.text['league']['games']
    res = json.loads(response.text)
    if currentleaguename == "mlb":
        if 'games' in res['league']:
            gamecount = len(res['league']['games'])
        else:
            gamecount = 0
    elif currentleaguename == "nba":
        if 'games' in res:
            gamecount = len(res['games'])
        else:
            gamecount = 0

    currentgame = 0
    # temp, hard-code variables for testing
    find = 'WAS'

    while currentgame < gamecount:

        if currentleaguename == "mlb":
            home = res['league']['games'][currentgame]['game']['home']['abbr']
            away = res['league']['games'][currentgame]['game']['away']['abbr']
            hometext = res['league']['games'][currentgame]['game']['home']['market'] + " " + res['league']['games'][currentgame]['game']['home']['name']
            awaytext = res['league']['games'][currentgame]['game']['away']['market'] + " " + res['league']['games'][currentgame]['game']['away']['name']
            homescore = res['league']['games'][currentgame]['game']['home']['runs']
            awayscore = res['league']['games'][currentgame]['game']['away']['runs']
        elif currentleaguename == "nba":
            home = res['games'][currentgame]['home']['alias']
            away = res['games'][currentgame]['away']['alias']
            hometext = res['games'][currentgame]['home']['name']
            awaytext = res['games'][currentgame]['away']['name']
            if res['games'][currentgame]['status'] != 'unnecessary':
                homescore = res['games'][currentgame]['home_points']
                awayscore = res['games'][currentgame]['away_points']
        # elif currentleaguename == "mlb":
        #     home = res['league']['games'][currentgame]['game']['home']['abbr']
        #     away = res['league']['games'][currentgame]['game']['away']['abbr']
        #     hometext = res['league']['games'][currentgame]['game']['home']['market'] + " " + res['league']['games'][currentgame]['game']['home']['name']
        #     awaytext = res['league']['games'][currentgame]['game']['away']['market'] + " " + res['league']['games'][currentgame]['game']['away']['name']
        #     homescore = res['league']['games'][currentgame]['game']['home']['runs']
        #     awayscore = res['league']['games'][currentgame]['game']['away']['runs']

        if home == find:
            if homescore > awayscore:
                result = "and won " + str(homescore) + " to " + str(awayscore)
            else:
                result = "and lost " + str(awayscore) + " to " + str(homescore)
            print(hometext, "played", awaytext, result, "- home game")
        if away == find:
            if homescore > awayscore:
                result = "and lost " + str(homescore) + " to " + str(awayscore)
            else:
                result = "and won " + str(awayscore) + " to " + str(homescore)
            print(awaytext, "played", hometext, result, "- away game")
        currentgame = currentgame + 1
    currentleague = currentleague + 1
#print(res)
>>>>>>> origin/main
