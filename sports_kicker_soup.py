import requests as req
from bs4 import BeautifulSoup

K_URL = 'https://www.fantasypros.com/nfl/rankings/k-cheatsheets.php'
K_HTML = req.get(K_URL)
K_Soup = BeautifulSoup(K_HTML.content, 'html.parser')
K_SOUP_TABLE = K_Soup.find(id = "rank-data")
K_SOUP_TABLE_ELEMS = K_SOUP_TABLE.find_all('tr')
kicker_list = []
kicker_names = []
name_class = "player-label sticky-cell sticky-cell-two"
kicker_info = []
kicker_list.append(["Rank", "BYE", "BEST", "WORST", "AVG", "STP DEV", "ADP",
                    "VS. ADP", ["Name", "Team"]])

for kicker in K_SOUP_TABLE_ELEMS:
    if (kicker.has_attr('data-id')):
        kicker_player = (kicker.text).split('\n')
        kicker_player.remove('')
        kicker_player.remove('')
        kicker_elem = kicker.find(class_ = name_class)
        kicker_name = kicker_elem.find(class_ = "full-name")
        kicker_team = kicker_elem.find(class_ = "grey")
        del kicker_player[1:2]
        kicker_player.append([kicker_name.text, kicker_team.text])
        kicker_list.append(kicker_player)

print(kicker_list)
