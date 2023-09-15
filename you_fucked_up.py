from collections import defaultdict
import heapq

id_and_name = {1: 'Arvin', 2: 'Liam', 3: 'Cooper', 4: 'Patrick', 5: 'Smith', 6: 'Robert',
                   7: 'Jon', 8: 'Scott', 9: 'Kyle', 10: 'Phoenix', 11: 'Nick', 12: 'Baker'}

def get_key(val):
    for key, value in id_and_name.items():
        if val == value:
            return key


def get_team(name, league):
    teams = league.teams
    for team in teams:
        print(team.team_id + team.team_name)
    name = name.title()
    id = get_key(name)
    for team in teams:
        if team.team_id == id:
            return team

# use get_team function and then pass the team into this function
def get_gameday_roster(team, week, league):
    '''gets the correct team within box_score class'''
    box_scores = league.box_scores(week)
    current_roster, current_points = None, None
    for i in range(len(box_scores)):
        if box_scores[i].away_team == team:
            current_roster = box_scores[i].away_lineup
            current_points = box_scores[i].away_score
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
    return "In week " + str(week) + " you scored " + str(points) + " points.\n"\
            "You could have scored " + str(max_score) + " points.\n"\
            "You left " + str(difference) + " points on the table you goober!"


if __name__ == "__main__":
    print(max_points('jon', 3))