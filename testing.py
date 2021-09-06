import spongemock

randomstring = "what henry veto qb trade"

if ('king henry') in randomstring:
    print('king')
if ('henry') in randomstring:
    print("That's King Henry to you.")
if ('veto') in randomstring:
    print(spongemock.sponge(randomstring))
if (('who') or ('what')) and (('qb') or ('quarterback')) in randomstring:
    print('bleh')
