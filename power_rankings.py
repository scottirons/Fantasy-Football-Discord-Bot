from espn_api.football import League
import random
from datetime import date


league = League(league_id=41302936, year=2021, espn_s2='AEBZs%2F0JhLRPJvsLxD28BaBMEXt4wQELeh'\
                'O2P9NAnhL2Nz23A%2Blf%2Fdal7ftW7YcOr7YngIMBEHj1pd72KKtrW2G%2F2zGVo%2BKM0YtL1At'\
                'pcN2ZiLNyhIMeCr7BvYd056vhbRRX3nwd%2Fxq23R9w7bwyDhyIH5sMxVBOur690YldBTTCLJZjbHk'\
                'rUg0tA6kcD3wtCiP8CICrQmezMZBSpu6dad61FwoAIJSNo2NqexL5627uGt%2BXX9f9SFK6EcqNk2z7'\
                'F5%2BANM5Es9oNA8MI0Wz9a8Wt', swid='{F713A680-D381-43C3-93A6-80D38113C33C}')

#print(rankings[0][1].team_name)
def stonks():
    '''prints power rankings of all teams'''
    season_start = date(2021, 9, 14)
    today = date.today()
    difference = today - season_start
    days = (difference.days)
    week = days // 7 + 2

    rankings = league.power_rankings(week=week)

    stringie = "This week's power rankings:"
    rankings_list = []
    for i in range(12):
        rankings_list.append(rankings[i][1].team_name + ": " + rankings[i][0])
    return(stringie + '\n' + '\n'.join(rankings_list))
    #return(rankings_list)

if __name__ == "__main__":
    print(stonks())