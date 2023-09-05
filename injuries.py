def injured_dict(league):
    nested_dict = {}
    teams = []
    for team in league.teams:
        teams.append(team.team_name)

    for team in league.teams:
        nested_dict.setdefault(team.team_name, [])
        print(team.team_name)

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

