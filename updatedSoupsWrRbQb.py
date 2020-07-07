import requests as req
from bs4 import BeautifulSoup
from pprint import pprint

# URL = "https://www.fantasypros.com/nfl/rankings/consensus-cheatsheets.php"
# overAllPlayerList = req.get(URL)
# FanSoup = BeautifulSoup(overAllPlayerList.content, 'html.parser')
# print(FanSoup)

# players = FanSoup.find(id='rank-data')
# pprint(players)
# playerRanks = players.find_all('td', class_="sticky-cell sticky-cell-one")
# playerNames = players.find_all('span', class_="full-name")

# PlayerData doesn't work
# playerData = players.find_all('a', class_='fp-icon__link')
# pprint(playerData)

# for rank in playerRanks:
# print(rank.text)

# rank_name_dict = {playerRanks[i].text: playerNames[i].text for i in range(len(playerNames))}
# print(rank_name_dict)

# for name in playerNames:
#    print(name.text)

# reOrg code and create functions for player position lists


# Quarter Backs
QB_URL = 'https://www.fantasypros.com/nfl/rankings/qb-cheatsheets.php'
QB_HTML = req.get(QB_URL)
QB_Soup = BeautifulSoup(QB_HTML.content, 'html.parser')
QB_RankWindow = QB_Soup.find(id='rank-data')
QB_Data = QB_RankWindow.find_all('tr')
QB_List = []
# pprint(QB_Data)

# Running Backs
RB_URL = 'https://www.fantasypros.com/nfl/rankings/half-point-ppr-rb-cheatsheets.php'
RB_HTML = req.get(RB_URL)
RB_Soup = BeautifulSoup(RB_HTML.content, 'html.parser')
RB_RankWindow = RB_Soup.find(id='rank-data')
RB_Data = RB_RankWindow.find_all('tr')
RB_List = []
# pprint(RB_Data)

# Wide Receivers
WR_URL = 'https://www.fantasypros.com/nfl/rankings/half-point-ppr-wr-cheatsheets.php'
WR_HTML = req.get(WR_URL)
WR_Soup = BeautifulSoup(WR_HTML.content, 'html.parser')
WR_RankWindow = WR_Soup.find(id='rank-data')
WR_Data = WR_RankWindow.find_all('tr')
WR_List = []
# pprint(WR_Data)

HEADER_LIST = ["Rank", "First Name", "Last Name", "Team", "BYE", "BEST",
               "WORST", "AVG", "STP DEV", "ADP", "VS. ADP"]


def scrape_qb_data() -> list:
    QB_List.append(HEADER_LIST)

    for players in QB_Data:
        if players.has_attr('data-id'):
            QB_List.append(players.text.split())

    for elem in QB_List:
        if elem[2] != 'Last Name':
            del elem[2]

    return QB_List


def scrape_rb_data() -> list:
    RB_List.append(HEADER_LIST)

    for players in RB_Data:
        if players.has_attr('data-id'):
            RB_List.append(players.text.split())

    for elem in RB_List:
        if elem[2] != 'Last Name':
            del elem[2]

    return RB_List


def scrape_wr_data() -> list:
    WR_List.append(HEADER_LIST)

    for players in WR_Data:
        if players.has_attr('data-id'):
            WR_List.append(players.text.split())

    for elem in WR_List:
        if elem[2] != 'Last Name':
            del elem[2]

    return WR_List


## for i in scrape_qb_data():
##     print(i)
## print('\n'*3)
## for j in scrape_wr_data():
##     print(j)
## print('\n'*3)
for k in scrape_rb_data():
    print(k)

'''
# Defense
DEF_URL = 'https://www.fantasypros.com/nfl/rankings/dst-cheatsheets.php'
DEF_HTML = req.get(DEF_URL)
DEF_Soup = BeautifulSoup(DEF_HTML.content, 'html.parser')

# Kicker
K_URL = 'https://www.fantasypros.com/nfl/rankings/k-cheatsheets.php'
K_HTML = req.get(K_URL)
K_Soup = BeautifulSoup(K_HTML.content, 'html.parser')

# Tight End
TE_URL = 'https://www.fantasypros.com/nfl/rankings/half-point-ppr-te-cheatsheets.php'
TE_HTML = req.get(TE_URL)
TE_Soup = BeautifulSoup(TE_HTML.content, 'html.parser')
'''
