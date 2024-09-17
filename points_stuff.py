
from datetime import date

id_and_name = {'Arvin': 1, 'Liam': 2, 'Cooper': 3, 'Patrick': 5, 'Brendan': 6, 'Sean': 8, 'Jon': 10, 'Scott': 11,
               'Kyle': 12, 'Phoenix': 13, 'Nick': 14, 'David': 15}
ournames = ['Arvin', 'Liam', 'Cooper', 'Patrick', 'Brendan', 'Sean', 'Jon', 'Scott', 'Kyle', 'Phoenix', 'Nick',
            'David']


# print(teams[0])

def points(player, league, week):
    teams = league.teams

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
