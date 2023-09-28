# gonna do some stuff with stats in this file

from datetime import date


# find current week so it'll pull the right stats
def make_points_dict(league):
    season_start = date(2023, 9, 7)
    today = date.today()
    difference = today - season_start
    days = difference.days
    week = days // 7 + 2

    nested_dict = {}
    teams = []

    # add team names to dictionary

    for team in league.teams:
        teams.append(team.team_name)

    # add players, then add stats

    for team in league.teams:
        nested_dict.setdefault(team.team_name, [])

        players = team.roster

        total_points = []
        for player in players:
            total_points = player.total_points
            total_points += total_points

            names = {}

        for player in players:
            names.setdefault((player.name.lower().translate({ord(i): None for i in '.'})), []).append(
                player.total_points)
        nested_dict.setdefault(team.team_name, []).append(names)
    return nested_dict


def average_points(name, league):
    name = name.lower()
    dict = make_points_dict(league)

    first_tuesday = date(2023, 9, 12)
    today = date.today()
    difference = today - first_tuesday
    days = difference.days
    week = days // 7 + 1

    counter = 1
    average_points = []
    for player in dict:
        try:
            average_points = (((dict[player][0][name]).pop()) / week)
            return '' + name.title() + " averages " + str(round(average_points, 2)) + " points."
        except:
            counter += 1
    if not average_points:
        return ('Sorry, either the name is spelled incorrectly or the player does not exist or the player is not on ' +
                'a current roster.')

