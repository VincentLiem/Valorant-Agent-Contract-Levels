import requests
from bs4 import BeautifulSoup

exp_data = requests.get("https://valorant.fandom.com/wiki/Experience")
soup = BeautifulSoup(exp_data.content, "html.parser")

# EXP stats as of 2/17/22
# Excludes weekly missions
tier1 = 20000
tier2 = 30000 + tier1
tier3 = 40000 + tier2
tier4 = 50000 + tier3
tier5 = 60000 + tier4
tier6 = 75000 + tier5
tier7 = 100000 + tier6
tier8 = 150000 + tier7
tier9 = 200000 + tier8
tier10 = 250000 + tier9
spikerush = 1000
deathmatch = 900
escalation = 800
escalation_win = 200
snowball = 750
snowball_win = 150
normal_round = 100  # Competitive, Replication, Unrated
normal_round_win = 200  # Competitive, Replication, Unrated
dailymision = 2000

print("Current exp?")
current = int(input())
print("Normal match rounds played?")
normal_round_played = int(input())
print("Normal match rounds won?")
normal_win_played = int(input())
print("Spike Rush games played?")
spikerush_played = int(input())
print("Deathmatch games played?")
deathmatch_played = int(input())
print("Escalation games played?")
escalation_played = int(input())
print("Escalation games won?")
escalation_win_played = int(input())
print("Snowball games played?")
snowball_played = int(input())
print("Snowball games won?")
snowball_win_played = int(input())
print("Daily missions completed?")
dailymision_done = int(input())

total = (
    current
    + spikerush * spikerush_played
    + deathmatch * deathmatch_played
    + normal_round * normal_round_played
    + normal_round_win * normal_win_played
    + escalation * escalation_played
    + escalation_win * escalation_played
    + snowball * snowball_played
    + snowball_win * snowball_win_played
)
print("Total exp: " + str(total))
tier = 0
if total >= tier1:
    tier = 1
if total >= tier2:
    tier = 2
if total >= tier3:
    tier = 3
if total >= tier4:
    tier = 4
if total >= tier5:
    tier = 5
if total >= tier6:
    tier = 6
if total >= tier7:
    tier = 7
if total >= tier8:
    tier = 8
if total >= tier9:
    tier = 9
if total >= tier10:
    tier = 10
print("Reached tier " + str(tier))
