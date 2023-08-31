from datetime import date


#print(rankings[0][1].team_name)
def stonks(league):
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