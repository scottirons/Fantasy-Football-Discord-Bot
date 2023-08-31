from espn_api.football import League, Player

league = League(league_id=41302936, year=2022, espn_s2='AEBZs%2F0JhLRPJvsLxD28BaBMEXt4wQELeh'\
                'O2P9NAnhL2Nz23A%2Blf%2Fdal7ftW7YcOr7YngIMBEHj1pd72KKtrW2G%2F2zGVo%2BKM0YtL1At'\
                'pcN2ZiLNyhIMeCr7BvYd056vhbRRX3nwd%2Fxq23R9w7bwyDhyIH5sMxVBOur690YldBTTCLJZjbHk'\
                'rUg0tA6kcD3wtCiP8CICrQmezMZBSpu6dad61FwoAIJSNo2NqexL5627uGt%2BXX9f9SFK6EcqNk2z7'\
                'F5%2BANM5Es9oNA8MI0Wz9a8Wt', swid='{F713A680-D381-43C3-93A6-80D38113C33C}')

def injured_dict():
    global nested_dict
    nested_dict= {}
    teams = []
    for team in league.teams:
        teams.append(team.team_name)

    for team in league.teams:
        nested_dict.setdefault(team.team_name, [])

        players = team.roster

        names = []
        for player in players:
            name = player.name
            names.append(name)

            pos_name = {}

        for player in players:
            pos_name.setdefault(player.injuryStatus, []).append(player.name)
        nested_dict.setdefault(team.team_name, []).append(pos_name)
    ournames = ['Arvin', 'Liam', 'Cooper', 'Patrick', 'Smith', 'Robert', 'Jon', 'Scott', 'Kyle', 'Phoenix', 'Alex',
                'Baker']
    positions = ['QB', 'WR', 'RB', 'TE', 'D/ST', 'K', 'FLEX']
    nested_dict = dict(zip(ournames, list(nested_dict.values())))

    return nested_dict

