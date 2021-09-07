import discord
import os
import spongemock
import random_qb
import random_rb
import random_player
import starterpick


questions = ['who', 'what', 'which']
rbeez = ['rb', 'running back', 'runningback']
qbeez = ['qb', 'quarterback']
winloss = ['win', 'lose', 'last', 'first']
swears = ['fuck', 'shit', 'damn', 'hell', 'ass', 'bitch'] 


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    message.content = message.content.lower()
    if ('king henry') in message.content:
        await message.channel.send("\U0001F451")
    elif ('henry henry henry') in message.content:
        await message.channel.send("KING KING KING!")
    elif ('henry') in message.content:
        await message.channel.send("That's King Henry to you.")
    if ('kelce') in message.content:
        await message.channel.send("Ben, why didn't you draft me instead? \U0001F97A")
    if('fumble') in message.content:
        await message.channel.send(file=discord.File('zeke.jpg'))
    if('qb') in message.content:
        await message.channel.send(file=discord.File('manningface.jpg'))
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
        await message.channel.send(file=discord.File('watchyourprofanity.gif'))
    if ('start') in message.content:
        await message.channel.send("what's your name?")
        myname = await client.wait_for('message', timeout=15)
        await message.channel.send("what position?")
        myposition = await client.wait_for('message', timeout=15)
        await message.channel.send(name)


    
client.run(os.environ['DISCORD_TOKEN'])
