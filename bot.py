# bot.py
import os
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Command prefix
bot = commands.Bot(command_prefix='c!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='david', help='Responds with whether or not you are better than david')
async def david(ctx):
  response = f'{ctx.author.name} is better than david'
  await ctx.send(response)

@bot.command(name='createrole', help='Give yourself the Student Role')
async def createrole(ctx, role: str):
  await ctx.guild.create_role(name=role)

# Incorrect role error message
@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.errors.CheckFailure):
    await ctx.send('You do not have the correct role for this command.')

# Incorrect command error
@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send('This command does not exist. Please use c!help to see valid commands.')


bot.run(TOKEN)