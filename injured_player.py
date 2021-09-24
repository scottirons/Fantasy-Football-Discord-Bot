from injuries import injured_dict

def injury(person):
    nested_dict = injured_dict()  # create the dictionary i think
#    print(nested_dict['Robert'][0])
    person = person.title()
    if person not in nested_dict:
        return('name does not exist')
    else:

        injured = []
        questionable = []
        doubtful = []
        counter = 1
        try:
            doubtful += (nested_dict[person][0]['DOUBTFUL'])
        except:
            counter += 1
        try:
            questionable += (nested_dict[person][0]['QUESTIONABLE'])
        except:
            counter += 1
        try:
            injured += (nested_dict[person][0]['OUT'])
        except:
            counter += 1
        try:
            injured += (nested_dict[person][0]['INJURY_RESERVE'])
        except:
            counter += 1

        if injured == [] and questionable == [] and doubtful == []: # H
            thing = (['Wow, your whole team is healthy!'])
            thing = '\n'.join(thing)
            return(thing)
        elif injured == []:
            if doubtful == []:
                thing = (['The following players are questionable:'] + questionable) # F
                thing = '\n'.join(thing)
                return(thing)
            elif questionable == []:
                thing = (['The following players are doubtful:'] + doubtful) # G
                thing = '\n'.join(thing)
                return (thing)
            else:
                thing = (['The following players are questionable:'] + questionable + # E
                         ['and the following players are doubtful:'] + doubtful)
                thing = '\n'.join(thing)
                return(thing)
        elif questionable == []:
            if doubtful == []:
                thing = (['The following players are injured:'] + injured) # D
                thing = '\n'.join(thing)
                return(thing)
            else:
                thing = (['The following players are doubtful:'] + doubtful + # C
                ['and the following players are injured:'] + injured)
                thing ='\n'.join(thing)
                return(thing)
        elif doubtful == []:
            thing = (['The following players are questionable:'] + questionable + # B
                     ['and the following players are injured:'] + injured)
            thing = '\n'.join(thing)
            return(thing)
        else:
            thing = (['The following players are questionable:'] + questionable + # A
                   ['the following players are injured:'] + injured +
                    ['and the following players are doubtful:'] + doubtful)
            thing = '\n'.join(thing)
            return(thing)

       #     return(nested_dict[person][0]['OUT'])
print(injury('Robert'))
