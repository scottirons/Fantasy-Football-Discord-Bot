from espn_api.football import League
import random
from datetime import date


league = League(league_id=41302936, year=2021, espn_s2='AEBZs%2F0JhLRPJvsLxD28BaBMEXt4wQELeh'\
                'O2P9NAnhL2Nz23A%2Blf%2Fdal7ftW7YcOr7YngIMBEHj1pd72KKtrW2G%2F2zGVo%2BKM0YtL1At'\
                'pcN2ZiLNyhIMeCr7BvYd056vhbRRX3nwd%2Fxq23R9w7bwyDhyIH5sMxVBOur690YldBTTCLJZjbHk'\
                'rUg0tA6kcD3wtCiP8CICrQmezMZBSpu6dad61FwoAIJSNo2NqexL5627uGt%2BXX9f9SFK6EcqNk2z7'\
                'F5%2BANM5Es9oNA8MI0Wz9a8Wt', swid='{F713A680-D381-43C3-93A6-80D38113C33C}')

teams = league.teams
ournames = ['Arvin', 'Liam', 'Brendan', 'Ben', 'Patrick', 'Jrog', 'Scott', 'Robert', 'Nathaniel', 'Jon', 'Nick', 'Jared']
#print(teams[0])

def points(player):
    season_start = date(2021, 9, 14)
    today = date.today()
    difference = today - season_start
    days = (difference.days)
    week = days // 7 + 1

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
    average_against = points_against/week
    average_against = round(average_against, 2)
    listie.append('Average against: ' + str(average_against))
    differential = total_points - points_against
    differential = round(differential, 2)
    listie.append('Point differential: ' + str(differential))
    return('\n'.join(listie))



if __name__ == "__main__":
    print(points('Scott'))