import subprocess
import sys

#subprocess.run([sys.executable, '-m', 'pip', 'install', 'psutil'])

import discord
import os
from discord.ext import commands
from discord.ext import tasks
from discord.ext.commands import BucketType
from dislash import *
import asyncio
import random
import math
import sqlite3
import topgg


client = discord.Client()

intents = discord.Intents.default()
intents.members = True

# the bot prefix
client = commands.Bot(command_prefix="d//", case_insensitive=True, intents=intents)
slash = slash_commands.SlashClient(client)
client.remove_command("help")
test_guilds = [840354954074128405]



#Owner ID for owner only command
OwnerID = 638092957756555291

cogs = ["cogs.help", "cogs.games", "cogs.owner", "cogs.economy", "cogs.utility", "cogs.moderation.mod_commands", "cogs.moderation.mod_search", "cogs.moderation.mod_set_up", "cogs.vote", "cogs.suggestion", "cogs.partner", "cogs.test"]
#cogs = ["cogs.top"]
#cogs = ["cogs.economy"]

# start
@client.event
async def on_ready():
    conn = sqlite3.connect("shop_items.db")
    c = conn.cursor()
    
    try:
        c.execute("""CREATE TABLE shop_items (
            name text,
            price int,
            option text,
            use text,
            visible text
            
        )""")
        
    except:
        print("Shop Items was not mad")
        pass
    
    conn.commit()
    conn.close()
    
    conn = sqlite3.connect("shop.db")
    c = conn.cursor()
    
    try:
        c.execute("""CREATE TABLE items_own (
               user_id text,
               item_name text,
               amount text 
        
        )""")
        
        print("Items Own table made")
        
    except:
        print("items owner table not made")
        pass
    
    conn = sqlite3.connect("partner.db")
    c = conn.cursor()

    try:
        c.execute("""CREATE TABLE application (
            message_id text,
            ammount_yes int,
            ammount_no int,
            question_1 text,
            question_2 text,
            question_3 text,
            question_4 text,
            question_5 text,
            question_6 text,
            question_7 text,
            status text
        
        )""")

        pass

    except:
        pass
    

    conn.commit()
    conn.close()

    conn = sqlite3.connect("auto.db")
    c = conn.cursor()
    
    try:
        c.execute("""CREATE TABLE member_join (
            guild_id int,
            join_channel int,
            message text
        
        )""")

        pass

    except:
        pass

    conn.commit()
    conn.close()
    
    conn = sqlite3.connect("economy.db")
    c = conn.cursor()
    
    try:
        c.execute("""CREATE TABLE economy (
            user_ID text,
            user_name text,
            wallet int,
            bank int,
            net int
        
        )""")

        print("Economy table made")
        
    except:
        pass
    
    conn.commit()
    conn.close()

    
    conn = sqlite3.connect("suggestion.db")
    c = conn.cursor()
    
    try:
        c.execute("""CREATE TABLE set_up (

            guild_ID text,
            aprove_ID int,
            aproved_ID int,
            role_1 text,
            role_2 text
        
        
        )""")

        conn.commit()
        
        print("Suggestions set_up table made")

        c.execute("""CREATE TABLE suggestion (

            suggestion_ID text,
            guild_ID text,
            user_ID text,
            suggestion text
        
        )""")
        
        conn.commit()
        
        print("Suggestions suggestion table made")
        
    except:
        pass

    conn.commit()
    conn.close()

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

#economy commands
@client.command()
@commands.cooldown(1, 300, commands.BucketType.user)
async def work(ctx):
    user_id = ctx.message.author.id
    user_name = ctx.message.author

    number = int(random.randint(5, 25))
    
    conn = sqlite3.connect('economy.db')
    c =conn.cursor()

    c.execute(f"SELECT * FROM economy WHERE user_ID = '{ctx.message.author.id}' LIMIT 1")

    conn.commit()

    items = c.fetchall()

    none = str(items)

    if none == "[]":
        c.execute(f"INSERT INTO economy VALUES ('{ctx.message.author.id}', '{ctx.message.author}', {number} , 0, {number})")

        conn.commit()

        embed: discord.Embed = discord.Embed(
            title="Dinosaur Balance",
            description=f"{ctx.message.author.mention} You got **{number}** Dinosaur Points from working!",
            color=discord.Color.green()
        )

        await ctx.send(embed=embed)

    else:
        for item in items:
            wallet = int(item[2])
            bank = int(item[3])

        sum = wallet + number

        c.execute(f"""UPDATE economy SET wallet = {sum}
                    WHERE user_ID = '{ctx.message.author.id}'   
                """)

        sum_1 = sum

        sum = sum_1 + bank
        
        c.execute(f"""UPDATE economy SET net = {sum}
                    WHERE user_ID = '{ctx.message.author.id}'   
                """)
        
        conn.commit()
        conn.close()
        
        embed: discord.Embed = discord.Embed(
            title="Work",
            description=f"You gained {number} Dinosaur Points form working",
            color=discord.Color.green()
        )

        await ctx.send(embed=embed)
        

token = "token"
client.run(token)
              
    #c.execute("""CREATE TABLE set_up (

        #guild_ID text,
        #aprove_ID int,
        #aproved_ID int,
        #role_1 text,
        #role_2 text
    
    
    #)""")

    #conn.commit()

    #c.execute("""CREATE TABLE suggestion (

        #suggestion_ID text,
        #guild_ID text,
        #user_ID text,
        #suggestion text
    
    #)""")

    #c.execute("""CREATE TABLE economy (
        #user_ID text,
        #user_name text,
        #wallet int,
        #bank int,
        #net int
        
    #)""")

    #c.execute(""" CREATE TABLE common (
        #user_ID text,
        #ammount int
    
        #)""")

    #c.execute(""" CREATE TABLE un_common (
        #user_ID text,
        #ammount int
    
        #)""")

    #c.execute(""" CREATE TABLE rare (
        #user_ID text,
        #ammount int
    
        #)""")