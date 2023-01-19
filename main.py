from datetime import datetime, timedelta
import result_lookup

#lines 10-75, dictionary of cities teams including leagues that I don't have API keys for

lookup = {"ANA": ["NHL|ANA"],
          "ARI": ["NHL|ARI","MLB|ARI"],
          "ATL": ["NBA|ATL","MLB|ATL",],
          "BAL": ["MLB|BAL"],
          "BKN": ["NBA|BKN"],
          "BOS": ["NHL|BOS","NBA|BOS","MLB|BOS"],
          "BUF": ["NHL|BUF"],
          "CAL": ["NHL|CGY"],
          "CAR": ["NHL|CAR"],
          "CHA": ["NBA|CHA",],
          "CHI": ["NHL|CHI","NBA|CHI","MLB|CHC","MLB|CWS"],
          "CIN": ["MLB|CIN"],
          "CLB": ["NHL|CBJ"],
          "CLE": ["NBA|CLE","MLB|CLE"],
          "COL": ["NHL|COL","MLB|COL"],
          "DAL": ["NHL|DAL","NBA|DAL"],
          "DEN": ["NBA|DEN"],
          "DET": ["NHL|DET","NBA|DET","MLB|DET"],
          "EDM": ["NHL|EDM"],
          "FLA": ["NHL|FLA","MLB|FLA"],
          "HOU": ["NBA|HOU","MLB|HOU"],
          "IND": ["NBA|IND"],
          "KC": ["MLB|KAN"],
          "LA": ["NHL|LA","NBA|LAL","MLB|LAA","NBA|LAC","MLB|LAD"],
          "LV": ["NHL|VGK"],
          "MEM": ["NBA|MEM"],
          "MIA": ["NBA|MIA"],
          "MIL": ["NBA|MIL","MLB|MIL"],
          "MIN": ["NHL|MIN","NBA|MIN","NFL|MIN","MLB|MIN"],
          "MTL": ["NHL|MTL"],
          "NE": ["NFL|NE"],
          "NJ": ["NHL|NJ"],
          "NO": ["NBA|NOP","NFL|NO"],
          "NSH": ["NHL|NSH"],
          "NY": ["NHL|NYI","NBA|NYK","NFL|NYG","MLB|NYM","NHL|NYR","NFL|NYJ","MLB|NYY"],
          "OAK": ["MLB|OAK"],
          "OKC": ["NBA|OKC"],
          "ORL": ["NBA|ORL"],
          "OTT": ["NHL|OTT"],
          "PHI": ["NHL|PHI","NBA|PHI","NFL|PHI","MLB|PHI"],
          "PHX": ["NBA|PHX"],
          "PIT": ["NHL|PIT","NFL|PIT","MLB|PIT"],
          "POR": ["NBA|POR"],
          "SAC": ["NBA|SAC"],
          "SAS": ["NBA|SAS"],
          "SD": ["MLB|SD"],
          "SEA": ["NHL|SEA","NFL|SEA","MLB|SEA"],
          "SF": ["NBA|GSW","NFL|SF","MLB|SF"],
          "SJ": ["NHL|SJ"],
          "SLC": ["MLB|RSL"],
          "STL": ["NHL|STL","MLB|STL"],
          "TB": ["NHL|TB","NFL|TB","MLB|TB"],
          "TEN": ["NFL|TEN"],
          "TEX": ["MLB|TEX"],
          "TOR": ["NHL|TOR","NBA|TOR","MLB|TOR"],
          "UTA": ["NBA|UTA"],
          "VAN": ["NHL|VAN"],
          "WAS": ["NHL|WAS","NBA|WAS","NFL|WAS","MLB|WAS"],
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

# leagues = "NHL", "MLB", "NBA"

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
    if city == "NHL" or city == "NBA" or city == "MLB":
        print("team: " + new[0])
        result_lookup.res_look(new[0], city, input_date)
    else:
        print("league: " + new[0] + " team: " + new[1])
        result_lookup.res_look(new[1], new[0], input_date)
    item = item+1




