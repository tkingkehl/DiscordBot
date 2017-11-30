import discord
import datetime
import asyncio
import random
import json
import os
import pybaseball
import weather
import steamapi

client = discord.Client()

file = open("C:/Users/darth/Documents/token.txt")
token = file.read()
file = open("C:/Users/darth/Documents/SteamToken.txt")
steamToken = file.read()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-------')

@client.event
async def on_message(message):
    if message.content.startswith('!istimcool'): # Tim is cool, duh.
        await client.send_message(message.channel, 'Well of course.')

    elif message.content.startswith('!hidrricks'): # Tim is cool, duh.
        await client.send_message(message.channel, 'Hello! It must be lab day.')

    elif message.content.startswith('!whattimeisit'): # Returns current time
        await client.send_message(message.channel, datetime.datetime.now().time())
        await client.send_message(message.channel, 'Central Time')

    elif message.content.startswith('!coinflip'): # Flips a coin
        resultOfFlip = random.choice(['Heads', 'Tails'])
        await client.send_message(message.channel, resultOfFlip)

    elif message.content.startswith('!addquote'): # Adds a quote to a running quote file.!
        if not os.path.isfile("quote_file.pk1"):
            quote_list = []
        else:
            with open("quote_file.pk1", "r") as quote_file:
                quote_list = json.load(quote_file)
        quote_list.append(message.content[9:])
        with open("quote_file.pk1", "w") as quote_file:
                json.dump(quote_list, quote_file)

    elif message.content.startswith('!quote'): # Pulls a random quote from the quote file.
        with open("quote_file.pk1", "r") as quote_file:
                quote_list = json.load(quote_file)
        await client.send_message(message.channel, random.choice(quote_list))

    elif message.content.startswith('!rps'): # Play rock paper scissors.
        rps = random.choice(["Rock", "Paper", "Scissors"])
        await client.send_message(message.channel, rps)

    elif message.content.startswith('!meme'):  # Turns to emoji text.
        Message = message.content[6:]

        if Message == 'hello':  # hello
            await client.send_message(message.channel, ':regional_indicator_h::regional_indicator_e::regional_indicator_l::regional_indicator_l::regional_indicator_o:')
        elif Message == 'liam sucks':  # liam sucks
            await client.send_message(message.channel, ':regional_indicator_l::regional_indicator_i::regional_indicator_a::regional_indicator_m: :regional_indicator_s::regional_indicator_u::regional_indicator_c::regional_indicator_k::regional_indicator_s:')

    elif message.content.startswith('!stats'):  # Returns batting stats for player
        playerName = message.content[7:]
        print(playerName)

        if playerName == 'Mike Moustakas':
            from pybaseball import statcast_batter
            playerID = 519058
            moustakasStats = statcast_batter('2017-04-01', '2017-09-01', playerID)
            print('success')
            await client.send_message(message.channel, moustakasStats)

    elif message.content.startswith('!censor'):  # NO SWEARING
        await client.send_message(message.channel, 'http://i0.kym-cdn.com/photos/images/original/001/299/189/6bb.jpg')

    elif message.content.startswith('!weather'):  # Returns condition and temp at location
        location = message.content[9:]

        from weather import Weather
        weather = Weather()
        lookup = weather.lookup_by_location(location)
        condition = lookup.condition().text()
        temp = lookup.condition().temp()
        desc = lookup.description()

        await client.send_message(message.channel, condition)
        await client.send_message(message.channel, temp)
        await client.send_message(message.channel, desc)

    elif message.content.startswith('!steam'):  # Steam info
        steamapi.core.APIConnection(api_key=steamToken, validate_key=True)
        me = steamapi.user.SteamUser(userurl="acanceroustwzlr")

        steamCommand = message.content[7:]

        if steamCommand == 'level':
            await client.send_message(message.channel, me.level)
        elif steamCommand == 'friends':
            await client.send_message(message.channel, me.friends)
        elif steamCommand == 'recently_played':
            await client.send_message(message.channel, me.recently_played)
        elif steamCommand == 'games':
            await client.send_message(message.channel, me.games)


client.run(token)