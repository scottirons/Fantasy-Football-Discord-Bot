import random
from datetime import date

id_and_name = {'Arvin': 1, 'Liam': 2, 'Cooper': 3, 'Patrick': 5, 'Smith': 6, 'Robert': 8, 'Jon': 10, 'Scott': 11,
               'Kyle': 12, 'Phoenix': 13, 'Nick': 14, 'Baker': 15}


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
            if box_scores[x].away_lineup[y].position in {'RB', 'TE', 'WR'}:
                name_and_position[box_scores[x].away_lineup[y].name] = box_scores[x].away_lineup[y].slot_position
        # print(name_and_position)
        eligible = []

        for player in name_and_position:
            if name_and_position[player] in {'BE', 'RB/WR/TE'}:
                eligible.append(player)

        team_id = box_scores[x].away_team.team_id
        flex_squads[team_id] = eligible

    # NOW ADD HOME TEAM
    for x in range(len(box_scores)):
        name_and_position = {}

        for y in range(len(box_scores[x].home_lineup)):
            if box_scores[x].home_lineup[y].position in {'RB', 'TE', 'WR'}:
                name_and_position[box_scores[x].home_lineup[y].name] = box_scores[x].home_lineup[y].slot_position
        # print(len(name_and_position))
        eligible = []

        for player in name_and_position:
            if name_and_position[player] in {'BE', 'RB/WR/TE'}:
                eligible.append(player)

        team_id = box_scores[x].home_team.team_id
        flex_squads[team_id] = eligible

    # print(flex_squads)
    return flex_squads


def pick_flex(name, flexable_players):
    name = name.title()
    return 'You should start ' + random.choice(flexable_players[id_and_name[name]]) + '.'

# print(pick_flex('scott'))
# print(flex_squads)



