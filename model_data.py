# File containing all soups which are used to scrape necessary players/teams/
# stats from fantasypros.com. File will be merged with projModel file once
# completed.

import requests as req
from bs4 import BeautifulSoup

# Quarter Backs
QB_URL = 'https://www.fantasypros.com/nfl/rankings/qb-cheatsheets.php'
QB_HTML = req.get(QB_URL)
QB_SOUP = BeautifulSoup(QB_HTML.content, 'html.parser')
QB_RANK_WINDOW = QB_SOUP.find(id='rank-data')
QB_DATA = QB_RANK_WINDOW.find_all('tr')
# QB_LIST = []

# BeautifulSoup setup for scraping of running backs and their stats
RB_URL = 'https://www.fantasypros.com/nfl/rankings/half-point-ppr-rb-cheatsheets.php'
RB_HTML = req.get(RB_URL)
RB_SOUP = BeautifulSoup(RB_HTML.content, 'html.parser')
RB_RANK_WINDOW = RB_SOUP.find(id='rank-data')
RB_DATA = RB_RANK_WINDOW.find_all('tr')
# RB_LIST = []

# BeautifulSoup setup for scraping of wide receivers and their stats
WR_URL = 'https://www.fantasypros.com/nfl/rankings/half-point-ppr-wr-cheatsheets.php'
WR_HTML = req.get(WR_URL)
WR_SOUP = BeautifulSoup(WR_HTML.content, 'html.parser')
WR_RANK_WINDOW = WR_SOUP.find(id='rank-data')
WR_DATA = WR_RANK_WINDOW.find_all('tr')
# WR_LIST = []

# BeautifulSoup setup for scraping of kickers and their stats
K_URL = 'https://www.fantasypros.com/nfl/rankings/k-cheatsheets.php'
K_HTML = req.get(K_URL)
K_SOUP = BeautifulSoup(K_HTML.content, 'html.parser')
K_RANK_WINDOW = K_SOUP.find(id="rank-data")
K_DATA = K_RANK_WINDOW.find_all('tr')
# K_LIST = []

# BeautifulSoup setup for scraping of tight ends and their stats
TE_URL = 'https://www.fantasypros.com/nfl/rankings/half-point-ppr-te-cheatsheets.php'
TE_HTML = req.get(TE_URL)
TE_SOUP = BeautifulSoup(TE_HTML.content, 'html.parser')
TE_RANK_WINDOW = TE_SOUP.find(id="rank-data")
TE_DATA = TE_RANK_WINDOW.find_all('tr')
# TE_LIST = []

#  DEFENSE REQUIRED A DIFFERENT APPROACH TO GET A CLEAN LOOKING LIST ###
# BeautifulSoup setup for scraping of defenses and their stats
DEF_URL = 'https://www.fantasypros.com/nfl/rankings/dst-cheatsheets.php'
DEF_HTML = req.get(DEF_URL)
DEF_SOUP = BeautifulSoup(DEF_HTML.content, 'html.parser')
DEF_RANK_WINDOW = DEF_SOUP.find(id="rank-data")
# DEF_DATA = DEF_RANK_WINDOW.find_all('tr') OLD APPROACH

DEF_DATA = DEF_RANK_WINDOW.find_all('tr',
                                    attrs={'data-id': ['8270', '8240', '8020', '8030', '8180', '8190', '8050', '8150',
                                                       '8170', '8280', '8230', '8090', '8250', '8130', '8290', '8300',
                                                       '8260', '8080', '8110', '8070', '8210', '8120', '8310', '8140',
                                                       '8100', '8010', '8000', '8040', '8160', '8220', '8060', '8200']})
Names = []
# print(DEF_DATA)
# creates list of full name of team's state with shorthand in parenthesis
for names in DEF_DATA:
    Names.append(names.find(class_="full-name").text)

# pprint.pprint(Names)
# creates list of Defense data bYe, points avg etc
# Standardized header to sqlite3 column index convention 8/27
DEF_HEADER = ["Rank", "State_Name", "Bye", "Best",
              "Worst", "Avg", "Stp_Dev", "Adp", "Vs.Adp"]
D_LIST = [DEF_HEADER]
for Dplayers in DEF_DATA:
    D_LIST.append(Dplayers.text.split())

# pprint.pprint(DEF_LIST)
# replaces short name with full name of state and deletes irrelevant elements taken from .append(Dplayers.text.split())
i = 0
for Dplayers in D_LIST[1:]:
    Dplayers[1] = Names[i]
    i += 1
    if len(Dplayers) == 12:
        del Dplayers[2:5]
    if len(Dplayers) == 11:
        del Dplayers[2:4]

# pprint.pprint(DEF_LIST)

# Header List for first entry in qb/rb/wr/kicker/tight end lists
# 8/26 Altered First Name, Last Name, STP DEV and VS. ADP so that sql doesn't throw user warning
# over column index naming convention
# Standardized header to sqlite3 column index convention 8/27
HEADER_LIST = ["Rank", "FirstName", "LastName", "Team", "Bye", "Best",
               "Worst", "Avg", "Stp_Dev", "Adp", "Vs.Adp"]


# Base function for scraping
def scrape_position(pos_data) -> list:
    position_list = [HEADER_LIST]

    for players in pos_data:
        if players.has_attr('data-id'):
            position_list.append(players.text.split())

    # This is for deleting short name and Name suffix ie Jr, II
    # This only applies to players in positions NOT DEFENSE
    for elem in position_list[1:]:
        if len(elem) == 13:
            del elem[2:4]
        else:
            del elem[2]
        if '.' in elem[2]:
            del elem[2]

    return position_list


# These are needed for DratData Controller

QB_LIST = scrape_position(QB_DATA)
RB_LIST = scrape_position(RB_DATA)
WR_LIST = scrape_position(WR_DATA)
K_LIST = scrape_position(K_DATA)
TE_LIST = scrape_position(TE_DATA)
# D_LIST = scrape_position(DEF_DATA)

if __name__ == '__main__':
    print(QB_LIST)
    print(RB_LIST)
    print(WR_LIST)
    print(K_LIST)
    print(TE_LIST)
    print(D_LIST)
