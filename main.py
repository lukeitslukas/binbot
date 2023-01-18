import discord
import asyncio
from datetime import datetime
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv() 

# setting up the bot and prefix.
prefix = "!"
bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")

# startup
@bot.event
async def on_ready():
    print("I'm in")
    print(bot.user)

    # change status
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("!help | the bins aye"))

@bot.command()
async def time(ctx):
    currentTime = datetime.now()
    await channel.send(currentTime)

@bot.command()
async def explain(ctx, arg1: int):
    if arg1 == 1:
        await ctx.send(file=discord.File('BlueBin.png'))
    if arg1 == 2:
        await ctx.send(file=discord.File('BurgundyBin.png'))
    if arg1 == 3:
        await ctx.send(file=discord.File('GrayBin.png'))


async def bins():
    await bot.wait_until_ready()
    channel = bot.get_channel(os.getenv("CHANNEL_ID"))  # Insert channel ID here
    while not bot.is_closed():
        currentTime = datetime.now()
        week = currentTime.isocalendar()[1]
        if ((week + 1) % 2) == 0 and currentTime.weekday() == 1 and currentTime.hour == 20 and currentTime.minute == 0:
            await channel.send("Yo uhh put the grey bin out lads. (General Waste)")
            await asyncio.sleep(60)
        if (week % 3) == 0 and currentTime.weekday() == 2 and currentTime.hour == 20 and currentTime.minute == 0:
            await channel.send("So that'd be burgundy bin time. (Plastics and cans)")
            await asyncio.sleep(60)
        if (week % 4) == 0 and currentTime.weekday() == 0 and currentTime.hour == 20 and currentTime.minute == 0:
            await channel.send("uh that blue bin if you wouldn't mind. (Paper and cardboard")
            await asyncio.sleep(60)
        await asyncio.sleep(10)


@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")


@bot.command()
async def help(ctx):
    embed = discord.Embed(colour=discord.Colour.blue())
    embed.title = "Bin bot"
    embed.description = "Prefix to all commands : '!'"
    embed.add_field(
        name=f"Bin Commands",
        value=f"explain 1/2/3 \n 1 - Blue bin\n 2 - Burgundy Bin\n 3 - Gray bin",
        inline=False)

    msg = await ctx.channel.send(embed=embed)
    await ctx.message.add_reaction('\U0001F44D')

    await asyncio.sleep(15)
    await msg.delete()
    await ctx.message.delete()

# let him out
if __name__ == "__main__":
    bot.loop.create_task(bins())
    token = os.getenv("TOKEN")
    bot.run(token)
