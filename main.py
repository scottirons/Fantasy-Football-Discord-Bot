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
import you_fucked_up


class Robot:
    def __init__(self):
        pass


questions = {'who', 'what', 'which'}
rbeez = {'rb', 'running back', 'runningback'}
qbeez = {'qb', 'quarterback'}
winloss = {'win', 'lose', 'last', 'first'}
ournames = {'Arvin', 'Liam', 'Brendan', 'Ben', 'Patrick',
            'Jrog', 'Ethan', 'Robert', 'Nathaniel', 'Jon', 'Nick', 'Jared'}
positions = {'k', 'qb', 'rb', 'running back', 'runningback', 'quarter back',
             'quarterback', 'd/st', 'def', 'defense', 'kicker', 'flex', 'te',
             'tight end', 'wr', 'wide receiver'}
answers = ['yes', 'no', 'of course', 'perhaps', 'fuck if I know', "it's unlikely",
           'sleep on it', 'it shall be done', 'my sources say no', 'nah', 'definitely',
           'most likely', 'probs', "I'm not confident in it", 'shabalabanono', 'get J riggity riggity'
                                                                               ' riggity riggity riggity rekt']
sup = {'hi ', 'hello', 'howdy'}
friendly_answers = {'suh dude', 'suh', 'wassup', "what's crackin'?", 'howdly doodly, neighbor', 'hi', 'hello',
                    'heyyy \U0001F609', 'how u doin'}
byez = {'bye', 'good night', 'see you', 'toodles'}
bye = {'toodles', 'bye gurl', 'see ya later, alligator', 'in a while, crocodile', 'peace out, Boy Scout'}
swears = {'fuck', 'shit', 'damn', ' ass ', 'bitch', 'cunt', 'whore', 'dick', 'laura'}

client = commands.Bot(command_prefix=['!'])


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command(brief="how many more points could you have scored?")
async def goober(ctx):
    try:
        await ctx.send("What's your name?")
        msg = await client.wait_for('message', check=lambda
            message: message.author == ctx.author, timeout=10)
        if msg:
            msg = msg.content
            if msg.capitalize() not in ournames:
                await ctx.send("I'm sorry, I don't recognize that name. "
                               "You get one more try.")
                msg = await client.wait_for('message', check=lambda
                    message: message.author == ctx.author, timeout=10)
                msg = msg.content
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
                week = week.content
            week = int(week)
            await ctx.channel.send(you_fucked_up.max_points(msg, week))

    except asyncio.TimeoutError:
        await ctx.send('TOO SLOW!')


@client.command(brief="AKERS OR NAH??")
async def starters(ctx):
    try:
        await ctx.send("What's your name?")
        msg = await client.wait_for('message', check=lambda \
                message: message.author == ctx.author, timeout=10)

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
                await ctx.send("I'm sorry, I don't recognize that position. "
                               "You get one more try.")
                position = await client.wait_for('message', check=lambda \
                        message: message.author == ctx.author, timeout=10)
                position = position.content
            if position.lower() == 'flex':
                await ctx.channel.send(flex_squads.pick_flex(msg))
            else:
                await ctx.channel.send(starterpick.who_start(msg, position))

    except asyncio.TimeoutError:
        await ctx.send('TOO SLOW!')


@client.command(name="8ball", brief="da bot knows everything")
async def _8ball(ctx):
    await ctx.send(random.choice(answers))


@client.command(brief="stop typing '!injuries jon' u jerks")
async def injuries(ctx, name):
    name = name.title()
    await ctx.channel.send(injured_player.injury(name))


@client.command(brief="BOOOOOOO DESCRIPTIONS BOOOOOOOOOO")
async def boo(ctx, *msg):
    await ctx.send("BOOOOO " + (("{}".format(" ".join(msg))).upper()) + " BOOOOOOOOO!")


@client.command(brief="made a doodoo dunderhead move? type the player's name ")
async def shoulda(ctx, *msg):
    await ctx.send("Damn, I should have started " + ((("{}".format(" ".join(msg))).title()) + "."))


@client.command(brief="type a player's name and see his average points. wow :)")
async def points(ctx, *msg):
    name = ("{}".format(" ".join(msg)))
    await ctx.send((stats_pull.average_points(name)))


@client.command(brief="power rankings aka who's close to Arvin")
async def power(ctx):
    await ctx.send(power_rankings.stonks())


@client.command(brief="gives you average points 'n' stuff")
async def scoring(ctx, name):
    name = name.title()
    await ctx.send(points_stuff.points(name))


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
    if ('veto') in message.content:
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


client.run(os.environ['DISCORD_TOKEN'])
