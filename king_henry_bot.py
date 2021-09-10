import discord
import os
import spongemock
import random_qb
import random_rb
import random_player
import starterpick
from discord.ext import commands
import asyncio
import random


questions = ['who', 'what', 'which']
rbeez = ['rb', 'running back', 'runningback']
qbeez = ['qb', 'quarterback']
winloss = ['win', 'lose', 'last', 'first']
swears = ['fuck', 'shit', 'damn', ' hell ', ' ass ', 'bitch', 'cunt', 'whore', 'dick', 'laura']
ournames = ['Arvin', 'Liam', 'Brendan', 'Ben', 'Patrick',\
            'Jrog', 'Scott', 'Robert', 'Nathaniel', 'Jon', 'Nick', 'Jared']
positions = ['k', 'qb', 'rb', 'running back', 'runningback', 'quarter back',\
             'quarterback', 'd/st', 'def', 'defense', 'kicker', 'flex', 'te',\
             'tight end', 'wr', 'wide receiver']
answers = ['yes', 'no', 'of course', 'perhaps', 'fuck if I know', "it's unlikely", \
           'sleep on it', 'it shall be done', 'my sources say no', 'nah', 'definitely',\
           'most likely', 'probs', "I'm not confident in it", 'shabalabanono', 'get J riggity riggity'\
           'riggity riggity riggity rekt']
sup = ['hi', 'hello', 'hey', 'howdy']
answers = ['suh dude', 'suh', 'wassup', "what's crackin'?", 'howdly doodly, neighbor', 'hi', 'hello', 'heyyy \U0001F609',\
           'how u doin']
byez = ['bye', 'good night', 'see you', 'toodles']
bye = ['toodles', 'bye gurl', 'see ya later, alligator', 'in a while, crocodile', 'peace out, Boy Scout']


client = commands.Bot(command_prefix=['!'])

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command()
async def starters(ctx):

    try:        
        await ctx.send("What's your name?")
        msg = await client.wait_for('message', check=lambda \
                message: message.author == ctx.author, timeout=10)
        
        if msg:
            msg = msg.content
            if msg.capitalize() not in ournames:
                await ctx.send("I'm sorry, I don't recognize that name. "
                               "You get one more try." )
                msg = await client.wait_for('message', check=lambda \
                message: message.author == ctx.author, timeout=10)
                msg = msg.content
            await ctx.send("What position?")
            position = await client.wait_for('message', check=lambda \
                    message: message.author == ctx.author, timeout=10)
        if position:
            position = position.content
            if position not in positions:
                await ctx.send("I'm sorry, I don't recognize that position. "\
                               "You get one more try." )
                position = await client.wait_for('message', check=lambda \
                    message: message.author == ctx.author, timeout=10)
                position = position.content            
            await ctx.channel.send(starterpick.who_start(msg,position))
        
    except asyncio.TimeoutError:
        await ctx.send('TOO SLOW!')

@client.command(name="8ball")
async def _8ball(ctx):
    await ctx.send(random.choice(answers))
        
    

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    message.content = message.content.lower()

    #kindness 
    if ('thank') in message.content:
        await message.channel.send("Ain't no thang, gurl")
    if any(word in message.content for word in sup):
        await message.channel.send(random.choice(answers))
    if any(word in message.content for word in byez):
        await message.channel.send(random.choice(bye))

    #good bot bad bot
    if ('good bot') in message.content:
        await message.channel.send('You know it.')
    if ('bad bot') in message.content:
        await message.channel.send('no u')

    #henry and king henry stuff
    if ('king henry') in message.content:
        await message.channel.send("\U0001F451")    
    elif ('henry henry henry') in message.content:
        await message.channel.send("KING KING KING!")
    elif ('king king king') in message.content:
        await message.channel.send("HENRY HENRY HENRY!")
    elif ('henry') in message.content:
        await message.channel.send("That's King Henry to you.")

    #random stuff
    if ('kelce') in message.content:
        await message.channel.send("Ben, why didn't you draft me instead? \U0001F97A")
    if('fumble') in message.content:
        await message.channel.send(file=discord.File('zeke.jpg'))
   # if('qb') in message.content:
   #     await message.channel.send(file=discord.File('manningface.jpg'))
    if('veto') in message.content:
        text = spongemock.sponge(message.content)
        await message.channel.send(text)
    if('trade') in message.content:
        await message.channel.send(file=discord.File('no trades.jpg'))
    if any(word in message.content for word in questions) \
       and any(thing in message.content for thing in qbeez):
        await message.channel.send(random_qb.which_qb())
    elif any(word in message.content for word in questions) \
       and any(thing in message.content for thing in rbeez):
        await message.channel.send(random_rb.which_rb())    
    if any(word in message.content for word in questions) \
       and any(thing in message.content for thing in winloss):
        await message.channel.send(random_player.which_player())
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
    if ('hell') in message.content:
        if message.channel.id == 883758150287757322:
            return
        else:
            if len(message.content) == 4:
                await message.channel.send(file=discord.File('watchyourprofanity.gif'))                
    await client.process_commands(message)
    


    
client.run(os.environ['DISCORD_TOKEN'])



