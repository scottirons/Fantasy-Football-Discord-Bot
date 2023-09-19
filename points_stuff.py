
from datetime import date

ournames = ['Arvin', 'Liam', 'Cooper', 'Patrick', 'Smith', 'Robert', 'Jon', 'Scott', 'Kyle', 'Phoenix', 'Nick',
            'Baker']


# print(teams[0])

def points(player, league):
    teams = league.teams
    season_start = date(2023, 9, 7)
    today = date.today()
    difference = today - season_start
    days = difference.days
    week = days // 7 + 1

    print("it's week " + str(week))

    player = player.title()
    numba = ournames.index(player)

    listie = []

    total_points = teams[numba].points_for
    total_points = round(total_points, 2)
    listie.append('Total points:' + ' ' + str(total_points))
    average_points = total_points / week
    average_points = round(average_points, 2)
    listie.append('Average scored: ' + str(average_points))
    points_against = teams[numba].points_against
    points_against = round(points_against, 2)
    listie.append('Points against: ' + str(points_against))
    average_against = points_against / week
    average_against = round(average_against, 2)
    listie.append('Average against: ' + str(average_against))
    differential = total_points - points_against
    differential = round(differential, 2)
    listie.append('Point differential: ' + str(differential))
    return '\n'.join(listie)
