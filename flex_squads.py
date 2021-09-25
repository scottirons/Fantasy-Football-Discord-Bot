from espn_api.football import League
import random
from datetime import date

league = League(league_id=41302936, year=2021, espn_s2='AEBZs%2F0JhLRPJvsLxD28BaBMEXt4wQELeh'\
                'O2P9NAnhL2Nz23A%2Blf%2Fdal7ftW7YcOr7YngIMBEHj1pd72KKtrW2G%2F2zGVo%2BKM0YtL1At'\
                'pcN2ZiLNyhIMeCr7BvYd056vhbRRX3nwd%2Fxq23R9w7bwyDhyIH5sMxVBOur690YldBTTCLJZjbHk'\
                'rUg0tA6kcD3wtCiP8CICrQmezMZBSpu6dad61FwoAIJSNo2NqexL5627uGt%2BXX9f9SFK6EcqNk2z7'\
                'F5%2BANM5Es9oNA8MI0Wz9a8Wt', swid='{F713A680-D381-43C3-93A6-80D38113C33C}')

nested_dict= {}
teams = []

# set target date at end of week 1, then use this to automatically tabulate the current week
season_start = date(2021, 9, 14)
today = date.today()
difference = today-season_start
days = (difference.days)
week = days//7 + 2


# now make list of startable flex players either in flex or on bench
box_scores = league.box_scores(week)
flex_squads = {}
# FIRST ADD AWAY TEAMS
for x in range(len(box_scores)):
    name_and_position = {}

    for y in range(len(box_scores[x].away_lineup)):
        if box_scores[x].away_lineup[y].position in ['RB', 'TE', 'WR']:
            name_and_position[box_scores[x].away_lineup[y].name] = box_scores[x].away_lineup[y].slot_position
    #print(len(name_and_position))
    eligible = []

    for player in name_and_position:
        if name_and_position[player] == 'BE':
            eligible.append(player)
        elif name_and_position[player] == 'RB/WR/TE':
            eligible.append(player)

    name = box_scores[x].away_team.team_id
    flex_squads[name] = eligible

# NOW ADD HOME TEAM
for x in range(len(box_scores)):
    name_and_position = {}

    for y in range(len(box_scores[x].home_lineup)):
        if box_scores[x].home_lineup[y].position in ['RB', 'TE', 'WR']:
            name_and_position[box_scores[x].home_lineup[y].name] = box_scores[x].home_lineup[y].slot_position
    # print(len(name_and_position))
    eligible = []

    for player in name_and_position:
        if name_and_position[player] == 'BE':
            eligible.append(player)
        elif name_and_position[player] == 'RB/WR/TE':
            eligible.append(player)

    name = box_scores[x].home_team.team_id
    flex_squads[name] = eligible

# print(flex_squads)

id_and_name = {1: 'Arvin', 2: 'Liam', 3: 'Brendan', 4: 'Ben', 5: 'Patrick', 6: 'Jrog',
               7: 'Scott', 8: 'Robert', 9: 'Nathaniel', 10: 'Jon', 11: 'Nick', 12: 'Jared'}
for number in range(1,13):
    flex_squads[id_and_name[number]] = flex_squads.pop(number)

def pick_flex(name):
    name = name.title()
    return('You should start ' + random.choice(flex_squads[name]) + '.')

print(pick_flex('scott'))
# print(flex_squads)

#print(random.choice(flex_squads['Scott']))

