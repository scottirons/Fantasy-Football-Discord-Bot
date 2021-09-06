import spongemock

randomstring = "henry veto trade"

if ('king henry') in randomstring:
    print('king')
if ('henry') in randomstring:
    print("That's King Henry to you.")
if ('veto') in randomstring:
    print(spongemock.sponge(randomstring))
if ('trade') in randomstring:
    print('I VETO THIS TRADE')
