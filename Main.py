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
	if message.content.startswith('$pingg'):
		await client.send_message(message.channel,'Welcome <@%s>'  %(message.author.id))
	
	if message.content.startswith('$pink'):
		em = discord.Embed(description='<3')
		em.set_image(url='https://cdn.discordapp.com/attachments/528886659031236608/530655785580101633/test_for_lauras_bot.jpg%27)
		await client.send_message(message.channel, embed=em)
	
	if message.content.startswith('$pinkland'):
		await client.send_message(message.channel,'PinkLand is owned by Lauraispink and this bot was made by Spinayy!')
	
	if message.content.startswith('$server'):
		randomlist = ["Hey","Mason_smells","SlimShadySmellsGood"]
		await client.send_message(message.channel,(random.choice(randomlist)))

client.run(os.environ['BOT_TOKEN'])
