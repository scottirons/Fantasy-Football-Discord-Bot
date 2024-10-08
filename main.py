from datetime import datetime, date
import discord
import os
import spongemock
import starterpick
from discord.ext import commands
import asyncio
import random
import injured_player
import flex_squads
import stats_pull
import power_rankings
import points_stuff
import goober_index
import time
from dotenv import load_dotenv
from espn_api.football import League

load_dotenv()

current_week = (date.today() - date(2024, 9, 10)).days // 7 + 2
    
questions = {'who', 'what', 'which'}
rbeez = {'rb', 'running back', 'runningback'}
qbeez = {'qb', 'quarterback'}
winloss = {'win', 'lose', 'last', 'first'}
positions = {'k', 'qb', 'rb', 'running back', 'runningback', 'quarter back',
             'quarterback', 'd/st', 'def', 'defense', 'kicker', 'flex', 'te',
             'tight end', 'wr', 'wide receiver'}
answers = ['yes', 'no', 'of course', 'perhaps', 'fuck if I know', "it's unlikely",
           'sleep on it', 'it shall be done', 'my sources say no', 'nah', 'definitely',
           'most likely', 'probs', "I'm not confident in it", 'shabalabanono', 'get J riggity riggity'
                                                                               ' riggity riggity riggity rekt']
sup = {'hi ', 'hello', 'howdy'}
friendly_answers = ['suh dude', 'suh', 'wassup', "what's crackin'?", 'howdly doodly, neighbor', 'hi', 'hello',
                    'heyyy \U0001F609', 'how u doin']
byez = {'bye', 'good night', 'see you', 'toodles'}
bye = ['toodles', 'bye gurl', 'see ya later, alligator', 'in a while, crocodile', 'peace out, Boy Scout']
swears = {'fuck', 'shit', 'damn', ' ass ', 'bitch', 'cunt', 'whore', 'dick', 'laura', 'lassen'}

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix=['!'], intents=intents)
league = League(league_id=41302936, year=2024, espn_s2='AEBZs%2F0JhLRPJvsLxD28BaBMEXt4wQELeh' \
                                                       'O2P9NAnhL2Nz23A%2Blf%2Fdal7ftW7YcOr7YngIMBEHj1pd72KKtrW2G%2F2zGVo%2BKM0YtL1At' \
                                                       'pcN2ZiLNyhIMeCr7BvYd056vhbRRX3nwd%2Fxq23R9w7bwyDhyIH5sMxVBOur690YldBTTCLJZjbHk' \
                                                       'rUg0tA6kcD3wtCiP8CICrQmezMZBSpu6dad61FwoAIJSNo2NqexL5627uGt%2BXX9f9SFK6EcqNk2z7' \
                                                       'F5%2BANM5Es9oNA8MI0Wz9a8Wt',
                swid='{F713A680-D381-43C3-93A6-80D38113C33C}')

nested_dict = {}
teams = []


for team in league.teams:
    teams.append(team.team_name)

for team in league.teams:
    nested_dict.setdefault(team.team_name, [])

    players = team.roster

    names = []
    for player in players:
        name = player.name
        names.append(name)

        pos_name = {}

    pos_name = {}
    for player in players:
        pos_name.setdefault(player.position, []).append(player.name)
    nested_dict.setdefault(team.team_name, []).append(pos_name)

ournames = ['Arvin', 'Liam', 'Cooper', 'Patrick', 'Sean', 'Brendan', 'Jon', 'Scott', 'Kyle', 'Phoenix', 'Nick',
            'David']
nested_dict = dict(zip(ournames, list(nested_dict.values())))
flexable_players = flex_squads.make_position_dict(league, current_week)

goober_scores = goober_index.full_goob(league, current_week)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command(brief="update data more easily")
async def update(ctx):
    start_time = time.perf_counter()
    global league, nested_dict, flexable_players, goober_scores, current_week
    current_week = (date.today() - date(2024, 9, 10)).days // 7 + 2
    league = League(league_id=41302936, year=2024, espn_s2='AEBZs%2F0JhLRPJvsLxD28BaBMEXt4wQELeh' \
                                                           'O2P9NAnhL2Nz23A%2Blf%2Fdal7ftW7YcOr7YngIMBEHj1pd72KKtrW2G'
                                                           '%2F2zGVo%2BKM0YtL1At' \
                                                           'pcN2ZiLNyhIMeCr7BvYd056vhbRRX3nwd'
                                                           '%2Fxq23R9w7bwyDhyIH5sMxVBOur690YldBTTCLJZjbHk' \
                                                           'rUg0tA6kcD3wtCiP8CICrQmezMZBSpu6dad61FwoAIJSNo2'
                                                           'NqexL5627uGt%2BXX9f9SFK6EcqNk2z7' \
                                                           'F5%2BANM5Es9oNA8MI0Wz9a8Wt',
                    swid='{F713A680-D381-43C3-93A6-80D38113C33C}')

    nested_dict = {}
    teams = []

    for team in league.teams:
        teams.append(team.team_name)

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

    nested_dict = dict(zip(ournames, list(nested_dict.values())))
    flexable_players = flex_squads.make_position_dict(league, current_week)
    goober_scores = goober_index.full_goob(league, current_week)
    print(f'League and positions updated in {time.perf_counter() - start_time} seconds')


@client.command(brief="Who was the goobiest goober?")
async def gooberreport(ctx):
    # if get_current_week() == 1:
    #     await ctx.send("Please wait until week 1 is over before goobology can be determined.")
    #     return
    try:
        await ctx.send("Which week's goober report do you want?")
        msg = await client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=4)
        if msg:
            try:
                week = int(msg.content)
                await ctx.send(goober_index.goober_report(max(week, 1), goober_scores))
            except ValueError:
                await ctx.send("That's not a number, you non-rule-follower. I'll just show the current week's report.")
                await ctx.send(goober_index.goober_report(max(current_week - 1, 1), goober_scores))
    except asyncio.TimeoutError:
        await ctx.send("TOO SLOW! Here's this past week's goober report.")
        await ctx.send(goober_index.goober_report(current_week - 1, goober_scores))
    await ctx.send("The goober report currently doesn't take into account which matchups were lost by extreme "
                   "goobosity and whether lower goober indices even correlate with won matchups, but that's coming "
                   "soon\u2122")



@client.command(brief="how many more points could you have scored?")
async def goober(ctx):
    # if get_current_week() == 1:
    #     await ctx.send("Please wait until week 1 is over before goobology can be determined.")
    #     return
    week = None
    try:
        await ctx.send("What's your name?")
        msg = await client.wait_for('message', check=lambda
            message: message.author == ctx.author, timeout=10)
        if msg:
            msg = msg.content
            if msg.capitalize() not in ournames:
                await ctx.send("I'm sorry, I don't recognize that name. "
                               f"Please pick one of the following names: {ournames}")
                msg = await client.wait_for('message', check=lambda
                    message: message.author == ctx.author, timeout=10)
                msg = msg.content.capitalize()
            await ctx.send("What week? Please enter a number.")
            week = await client.wait_for('message', check=lambda
                message: message.author == ctx.author, timeout=10)
        if week:
            week = week.content
            if len(week) > 2:
                await ctx.send("Wait a second, did you enter a number?"
                               " Please try again!")
                week = await client.wait_for('message', check=lambda \
                        message: message.author == ctx.author, timeout=10)
                week = int(week.content)
            start = time.perf_counter()
            msg = msg.capitalize()
            # print("it's week " + week + " and the requestor is " + msg + ".")
            week = int(week)
            # print(goober_scores)
            await ctx.channel.send(goober_index.print_goober_index(week,
                                                                   goober_scores[week][msg][0],
                                                                   goober_scores[week][msg][1],
                                                                   goober_scores[week][msg][2]))
            print("Goober index took " + str(time.perf_counter() - start) + " seconds.")

    except asyncio.TimeoutError:
        await ctx.send('TOO SLOW!')


@client.command(brief="AKERS OR NAH??")
async def starters(ctx):
    try:
        await ctx.send("What's your name?")
        msg = await client.wait_for('message', check=lambda \
                message: message.author == ctx.author, timeout=10)
        position = None
        if msg:
            msg = msg.content
            if msg.capitalize() not in ournames:
                await ctx.send("I'm sorry, I don't recognize that name. "
                               "You get one more try.")
                msg = await client.wait_for('message', check=lambda \
                        message: message.author == ctx.author, timeout=10)
                msg = msg.content
            await ctx.send("What position?")
            position = await client.wait_for('message', check=lambda \
                    message: message.author == ctx.author, timeout=10)
        if position:
            position = position.content
            if position not in positions:
                # print(position, positions)
                await ctx.send("I'm sorry, I don't recognize that position. "
                               "You get one more try.")
                position = await client.wait_for('message', check=lambda \
                        message: message.author == ctx.author, timeout=10)
                position = position.content
            if position.lower() == 'flex':
                await ctx.channel.send(flex_squads.pick_flex(msg, flexable_players))
            else:
                await ctx.channel.send(starterpick.who_start(msg, position, nested_dict))

    except asyncio.TimeoutError:
        await ctx.send('TOO SLOW!')


@client.command(name="8ball", brief="da bot knows everything")
async def _8ball(ctx):
    await ctx.send(random.choice(answers))


@client.command(brief="stop typing '!injuries liam' u jerks")
async def injuries(ctx):
    msg = None
    try:
        await ctx.send("What's your name?")
        msg = await client.wait_for('message', check=lambda
            message: message.author == ctx.author, timeout=10)
        if msg:
            msg = msg.content
            if msg.capitalize() not in ournames:
                await ctx.send("I'm sorry, I don't recognize that name. "
                               f"Please pick one of the following names: {ournames}")
                msg = await client.wait_for('message', check=lambda
                    message: message.author == ctx.author, timeout=10)
                msg = msg.content.capitalize()
        if msg:
            await ctx.channel.send(injured_player.injury(msg, league))
    except asyncio.TimeoutError:
        await ctx.send('TOO SLOW!')
    


@client.command(brief="BOOOOOOO DESCRIPTIONS BOOOOOOOOOO")
async def boo(ctx, *msg):
    await ctx.send("BOOOOO " + (("{}".format(" ".join(msg))).upper()) + " BOOOOOOOOO!")


@client.command(brief="made a doodoo dunderhead move? type the player's name ")
async def shoulda(ctx, *msg):
    await ctx.send("Damn, I should have started " + ((("{}".format(" ".join(msg))).title()) + "."))


@client.command(brief="type a player's name and see his average points. wow :)")
async def playerpoints(ctx):
    name = None
    try:
        await ctx.send("Which player's scoring do you want?")
        name = await client.wait_for('message', check=lambda
            message: message.author == ctx.author, timeout=10)
        if name:
            await ctx.send((stats_pull.average_points(name.content, league)))
    except asyncio.TimeoutError:
        await ctx.send('TOO SLOW!')
    


@client.command(brief="power rankings aka who's close to Arvin")
async def power(ctx):
    await ctx.send(power_rankings.stonks(league))


@client.command(brief="gives you average points 'n' stuff")
async def scoring(ctx):
    msg = None
    try:
        await ctx.send("What's your name?")
        msg = await client.wait_for('message', check=lambda
            message: message.author == ctx.author, timeout=10)
        if msg:
            msg = msg.content
            if msg.capitalize() not in ournames:
                await ctx.send("I'm sorry, I don't recognize that name. "
                               f"Please pick one of the following names: {ournames}")
                msg = await client.wait_for('message', check=lambda
                    message: message.author == ctx.author, timeout=10)
                msg = msg.content.capitalize()
        if msg:
            await ctx.send(points_stuff.points(msg, league, current_week - 1))
    except asyncio.TimeoutError:
        await ctx.send('TOO SLOW!')
    


@client.command(brief='just repeats your message lol')
async def chevy(ctx, *msg):
    msg = ("{}".format(" ".join(msg)))
    await ctx.send(msg)


@client.command(brief="ok this one will take work")
async def trade(ctx):
    await ctx.send('hi')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    message.content = message.content.lower()

    # kindness
    if 'thank' in message.content:
        await message.channel.send("Ain't no thang, gurl")
    if any(word in message.content for word in sup):
        await message.channel.send(random.choice(friendly_answers))
    if any(word in message.content for word in byez):
        await message.channel.send(random.choice(bye))

    # good bot bad bot
    if 'good bot' in message.content:
        await message.channel.send('You know it.')
    if 'bad bot' in message.content:
        await message.channel.send('no u')

    # henry and king henry stuff
    if 'king henry' in message.content:
        await message.channel.send("\U0001F451")
    elif ('henry henry henry') in message.content:
        await message.channel.send("KING KING KING!")
    elif ('king king king') in message.content:
        await message.channel.send("HENRY HENRY HENRY!")
    elif ('henry') in message.content:
        await message.channel.send("That's King Henry to you.")

    # random stuff
    if ('kelce') in message.content:
        await message.channel.send("Ben, why didn't you draft me instead? \U0001F97A")
    if ('fumble') in message.content:
        await message.channel.send(file=discord.File('zeke.jpg'))
    # if('qb') in message.content:
    #     await message.channel.send(file=discord.File('manningface.jpg'))
    if 'veto' in message.content:
        text = spongemock.sponge(message.content)
        await message.channel.send(text)
    #    if('trade') in message.content:
    #        await message.channel.send(file=discord.File('no trades.jpg'))
    #        await message.channel.send("ok fine yes trades")
    # if any(word in message.content for word in questions) \
    #         and any(thing in message.content for thing in qbeez):
    #     await message.channel.send(random_qb.which_qb())
    # elif any(word in message.content for word in questions) \
    #         and any(thing in message.content for thing in rbeez):
    #     await message.channel.send(random_rb.which_rb())
    # if any(word in message.content for word in questions) \
    #         and any(thing in message.content for thing in winloss):
    #     await message.channel.send(random_player.which_player())
    if any(word in message.content for word in swears):
        if message.channel.id == 883758150287757322:
            return
        else:
            await message.channel.send(file=discord.File('watchyourprofanity.gif'))
    if ('ass') in message.content:
        if message.channel.id == 883758150287757322:
            return
        else:
            if len(message.content) == 3:
                await message.channel.send(file=discord.File('watchyourprofanity.gif'))
    await client.process_commands(message)


client.run(os.getenv('DISCORD_TOKEN'))
