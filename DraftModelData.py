import requests as req
from bs4 import BeautifulSoup
from pprint import pprint

URL = "https://www.fantasypros.com/nfl/rankings/consensus-cheatsheets.php"
overAllPlayerList = req.get(URL)
FanSoup = BeautifulSoup(overAllPlayerList.content, 'html.parser')
#print(FanSoup)

players = FanSoup.find(id='rank-data')
#pprint(players)
#playerRanks = players.find_all('td', class_="sticky-cell sticky-cell-one")
playerNames = players.find_all('span', class_="full-name")

#PlayerData doesn't work
#playerData = players.find_all('a', class_='fp-icon__link')
#pprint(playerData)

#for rank in playerRanks:
    #print(rank.text)

#rank_name_dict = {playerRanks[i].text: playerNames[i].text for i in range(len(playerNames))}
#print(rank_name_dict)

#for name in playerNames:
#    print(name.text)

#reOrg code and create functions for player position lists

#Quarter Backs
QB_URL = 'https://www.fantasypros.com/nfl/rankings/qb-cheatsheets.php'
QB_HTML = req.get(QB_URL)
QB_Soup = BeautifulSoup(QB_HTML.content, 'html.parser')

#Running Backs
RB_URL = 'https://www.fantasypros.com/nfl/rankings/half-point-ppr-rb-cheatsheets.php'
RB_HTML = req.get(RB_URL)
RB_Soup = BeautifulSoup(RB_HTML.content, 'html.parser')

#Wide Receivers
WR_URL = 'https://www.fantasypros.com/nfl/rankings/half-point-ppr-wr-cheatsheets.php'
WR_HTML = req.get(WR_URL)
WR_Soup = BeautifulSoup(WR_HTML.content, 'html.parser')

#Defense
DEF_URL = 'https://www.fantasypros.com/nfl/rankings/dst-cheatsheets.php'
DEF_HTML = req.get(DEF_URL)
DEF_Soup = BeautifulSoup(DEF_HTML.content, 'html.parser')

#Kicker
K_URL = 'https://www.fantasypros.com/nfl/rankings/k-cheatsheets.php'
K_HTML = req.get(K_URL)
K_Soup = BeautifulSoup(K_HTML.content, 'html.parser')

#Tight End
TE_URL = 'https://www.fantasypros.com/nfl/rankings/half-point-ppr-te-cheatsheets.php'
TE_HTML = req.get(TE_URL)
TE_Soup = BeautifulSoup(TE_HTML.content, 'html.parser')


def GetRB():
    return 0
def getWR():
    return 0
def getDefense():
    return 0
def getKicker():
    return 0
def getTE():
    return 0
def getQB():
    return 0