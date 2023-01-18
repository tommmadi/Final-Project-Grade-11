from asyncio import sleep
from datetime import datetime, timedelta

import result_lookup


#lines 1-63, dictionary of cities teams including leagues that I don't have API keys for
# lookup = {"ANA": ["NHL|ANA"],
#           "ARI": ["NHL|ARI","NFL|ARI","MLB|ARI"],
#           "ATL": ["NBA|ATL","NFL|ATL","MLB|ATL","MLS|ATL"],
#           "AUS": ["MLS|AUS"],
#           "BAL": ["NFL|BAL","MLB|BAL"],
#           "BKN": ["NBA|BKN"],
#           "BOS": ["NHL|BOS","NBA|BOS","MLB|BOS"],
#           "BUF": ["NHL|BUF","NFL|BUF"],
#           "CAL": ["NHL|CGY"],
#           "CAR": ["NHL|CAR","NFL|CAR"],
#           "CHA": ["NBA|CHA","MLS|CHA"],
#           "CHI": ["NHL|CHI","NBA|CHI","NFL|CHI","MLB|CHC","MLS|CHI","MLB|CWS"],
#           "CIN": ["NFL|CIN","MLB|CIN","MLS|CIN"],
#           "CLB": ["NHL|CBJ", "MLS|CBS"],
#           "CLE": ["NBA|CLE","NFL|CLE","MLB|CLE"],
#           "COL": ["NHL|COL","MLB|COL","MLS|COL"],
#           "DAL": ["NHL|DAL","NBA|DAL","NFL|DAL","MLS|DAL"],
#           "DEN": ["NBA|DEN","NFL|DEN"],
#           "DET": ["NHL|DET","NBA|DET","NFL|DET","MLB|DET"],
#           "EDM": ["NHL|EDM"],
#           "FLA": ["NHL|FLA","MLB|FLA"],
#           "GB": ["NFL|GB"],
#           "HOU": ["NBA|HOU","NFL|HOU","MLB|HOU","MLS|HOU"],
#           "IND": ["NBA|IND","NFL|IND"],
#           "JAX": ["NFL|JAX"],
#           "KC": ["NFL|KC","MLB|KAN","MLS|KC"],
#           "LA": ["NHL|LA","NBA|LAL","NFL|LAR","MLB|LAA","MLS|LA","NBA|LAC","MLS|LAF","MLB|LAD","NFL|LAC"],
#           "LV": ["NHL|VGK","NFL|LV"],
#           "MEM": ["NBA|MEM"],
#           "MIA": ["NBA|MIA","NFL|MIA","MLS|MIA"],
#           "MIL": ["NBA|MIL","MLB|MIL"],
#           "MIN": ["NHL|MIN","NBA|MIN","NFL|MIN","MLB|MIN","MLS|MIN"],
#           "MTL": ["NHL|MTL","MLS|MTL"],
#           "NE": ["NFL|NE","MLS|NE"],
#           "NJ": ["NHL|NJ"],
#           "NO": ["NBA|NOP","NFL|NO"],
#           "NSH": ["NHL|NSH","MLS|NSH"],
#           "NY": ["NHL|NYI","NBA|NYK","NFL|NYG","MLB|NYM","MLS|NYR","NHL|NYR","NFL|NYJ","MLB|NYY","MLS|NYF"],
#           "OAK": ["MLB|OAK"],
#           "OKC": ["NBA|OKC"],
#           "ORL": ["NBA|ORL","MLS|ORL"],
#           "OTT": ["NHL|OTT"],
#           "PHI": ["NHL|PHI","NBA|PHI","NFL|PHI","MLB|PHI","MLS|PHI"],
#           "PHX": ["NBA|PHX"],
#           "PIT": ["NHL|PIT","NFL|PIT","MLB|PIT"],
#           "POR": ["NBA|POR","MLS|POR"],
#           "SAC": ["NBA|SAC"],
#           "SAS": ["NBA|SAS"],
#           "SD": ["MLB|SD"],
#           "SEA": ["NHL|SEA","NFL|SEA","MLB|SEA","MLS|SEA"],
#           "SF": ["NBA|GSW","NFL|SF","MLB|SF"],
#           "SJ": ["NHL|SJ","MLS|SJ"],
#           "SLC": ["MLB|RSL"],
#           "STL": ["NHL|STL","MLB|STL","MLS|STL"],
#           "TB": ["NHL|TB","NFL|TB","MLB|TB"],
#           "TEN": ["NFL|TEN"],
#           "TEX": ["MLB|TEX"],
#           "TOR": ["NHL|TOR","NBA|TOR","MLB|TOR","MLS|TOR"],
#           "UTA": ["NBA|UTA"],
#           "VAN": ["NHL|VAN","MLS|VAN"],
#           "WAS": ["NHL|WAS","NBA|WAS","NFL|WAS","MLB|WAS","MLS|DC"],
#           "WIN": ["NHL|WPG"],
#           "NHL": ["ANA","ARI","BOS","BUF","CGY","CAR","CHI","CBJ","COL",
#                   "DAL","DET","EDM","FLA","LA","VGK","MIN","MTL","NJ","NSH","NYR",
#                   "NYI","OTT","PHI","PIT","SEA","SJ","STL","TB","TOR","VAN","WAS","WPG"],
#           "NBA": ["ATL","BKN","BOS","CHA","CHI","CLE","DAL","DEN","DET",
#                   "HOU","IND","LAL","LAC","MEM","MIA","MIL","MIN","NOP","NYK","OKC",
#                   "ORL","PHI","PHX","POR","SAC","SAS","GSW","TOR","UTA","WAS"]}

lookup = {"ANA": ["NHL|ANA"],
          "ARI": ["NHL|ARI","NFL|ARI","MLB|ARI"],
          "ATL": ["NBA|ATL","NFL|ATL","MLB|ATL",],
          "BAL": ["NFL|BAL","MLB|BAL"],
          "BKN": ["NBA|BKN"],
          "BOS": ["NHL|BOS","NBA|BOS","MLB|BOS"],
          "BUF": ["NHL|BUF","NFL|BUF"],
          "CAL": ["NHL|CGY"],
          "CAR": ["NHL|CAR","NFL|CAR"],
          "CHA": ["NBA|CHA",],
          "CHI": ["NHL|CHI","NBA|CHI","NFL|CHI","MLB|CHC","MLB|CWS"],
          "CIN": ["NFL|CIN","MLB|CIN"],
          "CLB": ["NHL|CBJ"],
          "CLE": ["NBA|CLE","NFL|CLE","MLB|CLE"],
          "COL": ["NHL|COL","MLB|COL","MLS|COL"],
          "DAL": ["NHL|DAL","NBA|DAL","NFL|DAL","MLS|DAL"],
          "DEN": ["NBA|DEN","NFL|DEN"],
          "DET": ["NHL|DET","NBA|DET","NFL|DET","MLB|DET"],
          "EDM": ["NHL|EDM"],
          "FLA": ["NHL|FLA","MLB|FLA"],
          "GB": ["NFL|GB"],
          "HOU": ["NBA|HOU","NFL|HOU","MLB|HOU","MLS|HOU"],
          "IND": ["NBA|IND","NFL|IND"],
          "JAX": ["NFL|JAX"],
          "KC": ["NFL|KC","MLB|KAN","MLS|KC"],
          "LA": ["NHL|LA","NBA|LAL","NFL|LAR","MLB|LAA","MLS|LA","NBA|LAC","MLS|LAF","MLB|LAD","NFL|LAC"],
          "LV": ["NHL|VGK","NFL|LV"],
          "MEM": ["NBA|MEM"],
          "MIA": ["NBA|MIA","NFL|MIA","MLS|MIA"],
          "MIL": ["NBA|MIL","MLB|MIL"],
          "MIN": ["NHL|MIN","NBA|MIN","NFL|MIN","MLB|MIN","MLS|MIN"],
          "MTL": ["NHL|MTL","MLS|MTL"],
          "NE": ["NFL|NE","MLS|NE"],
          "NJ": ["NHL|NJ"],
          "NO": ["NBA|NOP","NFL|NO"],
          "NSH": ["NHL|NSH","MLS|NSH"],
          "NY": ["NHL|NYI","NBA|NYK","NFL|NYG","MLB|NYM","MLS|NYR","NHL|NYR","NFL|NYJ","MLB|NYY","MLS|NYF"],
          "OAK": ["MLB|OAK"],
          "OKC": ["NBA|OKC"],
          "ORL": ["NBA|ORL","MLS|ORL"],
          "OTT": ["NHL|OTT"],
          "PHI": ["NHL|PHI","NBA|PHI","NFL|PHI","MLB|PHI","MLS|PHI"],
          "PHX": ["NBA|PHX"],
          "PIT": ["NHL|PIT","NFL|PIT","MLB|PIT"],
          "POR": ["NBA|POR","MLS|POR"],
          "SAC": ["NBA|SAC"],
          "SAS": ["NBA|SAS"],
          "SD": ["MLB|SD"],
          "SEA": ["NHL|SEA","NFL|SEA","MLB|SEA","MLS|SEA"],
          "SF": ["NBA|GSW","NFL|SF","MLB|SF"],
          "SJ": ["NHL|SJ","MLS|SJ"],
          "SLC": ["MLB|RSL"],
          "STL": ["NHL|STL","MLB|STL","MLS|STL"],
          "TB": ["NHL|TB","NFL|TB","MLB|TB"],
          "TEN": ["NFL|TEN"],
          "TEX": ["MLB|TEX"],
          "TOR": ["NHL|TOR","NBA|TOR","MLB|TOR","MLS|TOR"],
          "UTA": ["NBA|UTA"],
          "VAN": ["NHL|VAN","MLS|VAN"],
          "WAS": ["NHL|WAS","NBA|WAS","NFL|WAS","MLB|WAS","MLS|DC"],
          "WIN": ["NHL|WPG"],
          "NHL": ["ANA","ARI","BOS","BUF","CGY","CAR","CHI","CBJ","COL",
                  "DAL","DET","EDM","FLA","LA","VGK","MIN","MTL","NJ","NSH","NYR",
                  "NYI","OTT","PHI","PIT","SEA","SJ","STL","TB","TOR","VAN","WAS","WPG"],
          "NBA": ["ATL","BKN","BOS","CHA","CHI","CLE","DAL","DEN","DET",
                  "HOU","IND","LAL","LAC","MEM","MIA","MIL","MIN","NOP","NYK","OKC",
                  "ORL","PHI","PHX","POR","SAC","SAS","GSW","TOR","UTA","WAS"]}

Valid_City = False
item = 0
length = 0
input_length = 0

# leagues = "NHL", "MLB", "MLS", "NBA", "NFL"

leagues = "MLB", "NBA", "NHL"
while not Valid_City:
    city = input("Search Any City/League For The A Sports Update: ")
    if city in lookup:
        if city in leagues:
            length = len(lookup[city])
            # print("Here Is The Sports Update For The", length, "Teams In The", city)
            Valid_City = True
        else:
            length = len(lookup[city])
            # print("Here Is The Sports Update For The", length, "Teams In", city)
            Valid_City = True
    else:
        print("That Is Not A Valid City/League")

# yyyy/mm/dd (if you don't enter a day, we will show yesterdays results)
while input_length == 0:
    input_date = input("Enter A Date In The Format YYYY/MM/DD (leave blank for yesterday): ")
    if input_date == "":
        yesterday = datetime.now() - timedelta(1)
        input_date = datetime.strftime(yesterday, '%Y/%m/%d')
        print(input_date)
    if len(input_date) != 0:
        input_length = len(input_date)

while item < length:
    new = lookup[city][item].split("|")
    print("league: " + new[0] + " team: " + new[1])
    result_lookup.res_look(new[1], new[0], input_date)
    # sleep(0.1)
    # print(lookup[city][item],":")

    item = item+1




