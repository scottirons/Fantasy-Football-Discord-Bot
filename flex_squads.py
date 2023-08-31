import random
from datetime import date


def make_position_dict(league):

    # set target date at end of week 1, then use this to automatically tabulate the current week
    season_start = date(2023, 9, 7)
    today = date.today()
    difference = today-season_start
    days = difference.days
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
        print(name_and_position)
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

    id_and_name = {1: 'Arvin', 2: 'Liam', 3: 'Cooper', 4: 'Patrick', 5: 'Smith', 6: 'Robert',
                   7: 'Jon', 8: 'Scott', 9: 'Kyle', 10: 'Phoenix', 11: 'Alex', 12: 'Baker'}
    for number in range(1, 13):
        flex_squads[id_and_name[number]] = flex_squads.pop(number)
    return flex_squads


def pick_flex(name, league):
    flex_squads = make_position_dict(league)
    name = name.title()
    return 'You should start ' + random.choice(flex_squads[name]) + '.'

# print(pick_flex('scott'))
# print(flex_squads)



