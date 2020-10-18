# bot.py
import os
import random
from dotenv import load_dotenv
from discord.ext import commands
from canvas import getCourses, getEvents
import discord

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

@bot.command(name='showCourse', help="Show the courses that you are in")
async def showcourse(ctx):
  courseList = getCourses()
  res = ""
  for course in courseList:
    res += "- " + course + "\n"
  embed = discord.Embed()
  embed.add_field(name="Current Courses", value=res, inline=False)
  await ctx.send(embed=embed)

@bot.command(name='events', help="Shows the upcoming events. <input> = OH or Section")
async def showEvent(ctx, input: str):
  eventList = getEvents()
  res = ""
  if (input.lower() == "oh"):
    for event in eventList:
      if ('OH' in event['name'] or 'Office Hours' in event['name']):
        res += "- " + event['name'] + " " + event['start_time'] + "\n"
  embed = discord.Embed()
  embed.add_field(name="Upcoming Events", value=res, inline=False)
  await ctx.send(embed=embed)

# Incorrect role error message
@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.errors.CheckFailure):
    await ctx.send('You do not have the correct role for this command.')
  elif isinstance(error, commands.CommandNotFound):
    await ctx.send('This command does not exist. Please use c!help to see valid commands.')

bot.run(TOKEN)