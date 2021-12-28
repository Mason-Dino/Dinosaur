import discord
import os
from discord.ext import commands
from discord.ext import tasks
from discord.ext.commands import BucketType
from dislash import *
from Disecon import *
import asyncio
import random
import math
import sqlite3
import topgg


client = discord.Client()

intents = discord.Intents.default()
intents.members = True

# the bot prefix
client = commands.Bot(command_prefix="d/", case_insensitive=True, intents=intents)
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
    #conn = sqlite3.connect("economy_old.db")
    #c = conn.cursor()

    #c.execute("SELECT * FROM economy")
    #items = c.fetchall()
    
    #print(items)

    #for item in items:
        #user_id = int(item[0])
        #wallet = int(item[2])
        #bank  = int(item[3])
        #net = int(item[4])
        
        #type(user_id)
        
        #conn = sqlite3.connect("economy.db")
        #c = conn.cursor()
        
        #c.execute(f"INSERT INTO economy VALUES ({user_id}, {wallet}, {bank}, {net})")
        
        #conn.commit()
        #conn.close()

        #conn_e = sqlite3.connect("economy.db")
        #ce = conn_e.cursor()
        
        #ce.execute("SELECT * FROM economy")
        #items = ce.fetchall()
        
        #print(items)
    
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

client.topgg_webhook = topgg.WebhookManager(client).dbl_webhook("/dblwebhook", "password")
client.topgg_webhook.run(5000)

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

@tasks.loop(hours=24)
async def check_data():
    x = datetime.datetime.now()
    m_d_y = x.strftime("%x")

    date = m_d_y.split("/")

    m = date[0]
    d = date[1]
    y = date[2]

    if d == "1":
        votechannel = client.get_channel(861773377742831656)

        conn = sqlite3.connect("vote.db")
        c = conn.cursor()

        c.execute("SELECT * FROM vote ORDER BY votes DESC LIMIT 1 OFFSET 0")

        items_1 = c.fetchall()
        none_1 = str(items_1)

        c.execute("SELECT * FROM vote ORDER BY votes DESC LIMIT 1 OFFSET 1")

        items_2 = c.fetchall()
        none_2 = str(items_2)

        c.execute("SELECT * FROM vote ORDER BY votes DESC LIMIT 1 OFFSET 2")

        items_3 = c.fetchall()
        none_3 = str(items_3)

        c.execute("SELECT * FROM vote ORDER BY votes DESC LIMIT 1 OFFSET 3")

        items_4 = c.fetchall()
        none_4 = str(items_4)

        c.execute("SELECT * FROM vote ORDER BY votes DESC LIMIT 1 OFFSET 4")

        items_5 = c.fetchall()
        none_5 = str(items_5)

        c.execute("SELECT * FROM vote ORDER BY votes DESC LIMIT 1 OFFSET 5")

        items_6 = c.fetchall()
        none_6 = str(items_6)

        c.execute("SELECT * FROM vote ORDER BY votes DESC LIMIT 1 OFFSET 6")

        items_7 = c.fetchall()
        none_7 = str(items_7)

        c.execute("SELECT * FROM vote ORDER BY votes DESC LIMIT 1 OFFSET 7")

        items_8 = c.fetchall()
        none_8 = str(items_8)

        c.execute("SELECT * FROM vote ORDER BY votes DESC LIMIT 1 OFFSET 8")

        items_9 = c.fetchall()
        none_9 = str(items_9)

        c.execute("SELECT * FROM vote ORDER BY votes DESC LIMIT 1 OFFSET 9")

        items_10 = c.fetchall()
        none_10 = str(items_10)

        if none_1 == "[]":
            user_1 = "Unavailable"
            votes_1 = 0

        else:
            for item_1 in items_1:
                user_1_id = int(item_1[0])
                vote_1 = int(item_1[1])

            user_1 = client.get_user(user_1_id)

            if user_1 == None:
                user_1 = user_1_id

            else:
                user_1 = user_1.name

        if none_2 == "[]":
            user_2 = "Unavailable"
            vote_2 = 0

        else:
            for item in items_2:
                user_2_id = int(item[0])
                vote_2 = int(item[1])

            user_2 = client.get_user(user_2_id)

            if user_2 == None:
                user_2 = user_2_id

            else:
                user_2 = user_2.name

        if none_3 == "[]":
            user_3 = "Unavailable"
            vote_3 = 0

        else:
            for item in items_3:
                user_3_id = int(item[0])
                vote_3 = int(item[1])

            user_3 = client.get_user(user_3_id)

            if user_3 == None:
                user_3 = user_3_id

            else:
                user_3 = user_3.name

        if none_4 == "[]":
            user_4 = "Unavailable"
            vote_4 = 0

        else:
            for item in items_4:
                user_4_id = int(item[0])
                vote_4 = int(item[1])

            user_4 = client.get_user(user_4_id)

            if user_4 == None:
                user_4 = user_4_id

            else:
                user_4 = user_4.name

        if none_5 == "[]":
            user_5 = "Unavailable"
            vote_5 = 0

        else:
            for item in items_5:
                user_5_id = int(item[0])
                vote_5 = int(item[1])

            user_5 = client.get_user(user_5_id)

            if user_5 == None:
                user_5 = user_5_id

            else:
                user_5 = user_5.name

        if none_6 == "[]":
            user_6 = "Unavailable"
            vote_6 = 0

        else:
            for item in items_6:
                user_6_id = int(item[0])
                vote_6 = int(item[1])

            user_6 = client.get_user(user_6_id)

            if user_6 == None:
                user_6 = user_6_id

            else:
                user_6 = user_6.name

        if none_7 == "[]":
            user_7 = "Unavailable"
            vote_7 = 0

        else:
            for item in items_7:
                user_7_id = int(item[0])
                vote_7 = int(item[1])

            user_7 = client.get_user(user_7_id)

            if user_7 == None:
                user_7 = user_7_id

            else:
                user_7 = user_7.name

        if none_8 == "[]":
            user_8 = "Unavailable"
            vote_8 = 0

        else:
            for item in items_8:
                user_8_id = int(item[0])
                vote_8 = int(item[1])

            user_8 = client.get_user(user_8_id)

            if user_8 == None:
                user_8 = user_8_id

            else:
                user_8 = user_8.name

        if none_9 == "[]":
            user_9 = "Unavailable"
            vote_9 = 0

        else:
            for item in items_9:
                user_9_id = int(item[0])
                vote_9 = int(item[1])

            user_9 = client.get_user(user_9_id)

            if user_9 == None:
                user_9 = user_9_id

            else:
                user_9 = user_9.name

        if none_10 == "[]":
            user_10 = "Unavailable"
            vote_10 = 0

        else:
            for item in items_10:
                user_10_id = int(item[0])
                vote_10 = int(item[1])

            user_10 = client.get_user(user_10_id)

            if user_10 == None:
                user_10 = user_10_id

            else:
                user_10 = user_10.name

        embed: discord.Embed = discord.Embed(
            title="Vote Leaderboard",
            description=f"Bellow are the top 10 people\n\n:first_place: {user_1} - {vote_1}\n:second_place: {user_2} - {vote_2}\n:third_place: {user_3} - {vote_3}\n:medal: {user_4} - {vote_4}\n:medal: {user_5} - {vote_5}\n:medal: {user_6} - {vote_6}\n:medal: {user_7} - {vote_7}\n:medal: {user_8} - {vote_8}\n:medal: {user_9} - {vote_9}\n:medal: {user_10} - {vote_10}\n",
            color=discord.Color.green()
        )

        conn = sqlite3.connect("vote.db")
        c = conn.cursor()

        c.execute("SELECT * FROM vote")

        items = c.fetchall()
        none = str(items)

        if none == "[]":
            pass
    
        else:
            for item in items:
                user_id = int(item[0])
                votes = int(item[1])

                c.execute(f"""UPDATE vote SET votes=0
                            WHERE user_ID={user_id}
                """)

                conn.commit()

            conn.close()

        await votechannel.send(embed=embed)

    else    :
        votechannel = client.get_channel(858437766479609876)

        await votechannel.send(f"Did not do task today as it is not the first of the month!\n\nCurrect Date - {m_d_y}")
    
@check_data.before_loop
async def before_some_task():
    await client.wait_until_ready()

#economy commands
@client.command()
@commands.cooldown(1, 300, commands.BucketType.user)
async def work(ctx):
    number = int(random.randint(5, 25))
    
    wallet = money.wallet(amount=number, user_ID=ctx.message.author.id)
    wallet.add()
        
    embed: discord.Embed = discord.Embed(
        title="Work",
        description=f"You gained **{number}** Dinosaur Points form working",
        color=discord.Color.green()
    )

    await ctx.send(embed=embed)
        

token = "BOT_TOKEN"
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