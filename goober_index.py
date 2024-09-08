from collections import defaultdict
import heapq

id_and_name = {'Arvin': 1, 'Liam': 2, 'Cooper': 3, 'Patrick': 5, 'Brendan': 6, 'Sean': 8, 'Jon': 10, 'Scott': 11,
               'Kyle': 12, 'Phoenix': 13, 'Nick': 14, 'David': 15}
our_names = ['Arvin', 'Liam', 'Cooper', 'Patrick', 'Sean', 'David', 'Jon', 'Scott', 'Kyle', 'Phoenix', 'Nick',
            'Brendan']


def get_team(name, league):
    teams = league.teams
    # for team in teams:
    #     print(str(team.team_id) + " is " + team.team_name)
    name = name.title()
    for team in teams:
        if team.team_id == id_and_name[name]:
            return team


# use get_team function and then pass the team into this function
def get_gameday_roster(team, week, league):
    """gets the correct team within box_score class"""
    box_scores = league.box_scores(week)
    for i in range(len(box_scores)):
        if box_scores[i].away_team == team:
            current_roster = box_scores[i].away_lineup
            current_points = box_scores[i].away_score
            return current_roster, current_points
        elif box_scores[i].home_team == team:
            current_roster = box_scores[i].home_lineup
            current_points = box_scores[i].home_score
            return current_roster, current_points


def max_points(name, week, league):
    team = get_team(name, league)
    roster = get_gameday_roster(team, week, league)[0]
    points = round(get_gameday_roster(team, week, league)[1], 2)
    max_score_dict = {'QB': 0, 'RB1': 0, 'RB2': 0, 'WR1': 0, 'WR2': 0, 'FLEX': 0, 'TE': 0, 'K': 0, 'DEF': 0}
    positions = defaultdict(list)

    for player in roster:
        positions[player.position].append(-player.points)

    for position in positions:
        heapq.heapify(positions[position])

    max_score_dict['QB'] = -heapq.heappop(positions['QB'])
    max_score_dict['RB1'] = -heapq.heappop(positions['RB'])
    max_score_dict['RB2'] = -heapq.heappop(positions['RB'])
    max_score_dict['WR1'] = -heapq.heappop(positions['WR'])
    max_score_dict['WR2'] = -heapq.heappop(positions['WR'])
    max_score_dict['TE'] = -heapq.heappop(positions['TE'])
    max_score_dict['K'] = -heapq.heappop(positions['K'])
    max_score_dict['DEF'] = -heapq.heappop(positions['D/ST'])
    if positions['WR']:
        max_score_dict['FLEX'] = max(max_score_dict['FLEX'], -heapq.heappop(positions['WR']))
    if positions['RB']:
        max_score_dict['FLEX'] = max(max_score_dict['FLEX'], -heapq.heappop(positions['RB']))
    if positions['TE']:
        max_score_dict['FLEX'] = max(max_score_dict['FLEX'], -heapq.heappop(positions['TE']))

    max_score = round((sum(max_score_dict.values())), 2)
    difference = round((max_score - points), 2)
    return points, max_score, difference


def print_goober_index(week, points, max_score, difference):
    return "In week " + str(week) + " you scored " + str(points) + " points.\n" \
                                                                   "You could have scored " + str(
        max_score) + " points.\n" \
                     "You left " + str(difference) + " points on the table you goober!"


def full_goob(league, current_week):
    full_goob_dict = defaultdict(dict)
    for week in range(1, current_week):
        for name in our_names:
            full_goob_dict[week][name] = max_points(name, week, league)
    

    return full_goob_dict


def goober_report(week, full_goob_dict):
    goob_scores = full_goob_dict[week]
    max_player = None
    max_score = 0
    min_player = None
    min_score = 500

    for player in goob_scores:
        if goob_scores[player][2] > max_score:
            max_score = goob_scores[player][2]
            max_player = player
        elif goob_scores[player][2] < min_score:
            min_score = goob_scores[player][2]
            min_player = player

    result = (
        f"This week's biggest goober was {max_player}, who only scored {goob_scores[max_player][0]} points, "
        f"but could have scored {goob_scores[max_player][1]} points, resulting in a goober index of {max_score} points."
        f"\nThis week's most precise lineup picker was {min_player}, who scored {goob_scores[min_player][0]} points, "
        f"and could have scored a max of {goob_scores[min_player][1]} points, resulting in a goober index of "
        f"{min_score} points. Noice *smack*."
    )

    return result
