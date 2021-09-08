from espn_api.football import League
import random

league = League(league_id=41302936, year=2021, espn_s2='AEBZs%2F0JhLRPJvsLxD28BaBMEXt4wQELeh'\
                'O2P9NAnhL2Nz23A%2Blf%2Fdal7ftW7YcOr7YngIMBEHj1pd72KKtrW2G%2F2zGVo%2BKM0YtL1At'\
                'pcN2ZiLNyhIMeCr7BvYd056vhbRRX3nwd%2Fxq23R9w7bwyDhyIH5sMxVBOur690YldBTTCLJZjbHk'\
                'rUg0tA6kcD3wtCiP8CICrQmezMZBSpu6dad61FwoAIJSNo2NqexL5627uGt%2BXX9f9SFK6EcqNk2z7'\
                'F5%2BANM5Es9oNA8MI0Wz9a8Wt', swid='{F713A680-D381-43C3-93A6-80D38113C33C}')

#print(league.teams)
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

        pos_name = {}

    for player in players:
        pos_name.setdefault(player.position,[]).append(player.name)
    nested_dict.setdefault(team.team_name, []).append(pos_name)

ournames = ['Arvin', 'Liam', 'Brendan', 'Ben', 'Patrick', 'Jrog', 'Scott', 'Robert', 'Nathaniel', 'Jon', 'Nick', 'Jared']
positions = ['QB', 'WR', 'RB', 'TE', 'D/ST', 'K', 'FLEX']
nested_dict = dict(zip(ournames, list(nested_dict.values())))

#print(nested_dict)


def who_start(playername, whatpos):
    if 'mom' in playername:
        return('bruh')
    if 'doggy' in whatpos:
        return('bruh')
    if playername.capitalize() not in nested_dict:
        return('name does not exist')
    playername = playername.capitalize()
    if whatpos.lower() in ('defense', 'def', 'd'):
        whatpos = 'd/st'
    if whatpos.lower() in ('running back', 'running'):
        whatpos = 'rb'
    if whatpos.lower() in ('quarter back', 'quarterback', 'qb'):
        whatpos = 'qb'
    if whatpos.lower() in ('wide receiver'):
        whatpos = 'wr'   
    elif 'quarter' in whatpos.lower():
        whatpos = 'qb'
    elif whatpos.lower() == 'kicker':
        whatpos = 'k'
    if whatpos.upper() not in positions:
        return('position does not exist')    
    if whatpos in ('k', 'te', 'qb', 'd/st'):
        return('You should start '+ random.choice(nested_dict[playername][0][whatpos.upper()]) + '.')
    elif whatpos == 'flex':
        newpos = random.choice(['wr', 'rb'])
        return('You should start ' + random.choice(nested_dict[playername][0][newpos.upper()]) + '.')
    else:
        choice1 = random.choice(nested_dict[playername][0][whatpos.upper()])
        while True:
            choice2 = random.choice(nested_dict[playername][0][whatpos.upper()])
            if choice2 != choice1:
                break
        return('You should start ' + choice1 + ' and ' + choice2 + '.')

#print(who_start('scott','poop'))

#print(nested_dict)




