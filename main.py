import discord
from discord.ext import commands
import asyncio
import datetime
import os

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

timer_task = None
start_time = None


@bot.command()
async def dinnertime(ctx):
    global timer_task, start_time
    if timer_task is not None:
        await ctx.send("Dinner time is already running!")
        return

    start_time = datetime.datetime.now()
    timer_task = asyncio.create_task(dinner_timer(ctx))
    await ctx.send("Dinner timer started!")


async def dinner_timer(ctx):
    while True:
        await asyncio.sleep(1)


@bot.command()
async def dinnersover(ctx):
    global timer_task, start_time
    if timer_task is None:
        await ctx.send("No dinner timer is running!")
        return

    end_time = datetime.datetime.now()
    elapsed_time = end_time - start_time
    timer_task.cancel()
    timer_task = None
    await ctx.send(f"Dinner timer stopped! Elapsed time: {elapsed_time}")


@bot.command()
async def adam(ctx):
    user_id = "483812319995101196"
    await ctx.send(f"<@{user_id}> is ...")

bot.run(TOKEN)
