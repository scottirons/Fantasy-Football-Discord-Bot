from injuries import injured_dict

def injury(person):
    nested_dict = injured_dict()  # create the dictionary i think
#    print(nested_dict)
    person = person.title()
    if person not in nested_dict:
        return('name does not exist')
    else:

        injured = []
        questionable = []
        counter = 1
        try:
            questionable += (nested_dict[person][0]['QUESTIONABLE'])
        except:
            counter += 69
        try:
            injured += (nested_dict[person][0]['OUT'])
        except:
            counter += 1
        try:
            injured += (nested_dict[person][0]['IR'])
        except:
            counter += 13

        if injured == [] and questionable == []:
            thing = (['Wow, your whole team is healthy!'])
            thing = '\n'.join(thing)
            return(thing)
        elif injured == []:
            thing = (['The following players are questionable:'] + questionable)
            thing = '\n'.join(thing)
            return(thing)
        elif questionable == []:
            thing = (['The following players are injured:'] + injured)
            thing = '\n'.join(thing)
            return(thing)
        else:
            thing = (['The following players are questionable:'] + questionable +
                   ['and the following players are injured:'] + injured)
            thing = '\n'.join(thing)
            return(thing)

       #     return(nested_dict[person][0]['OUT'])

print(injury('scott'))
