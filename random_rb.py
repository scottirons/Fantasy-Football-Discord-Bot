import random

def which_rb():

    my_file = open("rbs.txt", "r")
    rbs = []
    for rb in my_file:
        stripped_line = rb.strip()
        rbs.append(stripped_line)

    my_file.close()

    return(random.choice(rbs))



