from espn_api.football import League


league = League(league_id=41302936, year=2022, espn_s2='AEBZs%2F0JhLRPJvsLxD28BaBMEXt4wQELeh'\
                    'O2P9NAnhL2Nz23A%2Blf%2Fdal7ftW7YcOr7YngIMBEHj1pd72KKtrW2G%2F2zGVo%2BKM0YtL1At'\
                    'pcN2ZiLNyhIMeCr7BvYd056vhbRRX3nwd%2Fxq23R9w7bwyDhyIH5sMxVBOur690YldBTTCLJZjbHk'\
                    'rUg0tA6kcD3wtCiP8CICrQmezMZBSpu6dad61FwoAIJSNo2NqexL5627uGt%2BXX9f9SFK6EcqNk2z7'\
                    'F5%2BANM5Es9oNA8MI0Wz9a8Wt', swid='{F713A680-D381-43C3-93A6-80D38113C33C}')

teams = league.teams


id_and_name = {1: 'Arvin', 2: 'Liam', 3: 'Brendan', 4: 'Ben', 5: 'Patrick', 6: 'Jrog',
                   13: 'Ethan', 8: 'Robert', 9: 'Nathaniel', 10: 'Jon', 11: 'Nick', 12: 'Jared'}
def get_key(val):
    for key, value in id_and_name.items():
        if val == value:
            return key
        else:
            continue

def get_team(name):
    name = name.title()
    id = get_key(name)
    for team in teams:
        if team.team_id == id:
            return team
        else:
            continue

# use get_team function and then pass the team into this function
def get_gameday_roster(team, week):
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

# def replace_value(dictionary,position,location, name, week):
#     team = get_team(name)
#     roster = get_gameday_roster(team, week)[0]
#     for player in roster:
#         if player.position == position:
#             if player.points > dictionary[location]:
#                 dictionary[location] = player.points

def max_points(name, week):
    team = get_team(name)
    roster = get_gameday_roster(team, week)[0]
    points = round(get_gameday_roster(team, week)[1], 2)
    max_score_dict = {'QB': 0, 'RB1': 0, 'RB2': 0, 'WR1': 0, 'WR2': 0, 'FLEX': 0, 'TE': 0, 'K': 0, 'DEF': 0}
    not_again = set()
    for player in roster:
        if player.position == 'QB':
            if player.points > max_score_dict['QB']:
                max_score_dict['QB'] = player.points
        elif player.position == 'K':
            if player.points > max_score_dict['K']:
                max_score_dict['K'] = player.points
        elif player.position == 'D/ST':
            if player.points > max_score_dict['DEF']:
                max_score_dict['DEF'] = player.points
        elif player.position == 'TE':
            if player.points > max_score_dict['TE']:
                max_score_dict['TE'] = player.points
                not_again.add(player.name)
        elif player.position == 'RB':
            if player.points > max_score_dict['RB1']:
                max_score_dict['RB1'] = player.points
                not_again.add(player.name)
        elif player.position == 'WR':
            if player.points > max_score_dict['WR1']:
                max_score_dict['WR1'] = player.points
                not_again.add(player.name)

    for player in roster:
        if player.name in not_again:
            continue
        elif player.position == 'RB':
            if player.points > max_score_dict['RB2']:
                max_score_dict['RB2'] = player.points
                not_again.add(player.name)
        if player.position == 'WR':
            if player.name not in not_again:
                if player.points > max_score_dict['WR2']:
                    max_score_dict['WR2'] = player.points
                    not_again.add(player.name)

    for player in roster:
        if player.position in ['WR', 'TE', 'RB']:
            if player.name not in not_again:
                if player.points > max_score_dict['FLEX']:
                    max_score_dict['FLEX'] = player.points
    max_score = round((sum(max_score_dict.values())), 2)
    difference = round((max_score - points), 2)
    return "In week " + str(week) + " you scored " + str(points) + " points.\n"\
            "You could have scored " + str(max_score) + " points.\n"\
            "You left " + str(difference) + " points on the table you goober!"


if __name__ == "__main__":
    print(max_points('jon', 1))