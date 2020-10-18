# bot.py
import os
import random
import sqlite3
import discord

from dotenv import load_dotenv
from discord.ext import commands
from canvas import getCourses, getEvents
import discord
intents = discord.Intents.all()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Command prefix
bot = commands.Bot(command_prefix='c!', intents=intents)

# Connect db
connection = sqlite3.connect("canvasbot.db")

@bot.event
async def on_ready():
  print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_disconnect():
  connection.close()
  print(f'{bot.user.name} has shut down.')


@bot.event
async def on_guild_join(guild):
  cursor = connection.cursor()
  cursor.execute(f"INSERT INTO Servers VALUES({guild.id},'{guild.name}')")
  for member in guild.members:
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO Members VALUES ('{member}', {member.guild.id}, 0)")

@bot.event
async def on_guild_remove(guild):
  cursor = connection.cursor()
  cursor.execute(f"DELETE FROM Servers WHERE sid = {guild.id}")
  cursor.execute(f"DELETE FROM Members WHERE sid = {guild.id}")

@bot.event
async def on_member_join(member):
  cursor = connection.cursor()
  cursor.execute(f"INSERT INTO Members VALUES ('{member}', {member.guild.id}, 0)")

@bot.event
async def on_member_remove(member):
  cursor = connection.cursor()
  cursor.execute(f"DELETE FROM Members WHERE name = '{member}' AND sid = {member.guild.id})")

# @bot.command(name='join')
# async def join(ctx):
#   await ctx.send(f'{ctx.author} {ctx.author.guild.id}')
#   print(f'{ctx.author} {ctx.author.guild.id}')
#   cursor = connection.cursor()
#   cursor.execute(f"INSERT INTO Members VALUES ('{ctx.author}', {ctx.author.guild.id}, 0)")
#   print("works")
#   temp = cursor.execute("SELECT * FROM Members").fetchall()
#   print(temp)

# @bot.command(name='createrole', help='Give yourself the Student Role')
# async def createrole(ctx, role: str):
#   await ctx.guild.create_role(name=role)

@bot.command(name='optin', help='Opt-In for schedule reminders.')
async def optin(ctx):
  cursor = connection.cursor()
  cursor.execute(f"UPDATE Members SET optin = 1 WHERE name = '{ctx.author}' AND sid = {ctx.author.guild.id}")
  await ctx.author.send('You are signed up for reminders!')

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

# Error Messages
@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.errors.CheckFailure):
    await ctx.send('You do not have the correct role for this command.')
  elif isinstance(error, commands.CommandNotFound):
    await ctx.send('This command does not exist. Please use c!help to see valid commands.')

bot.run(TOKEN)