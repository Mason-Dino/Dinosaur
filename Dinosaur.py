#----------------------------------------------------------------------#
#
#       on_ready: -on_ready
#       on_command_error: -on_command_error
#       on_guild_join: -on_guild_join
#       on_guild_remove: on_guild_remove
#       on_dbl_vote: -on_dbl_vote
#
#----------------------------------------------------------------------#


import discord
import os
from discord.ext import commands
from discord.ext import tasks
from discord.ext.commands import BucketType
from functions.database import database
from Disecon import *
import asyncio
import random
import math
import sqlite3
import datetime

import os
from dotenv import load_dotenv


load_dotenv()
BTOKEN = os.getenv("BTOKEN")
TOKEN = os.getenv("TOKEN")


intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = discord.Client(intents=intents)

# the bot prefix
client = commands.Bot(command_prefix="d!", case_insensitive=True, intents=intents)
client.remove_command("help")
test_guilds = [840354954074128405]



#Owner ID for owner only command
OwnerID = 638092957756555291

cogs = ["cogs.help", "cogs.games", "cogs.owner", "cogs.economy", "cogs.utility", "cogs.vote"]
#cogs = ["cogs.top"]
#cogs = ["cogs.economy"]

#on_ready Event -on_ready
@client.event
async def on_ready():
    #database("Shop Items")
    #database("Items Own")
    #database("Economy")


    print("I'm in")
    print(client.user)
    await client.change_presence(activity=discord.Game(name="Just started up!"))
    await asyncio.sleep(5)
    await client.change_presence(activity=discord.Game(name='with d/help'))
    for cog in cogs:
        try:
            client.load_extension(cog)
            print(cog + " was loaded.")

        except Exception as e:
            print(e)

#on_command_error Event -on_command_error  
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):

        cooldown = int(error.retry_after)

        if 60 > cooldown:
            embed: discord.Embed = discord.Embed(
                title="Cooldown",
                description=f"You have :alarm_clock: **00:{error.retry_after:,.0f} seconds left**",
                color=discord.Color.green()
            )

            await ctx.send(embed=embed)

        elif 3600 > cooldown: 
            whole1 = math.floor(cooldown)
            decimal = cooldown - whole1

            left = whole1 / 60
            fractional1, whole2 = math.modf(left)

            sec = fractional1 * 60

            fractional2, whole3 = math.modf(sec)

            embed: discord.Embed = discord.Embed(
                title="Cooldown",
                description=f"You have :alarm_clock: **{whole2:,.0f}:{whole3:,.0f}** time left.",
                color=discord.Color.green()
            )
            embed.set_footer(text="Format - Minute : Seconds")

            await ctx.send(embed=embed)

        elif 86400 > cooldown:
            whole1 = math.floor(cooldown)

            whole2 = whole1 / 60

            sec1, min1 = math.modf(whole2)

            sec2 = sec1 * 60

            hour1 = min1 / 60

            min2, hour2 = math.modf(hour1)

            min3 = min2 * 60

            embed: discord.Embed = discord.Embed(
                title="Cooldown",
                description=f"You have :alarm_clock: **{hour2:,.0f}:{min3:,.0f}:{sec2:,.0f}** time left.",
                color=discord.Color.green()
            )
            embed.set_footer(text="Format - Hour:Minutes:Seconds")

            await ctx.send(embed=embed)

    elif isinstance(error, commands.CommandNotFound):
        embed: discord.Embed = discord.Embed(
            title="Invalid Command",
            description="You gave a invaild command\nPlease try doing `d/help` to see some of the commands.\n\nIf you need more support pelase join the support server where we can help you.\n[Support Server](https://discord.gg/KxPuFvazuF)",
            color=discord.Color.green()
        )

        await ctx.send(embed=embed)

    else:
        print("===============")
        print(error)

#on_guild_join Event -on_guild_join
@client.event
async def on_guild_join(guild):
    join = client.get_channel(840355732183318548)

    name = str(guild.name)
    description = str(guild.description)    
    owner = str(guild.owner)
    id = str(guild.id)
    region = str(guild.region)
    memberCount = str(guild.member_count)
    ownername=str(guild.owner_id)
    icon = str(guild.icon_url)  
    
    embed: discord.Embed = discord.Embed(
        title=f'Joined "{name}"',
        description=None,
        color=discord.Color.green()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=f"<@!{ownername}>", inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)
    embed.add_field(name="Current Guilds I'm in: ", value=(str(len(client.guilds))))   

    await join.send(embed=embed)

#on_guild_remove Event -on_guild_remove
@client.event
async def on_guild_remove(guild):
    join = client.get_channel(840355732183318548)

    name = str(guild.name)
    description = str(guild.description)    
    owner = str(guild.owner)
    id = str(guild.id)
    region = str(guild.region)
    memberCount = str(guild.member_count)
    ownername=str(guild.owner_id)
    icon = str(guild.icon_url)  
    
    embed: discord.Embed = discord.Embed(
        title=f'Left "{name}"',
        description=None,
        color=discord.Color.red()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=f"<@!{ownername}>", inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)
    embed.add_field(name="Current Guilds I'm in: ", value=(str(len(client.guilds))))   

    await join.send(embed=embed)

#on_dbl_vote Event -on_dbl_vote
@client.event
async def on_dbl_vote(data):
    if data["type"] == "test":
        guild = client.get_guild(840354954074128405)

        votechannel = discord.utils.get(guild.channels, name="vote-logs")
        
        user = 638092957756555291

        user = client.get_user(user)

        conn = sqlite3.connect("vote.db")
        c = conn.cursor()

        c.execute(f"SELECT * FROM vote WHERE user_ID={user.id}")

        items = c.fetchall()
        none = str(items)

        if none == "[]":
            c.execute(f"INSERT INTO vote VALUES ({user.id}, 1)")

            conn.commit()

        else:
            for item in items:
                vote = int(item[1])

            vote = vote + 1

            c.execute(f"""UPDATE vote SET votes = {vote}
                        WHERE user_ID = {user.id}  
                    """)

            conn.commit()
            conn.close()

        embed: discord.Embed = discord.Embed(
            title=f"{user.name} Voted!",
            description=f"ID - {user.id}",
            color=discord.Color.dark_green()
        )
        embed.set_footer(text=f"This user has voted {vote} times")

        await votechannel.send(embed=embed)

        if none =="[]":
            embed: discord.Embed = discord.Embed(
                title="Thanks for voting!",
                description=f"You have voted 1 time so far!",
                color=discord.Color.dark_green()
            )
            try:
                await user.send(embed=embed)

            except:
                pass

        else:
            embed: discord.Embed = discord.Embed(
                title="Thanks for voting!",
                description=f"You have voted {vote} times so far!",
                color=discord.Color.dark_green()
            )

            try:
                await user.send(embed=embed)

            except:
                pass

    else:
        guild = client.get_guild(840354954074128405)

        votechannel = discord.utils.get(guild.channels, name="vote-logs")
        
        user = int(data["user"])

        user = client.get_user(user)

        conn = sqlite3.connect("vote.db")
        c = conn.cursor()

        c.execute(f"SELECT * FROM vote WHERE user_ID={user.id}")

        items = c.fetchall()
        none = str(items)

        if none == "[]":
            c.execute(f"INSERT INTO vote VALUES ({user.id}, 1)")

            vote = 1

            conn.commit()

            embed: discord.Embed = discord.Embed(
                title=f"{user.name} Voted!",
                description=f"ID - {user.id}",
                color=discord.Color.green()
            )
            embed.set_footer(text=f"This user has voted {vote} times")

            await votechannel.send(embed=embed)

            if none =="[]":
                embed: discord.Embed = discord.Embed(
                    title="Thanks for voting!",
                    description=f"You have voted 1 time so far!",
                    color=discord.Color.green()
                )
                try:
                    await user.send(embed=embed)

                except:
                    pass

        else:
            for item in items:
                vote = int(item[1])

            vote = vote + 1

            c.execute(f"""UPDATE vote SET votes = {vote}
                        WHERE user_ID = {user.id}  
                    """)

            conn.commit()
            conn.close()

        embed: discord.Embed = discord.Embed(
            title=f"{user.name} Voted!",
            description=f"ID - {user.id}",
            color=discord.Color.green()
        )
        embed.set_footer(text=f"This user has voted {vote} times")

        await votechannel.send(embed=embed)

        if none =="[]":
            embed: discord.Embed = discord.Embed(
                title="Thanks for voting!",
                description=f"You have voted 1 time so far!",
                color=discord.Color.green()
            )
            try:
                await user.send(embed=embed)

            except:
                pass

        else:
            embed: discord.Embed = discord.Embed(
                title="Thanks for voting!",
                description=f"You have voted {vote} times so far!",
                color=discord.Color.green()
            )

            try:
                await user.send(embed=embed)

            except:
                pass
        


client.run(TOKEN)
