from espn_api.football import League, BoxPlayer, Player
import random

league = League(league_id=41302936, year=2021, espn_s2='AEBZs%2F0JhLRPJvsLxD28BaBMEXt4wQELeh'\
                'O2P9NAnhL2Nz23A%2Blf%2Fdal7ftW7YcOr7YngIMBEHj1pd72KKtrW2G%2F2zGVo%2BKM0YtL1At'\
                'pcN2ZiLNyhIMeCr7BvYd056vhbRRX3nwd%2Fxq23R9w7bwyDhyIH5sMxVBOur690YldBTTCLJZjbHk'\
                'rUg0tA6kcD3wtCiP8CICrQmezMZBSpu6dad61FwoAIJSNo2NqexL5627uGt%2BXX9f9SFK6EcqNk2z7'\
                'F5%2BANM5Es9oNA8MI0Wz9a8Wt', swid='{F713A680-D381-43C3-93A6-80D38113C33C}')


nested_dict= {}
teams = []

for team in league.teams:
    teams.append(team.team_name)
#print(teams)

for team in league.teams:
    nested_dict.setdefault(team.team_name, [])

    players = team.roster

    names = []
    for player in players:
        name = player.name
        names.append(name)

        current_position = {}

    for player in players:
        current_position.setdefault(player.slot_position,[]).append(player.name)
    nested_dict.setdefault(team.team_name, []).append(current_position)

ournames = ['Arvin', 'Liam', 'Brendan', 'Ben', 'Patrick', 'Jrog', 'Scott', 'Robert', 'Nathaniel', 'Jon', 'Nick', 'Jared']
positions = ['QB', 'WR', 'RB', 'TE', 'D/ST', 'K', 'FLEX']
nested_dict = dict(zip(ournames, list(nested_dict.values())))
# print(teams)
# print(nested_dict['Scott'])
#print(nested_dict)


