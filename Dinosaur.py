
import discord
import os
from discord.ext import commands
from discord.ext.commands import BucketType
import asyncio
import random
import math
import sqlite3

client = discord.Client()

intents = discord.Intents.default()
intents.members = True

# the bot prefix
client = commands.Bot(command_prefix="d/", case_insensitive=True, intents=intents)
client.remove_command("help")


#Owner ID for owner only command
OwnerID = 638092957756555291

cogs = ["cogs.help", "cogs.games", "cogs.owner", "cogs.economy", "cogs.utility", "cogs.moderation.mod_commands", "cogs.moderation.mod_search", "cogs.moderation.mod_set_up", "cogs.vote"]
#cogs = ["cogs.top"]

# start
@client.event
async def on_ready():
    #conn = sqlite3.connect("economy.db")
    #c = conn.cursor()

    #c.execute("""CREATE TABLE economy (
        #user_ID text,
        #user_name text,
        #wallet int,
        #bank int,
        #net int
        
    #)""")

    #conn.commit()
    #conn.close()

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
        title=f'Joined "{name}"',
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


token = "ODQwMzc1NjgxMDQ1MTAyNjAz.YJXS1w.lvHG0ulfs-DNo_Bklt4OoW0zXX8"
client.run(token)

    #c.execute("ALTER TABLE economy ADD COLUMN net int;")
              
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
        #bank int
        
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