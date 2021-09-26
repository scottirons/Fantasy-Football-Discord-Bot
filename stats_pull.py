# gonna do some stuff with stats in this file

from espn_api.football import League
import random
from datetime import date


league = League(league_id=41302936, year=2021, espn_s2='AEBZs%2F0JhLRPJvsLxD28BaBMEXt4wQELeh'\
                'O2P9NAnhL2Nz23A%2Blf%2Fdal7ftW7YcOr7YngIMBEHj1pd72KKtrW2G%2F2zGVo%2BKM0YtL1At'\
                'pcN2ZiLNyhIMeCr7BvYd056vhbRRX3nwd%2Fxq23R9w7bwyDhyIH5sMxVBOur690YldBTTCLJZjbHk'\
                'rUg0tA6kcD3wtCiP8CICrQmezMZBSpu6dad61FwoAIJSNo2NqexL5627uGt%2BXX9f9SFK6EcqNk2z7'\
                'F5%2BANM5Es9oNA8MI0Wz9a8Wt', swid='{F713A680-D381-43C3-93A6-80D38113C33C}')

#find current week so it'll pull the right stats
def make_points_dict():
    season_start = date(2021, 9, 14)
    today = date.today()
    difference = today-season_start
    days = (difference.days)
    week = days//7 + 2

    nested_dict= {}
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
            total_points += (total_points)

            names = {}

        for player in players:
            names.setdefault((player.name.lower().translate({ord(i): None for i in '.'})),[]).append(player.total_points)
        nested_dict.setdefault(team.team_name, []).append(names)
    return(nested_dict)




def average_points(name):
    name = name.lower()
    dict = make_points_dict()


    season_start = date(2021, 9, 14)
    today = date.today()
    difference = today - season_start
    days = (difference.days)
    week = days // 7 + 1

    counter = 1
    average_points = []
    for player in dict:
        try:
            average_points = (((dict[player][0][name]).pop())/week)
            return('' + name.title() + " averages " + str(average_points) + " points.")
        except:
            counter += 1
    if average_points == []:
        return('Sorry, either the name is spelled incorrectly or the player does not exist or the player is not on ' +
               'a current roster')

if __name__ == "__main__":
    print(average_points('derrick henry'))