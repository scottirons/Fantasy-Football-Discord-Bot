import random

def which_player():

    my_file = open("players.txt", "r")
    players = []
    for player in my_file:
        stripped_line = player.strip()
        players.append(stripped_line)

    my_file.close()

    return(random.choice(players))
