### This code provides information about the statistics of yesterday's NBA leaders.

from bs4 import BeautifulSoup
import requests
from pprint import pprint

nba_website = "https://www.nba.com/stats"

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36","Accept-Language": "en-US,en;q=0.9"}

response = requests.get(url=nba_website, headers=header)

nbaplayers_webpage_text = response.text
soup = BeautifulSoup(nbaplayers_webpage_text, "html.parser")

stats_names = soup.find_all("h2", class_="LeaderBoardCard_lbcTitle___WI9J")

stat_list = []
point_list = []

for stats in stats_names:
    stat_list.append(stats.text)

points = soup.find_all("a", class_="Anchor_anchor__cSc3P LeaderBoardPlayerCard_lbpcTableLink__MDNgL")

for point in points:
    point_list.append(point.text)

first_90_players_points = point_list[:90]

chunk_size = len(first_90_players_points) // len(stat_list[:9])  # Assuming the data is evenly distributed per stat

players_stats = {}
for i, term in enumerate(stat_list[:9]):
    print(i)
    print(term)
    start = i * chunk_size
    end = (i + 1) * chunk_size
    stats = first_90_players_points[start:end]
    players_stats[term] = [(stats[j], stats[j + 1]) for j in range(0, len(stats), 2)]

pprint(players_stats)