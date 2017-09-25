import discord
import datetime
import asyncio
import random
import json
import os

client = discord.Client()

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
    if message.content.startswith('!isliamcool'):  # Liam isn't cool, duh.
        await client.send_message(message.channel, 'Oh god no.')
    if message.content.startswith('!hidrricks'): # Tim is cool, duh.
        await client.send_message(message.channel, 'Hello! It must be lab day.')
    elif message.content.startswith('!whattimeisit'): # Returns current time
        await client.send_message(message.channel, datetime.datetime.now().time())
        await client.send_message(message.channel, 'Central Time')
    elif message.content.startswith('!coinflip'): # Flips a coin
        resultOfFlip = random.choice(['Heads', 'Tails'])
        await client.send_message(message.channel, resultOfFlip)
    elif message.content.startswith('!addquote'): # Adds a quote to a running quote file.
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



client.run('MzU5MTYzNDI0ODUwMzEzMjI2.DKDAkQ.PfAx65_sYyGW8bzM8boLhrPZYcQ')