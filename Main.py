import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import os
from discord import Game

Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()

@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Welcome to the server hope you have a great time!!!!!')
    print('Sent message to ' + member.name)

@client.event
async def on_ready():
	await client.change_presence(game=Game(name='Pink Land'))
	print('Ready, Freddy')
	
@client.event
async def on_message(message):
    if message.content.upper().startswith('.ADMINME'):
        userID = message.author.id
        await client.send_message(message.channel, ":x: You do not have the permission to do that <@%s" % (userID))
    if message.content.upper().startswith('.LOGIN'):
        if message.author.id == "277983178914922497": #Replace <User ID> with the ID of the user you want to be able to execute this command!
            args = message.content.split(" ")
            await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
        else:
            await client.send_message(message.channel, "You do not have permission to log into this service!")
    if message.content.upper().startswith('.AMIADMIN'):
        if "518836398216708129" in [role.id for role in message.author.roles]: #Replace <Role ID> with the ID of the role you want to be able to execute this command
            await client.send_message(message.channel, "You are an administrator!")
        else:
            await client.send_message(message.channel, "You are not an administrator! Please ensure that i have the full permissions and above all of the higher ranks.")

client.run(os.environ['BOT_TOKEN'])
