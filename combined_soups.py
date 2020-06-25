# File containings all soups which are used to scrape necessary players/teams/
# stats from fantasypros.com. File will be merged with projModel file once
# completed.

import requests as req
from bs4 import BeautifulSoup

# BeautifulSoup setup for scraping of kickers and their stats
K_URL = 'https://www.fantasypros.com/nfl/rankings/k-cheatsheets.php'
K_HTML = req.get(K_URL)
K_Soup = BeautifulSoup(K_HTML.content, 'html.parser')
K_SOUP_TABLE = K_Soup.find(id = "rank-data")
K_SOUP_TABLE_ELEMS = K_SOUP_TABLE.find_all('tr')
KICKER_LIST = []

# BeautifulSoup setup for scraping of tight ends and their stats
TE_URL = 'https://www.fantasypros.com/nfl/rankings/half-point-ppr-te-cheatsheets.php'
TE_HTML = req.get(TE_URL)
TE_Soup = BeautifulSoup(TE_HTML.content, 'html.parser')
TE_SOUP_TABLE = TE_Soup.find(id = "rank-data")
TE_SOUP_TABLE_ELEMS = TE_SOUP_TABLE.find_all('tr')
TIGHT_ENDS_LIST = []

# BeautifulSoup setup for scraping of defenses and their stats
DEF_URL = 'https://www.fantasypros.com/nfl/rankings/dst-cheatsheets.php'
DEF_HTML = req.get(DEF_URL)
DEF_Soup = BeautifulSoup(DEF_HTML.content, 'html.parser')
DEF_SOUP_TABLE = DEF_Soup.find(id = "rank-data")
DEF_SOUP_TABLE_ELEMS = DEF_SOUP_TABLE.find_all('tr')
DEFENSE_LIST = []

# Header List for first entry in defense/kicker/tight end lists
HEADER_LIST = ["Rank", "BYE", "BEST", "WORST", "AVG", "STP DEV", "ADP",
                    "VS. ADP", ["Name", "Team"]]

# Function which goes through html code provided by soup to make a sublist from
# stats and player name/team to append to KICKER_LIST. Returns KICKER_LIST, a
# list, which contains every entry from the corresponding website along with
# their relevant information.
def scrape_kickers() -> list:
    KICKER_LIST.append(HEADER_LIST)
    for kicker in K_SOUP_TABLE_ELEMS:
        if (kicker.has_attr('data-id')):
            kicker_stats = (kicker.text).split('\n') #Split text attribute from kicker into list
            kicker_stats.remove('') #Remove extra, empty strings in kicker_stats
            kicker_stats.remove('')
            del kicker_stats[1:2]   #Delete second entry b/c name/team are displayed together incorrectly
            
            kicker_elem = kicker.find(class_ = 'wsis') 
            kicker_stats.append([kicker_elem['data-name'],
                                 kicker_elem['data-team']]) #Find name/team of player and append them as a sublist to kicker_stats list
            KICKER_LIST.append(kicker_stats)
    return KICKER_LIST #Return list which contains all ranked kickers from the given url

# Function which goes through html code provided by soup to make a sublist from
# stats and player name/team to append to TIGHT_ENDS_LIST. Returns
# TIGHT_ENDS_LIST, a list, which contains every entry from the corresponding
#website along with their relevant information.
def scrape_tight_ends() -> list:
    TIGHT_ENDS_LIST.append(HEADER_LIST)
    for tight_end in TE_SOUP_TABLE_ELEMS:
        if (tight_end.has_attr('data-id')):
            tight_end_stats = (tight_end.text).split('\n')
            tight_end_stats.remove('')
            tight_end_stats.remove('')
            del tight_end_stats[1:2]
            
            tight_end_elem = tight_end.find(class_ = 'wsis')
            tight_end_stats.append([tight_end_elem['data-name'],
                                     tight_end_elem['data-team']])
            TIGHT_ENDS_LIST.append(tight_end_stats)
    return TIGHT_ENDS_LIST

# Function which goes through html code provided by soup to make a sublist from
# stats and the teams to append to DEFENSE_LIST. Returns DEFENSE_LIST, a list,
# which contains every entry from the corresponding website along with their
# relevant information.
def scrape_defense() -> list:
    DEFENSE_LIST.append(HEADER_LIST)
    for defense in DEF_SOUP_TABLE_ELEMS:
        if (defense.has_attr('data-id')):
            defense_stats = (defense.text).split('\n')
            defense_stats.remove('')
            defense_stats.remove('')
            del defense_stats[1:2]
            
            defense_elem = defense.find(class_ = 'wsis')
            defense_stats.append([defense_elem['data-name'],
                                 defense_elem['data-team']])
            DEFENSE_LIST.append(defense_stats)
    return DEFENSE_LIST

if __name__ == '__main__':
    print(scrape_kickers())
    print(scrape_tight_ends())
    print(scrape_defense())
