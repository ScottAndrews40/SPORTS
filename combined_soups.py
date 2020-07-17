# File containings all soups which are used to scrape necessary players/teams/
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

# BeautifulSoup setup for scraping of defenses and their stats
DEF_URL = 'https://www.fantasypros.com/nfl/rankings/dst-cheatsheets.php'
DEF_HTML = req.get(DEF_URL)
DEF_SOUP = BeautifulSoup(DEF_HTML.content, 'html.parser')
DEF_RANK_WINDOW = DEF_SOUP.find(id="rank-data")
DEF_DATA = DEF_RANK_WINDOW.find_all('tr')
# DEF_LIST = []

# Header List for first entry in defense/kicker/tight end lists
HEADER_LIST = ["Rank", "First Name", "Last Name", "Team", "BYE", "BEST",
               "WORST", "AVG", "STP DEV", "ADP", "VS. ADP"]


# Base function for scraping
def scrape_position(pos_data) -> list:
    position_list = [HEADER_LIST]

    for players in pos_data:
        if players.has_attr('data-id'):
            position_list.append(players.text.split())

    for elem in position_list:
        if (elem[2]) != 'Last Name':
            del elem[2]

    return position_list


QB_LIST = scrape_position(QB_DATA)
RB_LIST = scrape_position(RB_DATA)
WR_LIST = scrape_position(WR_DATA)
K_LIST = scrape_position(K_DATA)
TE_LIST = scrape_position(TE_DATA)
D_LIST = scrape_position(DEF_DATA)

if __name__ == '__main__':
    QB_LIST = scrape_position(QB_DATA)
    RB_LIST = scrape_position(RB_DATA)
    WR_LIST = scrape_position(WR_DATA)
    K_LIST = scrape_position(K_DATA)
    TE_LIST = scrape_position(TE_DATA)
    D_LIST = scrape_position(DEF_DATA)
    print(QB_LIST)
    print(RB_LIST)
    print(WR_LIST)
    print(K_LIST)
    print(TE_LIST)
    print(D_LIST)
