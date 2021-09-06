import random
questions = ['who', 'what', 'which']
other_stuff = ['qb', 'quarterback']
def which_qb():

    my_file = open("quarterbacks.txt", "r")
    qbs = []
    for qb in my_file:
        stripped_line = qb.strip()
        qbs.append(stripped_line)

    my_file.close()

    return(random.choice(qbs))



