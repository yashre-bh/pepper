import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('BOT_TOKEN')

intents = discord.Intents.all()
discord.members = True

bot = commands.Bot(command_prefix = 'pep ', intents = intents)

@bot.event 
async def on_ready():
    print('All set!')

@bot.event
async def on_member_join(member):
    print(f'{member} has joined the server')

@bot.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

@bot.command()
async def ping(ctx):
    await ctx.send('Hello!')
    
@bot.command()
async def clear(ctx, number=1):
    await ctx.channel.purge(limit=number)


bot.run(token)