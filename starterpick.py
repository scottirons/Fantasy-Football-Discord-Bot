from main import league
import random

#print(league.teams)
nested_dict = {}
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
        pos_name.setdefault(player.position, []).append(player.name)
    nested_dict.setdefault(team.team_name, []).append(pos_name)

ournames = ['Arvin', 'Liam', 'Brendan', 'Ben', 'Patrick', 'Jrog', 'Scott', 'Robert', 'Nathaniel', 'Jon', 'Nick', 'Jared']
positions = ['QB', 'WR', 'RB', 'TE', 'D/ST', 'K', 'FLEX']
nested_dict = dict(zip(ournames, list(nested_dict.values())))


def who_start(playername, whatpos):
    if 'mom' in playername:
        return 'bruh'
    if 'doggy' in whatpos:
        return 'bruh'
    if playername.capitalize() not in nested_dict:
        return 'name does not exist'
    playername = playername.capitalize()
    if whatpos.lower() in ('defense', 'def', 'd'):
        whatpos = 'd/st'
    if whatpos.lower() in ('running back', 'running'):
        whatpos = 'rb'
    if whatpos.lower() in ('quarter back', 'quarterback', 'qb'):
        whatpos = 'qb'
    if whatpos.lower() in 'wide receiver':
        whatpos = 'wr'   
    elif 'quarter' in whatpos.lower():
        whatpos = 'qb'
    elif whatpos.lower() == 'kicker':
        whatpos = 'k'
    if whatpos.upper() not in positions:
        return 'position does not exist'
    if whatpos in ('k', 'te', 'qb', 'd/st'):
        return 'You should start '+ random.choice(nested_dict[playername][0][whatpos.upper()]) + '.'
#    elif whatpos == 'flex':
#        newpos = random.choice(['wr', 'rb'])
#       return('You should start ' + random.choice(nested_dict[playername][0][newpos.upper()]) + '.')
    else:
        choice1 = random.choice(nested_dict[playername][0][whatpos.upper()])
        while True:
            choice2 = random.choice(nested_dict[playername][0][whatpos.upper()])
            if choice2 != choice1:
                break
        return 'You should start ' + choice1 + ' and ' + choice2 + '.'

# print(who_start('scott','qb'))

#print(nested_dict)




