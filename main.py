
import discord
import json
import sys
from colorama import Fore,Style
import asyncio as aio
import random as rd
from discord.ext import commands as client
from discord import *
from discord.ext import commands, tasks
from itertools import cycle
from discord.ext.commands.core import command
from dotenv import load_dotenv
import os
import random

client = commands.Bot(command_prefix = '.')
status = cycle(['with ', 'your mom'])
@tasks.loop(seconds=2)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready.')

@client.event
async def on_reaction_add(reaction, user):
  ChID = '876213816139071518'
  if reaction.message.channel.id != ChID:
    return
  if reaction.emoji == "💻":
    Role = discord.utils.get(user.server.roles, name="Coder")
    await client.add_roles(user, Role)
    print('Hello')

@client.event
async def on_member_join(member):
    print(f'{member} Fuck you!')

@client.event
async def on_member_remove(member):
    print(f'{member} has left this stupid server!')

@client.command()
async def pong(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason='Is gay'):
    await member.ban(reason=reason)
    await ctx.send(f'Banned for being gay')

@client.command()
async def ember(ctx):
    ember = [ 
        'cJOZAN', 'kdlqlW', 'P4Wx9p',
    ]
    response = random.choice(ember)
    await ctx.send(response)

@client.command()
async def obelisk(ctx):
    obelisk = [
        'rk16nn', 'sO-mWP',
    ]
    response = random.choice(obelisk)
    await ctx.send(response)

@client.command()
async def nimbus(ctx):
    nimbus = [
        'VY5CsN', 'qKxzFO',
    ]
    response = random.choice(nimbus)
    await ctx.send(response)

@client.command()
async def dunes(ctx):
    dunes = [
        'snXVWG', 'XDXX4U',
    ]
    response = random.choice(dunes)
    await ctx.send(response)

@client.command()
async def training(ctx):
    training = [
        'u_02cc', '-Mg2ZO',
    ]
    response = random.choice(training)
    await ctx.send(response)

@client.command()
async def bridge(ctx):
    bridge = [
        'Glgyie', 'DIRYil',
    ]
    response = random.choice(bridge)
    await ctx.send(response)


client.run('ODgwODAyNDYxNTg0MDk3MzEx.YSjlNw.df9EFGYm-YdmvT2t9vs_2qLt9ME')