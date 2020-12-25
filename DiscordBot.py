import asyncio
import discord
import random
import time
from discord.ext import commands

bot = discord.Client()
bot = commands.Bot(command_prefix = '.')
owner_id=451442660490739722

def global_variables():
    variables={'names': ['Clear','Nuke','nuke','purge','Purge'], 'me' : ['author','Author','Owner'], 'noprefix': ['f','F'], 'i' : 1}
    return variables

x = global_variables()

@bot.event
async def on_ready():
    print('Bot is ready')
    style=discord.Activity(type=discord.ActivityType.watching, name='Making a Discord Bot')
    await bot.change_presence(status=discord.Status.idle, activity=style)

@bot.command(aliases=x['names'])
async def clear(ctx,amount=2):
    await ctx.channel.purge(limit=amount)

@bot.command()
async def ping(ctx):
  await ctx.send(f'My Latency : {round(bot.latency*1000)}ms')

@bot.command()
async def annoy(ctx, member : discord.Member):
    i=1
    while i<=25:
        await ctx.send(f'{member.mention}')
        time.sleep(0.5)
        i+=1

@bot.command()
async def annoyrole(ctx, role : discord.Role):
    i=1
    while i<=25:
        await ctx.send(f"{role.mention}")
        i+=1
                        
@bot.command()
async def coolrate(ctx, member : discord.Member):
    await ctx.send(f'{member.mention} is {int((random.uniform(0,10)/10)*100)}% Cool')

@bot.command()
async def gayrate(ctx, member : discord.Member):
    await ctx.send(f'{member.mention} is {int((random.uniform(0,10)/10)*100)}% Gay')

@bot.command(aliases=x['me'])
async def owner(ctx):
    await ctx.send(f'Username of the Wonderful Person who made me : {ctx.author}')



bot.run('Your Token Goes here')
