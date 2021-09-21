import discord
import os
from discord.ext import commands
from discord.ext.commands import BucketType
import asyncio
import random
import math
import sqlite3

class Economy(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def top(self, ctx):
        conn = sqlite3.connect('economy.db')
        c = conn.cursor()

        c.execute("SELECT * FROM economy ORDER BY net DESC LIMIT 1")

        items = c.fetchall()

        none = str(items)

        if none == '[]':
            user_1 = self.client.get_user(840375681045102603)
            user_1.name = "None"
            net_1 = "None"

        else:
            for item in items:
                net_1 = item[4]
                user_ID_1 = int(item[0])

                user_1 = self.client.get_user(user_ID_1)
                
                print("1")
                
                pass

        c.execute("SELECT * FROM economy ORDER BY net DESC LIMIT 1 OFFSET 1")

        items = c.fetchall()

        none = str(items)

        if none == '[]':
            user_2 = self.client.get_user(840375681045102603)
            user_2.name = "None"
            net_2 = "None"

        else:
            for item in items:
                net_2 = item[4]
                user_ID_2 = int(item[0])

                user_2 = self.client.get_user(user_ID_2)

                print("2")

                pass

        c.execute("SELECT * FROM economy ORDER BY net DESC LIMIT 1 OFFSET 2")

        items = c.fetchall()

        none = str(items)

        if none == '[]':
            user_3 = self.client.get_user(840375681045102603)

            user_3.name = "None 1"
            net_3 = "None"

        else:
            for item in items:
                net_3 = item[4]
                user_ID_3 = int(item[0])

                user_3 = self.client.get_user(user_ID_3)
                
                print("3")
                
                pass

        c.execute("SELECT * FROM economy ORDER BY net DESC LIMIT 1 OFFSET 3")

        items = c.fetchall()

        none = str(items)

        if none == '[]':
            user_4 = self.client.get_user(840375681045102603)
            user_4.name = "None"
            net_4 = "None"

        else:
            for item in items:
                net_4 = item[4]
                user_ID_4 = int(item[0])

                user_4 = self.client.get_user(user_ID_4)
                
                print("4")
                
                pass

        c.execute("SELECT * FROM economy ORDER BY net DESC LIMIT 1 OFFSET 4")

        items = c.fetchall()

        none = str(items)

        if none == '[]':
            user_5 = self.client.get_user(840375681045102603)
            user_5.name = "None"
            net_5 = "None"

        else:
            for item in items:
                net_5 = item[4]
                user_ID_5 = int(item[0])

                user_5 = self.client.get_user(user_ID_5)
                
                print("5")
                
                pass

        c.execute("SELECT * FROM economy ORDER BY net DESC LIMIT 1 OFFSET 5")

        items = c.fetchall()

        none = str(items)

        if none == '[]':
            user_6 = self.client.get_user(840375681045102603)
            user_6.name = "None"
            net_6 = "None"

        else:
            for item in items:
                net_6 = item[4]
                user_ID_6 = int(item[0])

                user_6 = self.client.get_user(user_ID_6)
                
                print("6")
                
                pass

        c.execute("SELECT * FROM economy ORDER BY net DESC LIMIT 1 OFFSET 6")

        items = c.fetchall()

        none = str(items)

        if none == '[]':
            user_7 = self.client.get_user(840375681045102603)
            user_7.name = "None"
            net_7 = "None"

        else:
            for item in items:
                net_7 = item[4]
                user_ID_7 = int(item[0])

                user_7 = self.client.get_user(user_ID_7)
                
                print("7")
                
                pass

        c.execute("SELECT * FROM economy ORDER BY net DESC LIMIT 1 OFFSET 7")

        items = c.fetchall()

        none = str(items)

        if none == '[]':
            user_8 = self.client.get_user(840375681045102603)
            user_8.name = "None"
            net_8 = "None"

        else:
            for item in items:
                net_8 = item[4]
                user_ID_8 = int(item[0])

                user_8 = self.client.get_user(user_ID_8)
                
                print("8")

                pass

        c.execute("SELECT * FROM economy ORDER BY net DESC LIMIT 1 OFFSET 8")

        items = c.fetchall()

        none = str(items)

        if none == '[]':
            user_9 = self.client.get_user(840375681045102603)
            user_9.name = "None"
            net_9 = "None"

        else:
            for item in items:
                net_9 = item[4]
                user_ID_9 = int(item[0])

                user_9 = self.client.get_user(user_ID_9)
                
                print("9")
                
                pass

        c.execute("SELECT * FROM economy ORDER BY net DESC LIMIT 1 OFFSET 9")

        items = c.fetchall()

        none = str(items)

        if none == '[]':
            user_10 = self.client.get_user(840375681045102603)
            user_10.name = "None"
            net_10 = "None"

        else:
            for item in items:
                net_10 = item[4]
                user_ID_10 = int(item[0])

                user_10 = self.client.get_user(user_ID_10)
                
                print("10")
                
                pass
            
        if user_1 == None:
            user_1_lb = user_ID_1
            
        else:
            user_1_lb = user_1.name
            pass
            
        if user_2 == None:
            user_2_lb = user_ID_2
            pass
            
        else:
            user_2_lb = user_2.name
            pass
        
        if user_3 == None:
            user_3_lb = user_ID_3
            pass
            
        else:
            user_3_lb = user_3.name
            pass
        
        if user_4 == None:
            user_4_lb = user_ID_4
            pass
            
        else:
            user_4_lb = user_4.name
            pass
        
        if user_5 == None:
            user_5_lb = user_ID_5
            pass
            
        else:
            user_5_lb = user_5.name
            pass
        
        if user_6 == None:
            user_6_lb = user_ID_6
            pass
            
        else:
            user_6_lb = user_6.name
            pass
        
        if user_7 == None:
            user_7_lb = user_ID_7
            pass
            
        else:
            user_7_lb = user_7.name
            pass
        
        if user_8 == None:
            user_8_lb = user_ID_8
            pass
            
        else:
            user_8_lb = user_8.name
            pass
        
        if user_9 == None:
            user_9_lb = user_ID_9
            pass
            
        else:
            user_9_lb = user_9.name
            pass
            
        if user_10 == None:
            user_10_lb = user_ID_10
            pass
            
        else:
            user_10_lb = user_10.name
            pass
            
        
            
        embed: discord.Embed = discord.Embed(
            title="Dinosaur Leaderboard",
            description=f"Bellow are the top 10 people\n\n:first_place: {user_1_lb} - {net_1}\n:second_place: {user_2_lb} - {net_2}\n:third_place: {user_3_lb} - {net_3}\n:medal: {user_4_lb} - {net_4}\n:medal: {user_5_lb} - {net_5}\n:medal: {user_6_lb} - {net_6}\n:medal: {user_7_lb} - {net_7}\n:medal: {user_8_lb} - {net_8}\n:medal: {user_9_lb} - {net_9}\n:medal: {user_10_lb} - {net_10}\n",
            color=discord.Color.green()
        )

        await ctx.send(embed=embed)
        
    @commands.command()
    async def lb(self, ctx):
        conn = sqlite3.connect("economy.db")
        c = conn.cursor()
        
        c.execute("SELECT * FROM economy ORDER BY net DESC LIMIT 10")


    @commands.command(aliases=['bal'])
    async def balance(self, ctx):
        conn = sqlite3.connect('economy.db')
        c = conn.cursor()

        c.execute(f"SELECT * FROM economy WHERE user_ID = '{ctx.message.author.id}'")

        items = c.fetchall()

        none = str(items)

        if none == "[]":
            c.execute(f"INSERT INTO economy VALUES ('{ctx.message.author.id}', '{ctx.message.author}', 0 , 0, 0)")

            conn.commit()

            embed: discord.Embed = discord.Embed(
                title="Dinosaur Balance",
                description=f"{ctx.message.author.mention} Dinosaur Balance\n\nWallet Amount: **0**\n\nBank Amount: **0**",
                color=discord.Color.green()
            )

            await ctx.send(embed=embed)

        else:
            for item in items:
                wallet = item[2]
                bank = item[3]

            embed: discord.Embed = discord.Embed(
                title="Dinosaur Balance",
                description=f"{ctx.message.author.mention} Dinosaur Balance\n\nWallet Amount: **{wallet}**\n\nBank Ammount: **{bank}**",
                color=discord.Color.green()
            )

            await ctx.send(embed=embed)

    @commands.command(aliases=['dep'])
    async def deposit(self, ctx, arg1=None, *, ammount: int=None):
        conn = sqlite3.connect('economy.db')
        c = conn.cursor()

        c.execute(f"SELECT * FROM economy WHERE user_ID = '{ctx.message.author.id}'")

        items = c.fetchall()

        none = str(items)

        if none == "[]":
            c.execute(f"INSERT INTO economy VALUES ('{ctx.message.author.id}', '{ctx.message.author}', 0 , 0, 0)")

            conn.commit()
            conn.close()

            await ctx.send("You don't have any coins to deposti")

        else:
            for item in items:
                wallet = item[2]
                bank = item[3]

            if arg1 == "all":
                sum = wallet + bank

                c.execute(f"""UPDATE economy SET bank = {sum}
                    WHERE user_ID = '{ctx.message.author.id}'   
                """)

                conn.commit()

                c.execute(f"""UPDATE economy SET wallet = 0
                    WHERE user_ID = '{ctx.message.author.id}'   
                """)

                conn.commit()

                embed: discord.Embed = discord.Embed(
                    title="Deposit",
                    description=f"You deposited **{wallet}** into your bank",
                    color=discord.Color.green()
                )

                await ctx.send(embed=embed)

            elif arg1=="set":
                if ammount == None:
                    await ctx.send("Please send the amount of Dinosaur Points you want to deposite")

                else:
                    if wallet >= ammount:
                        new_wallet = wallet - ammount

                        new_bank = bank + ammount

                        c.execute(f"""UPDATE economy SET wallet = {new_wallet}
                                WHERE user_ID = '{ctx.message.author.id}'   
                            """)

                        conn.commit()

                        c.execute(f"""UPDATE economy SET bank = {new_bank}
                                WHERE user_ID = '{ctx.message.author.id}'   
                            """)

                        conn.commit()

                        embed: discord.Embed = discord.Embed(
                            title="Deposit",
                            description=f"You deposited **{ammount}** into your bank",
                            color=discord.Color.green()
                        )

                        await ctx.send(embed=embed)

                    else:
                        await ctx.send("Please only send the ammount of Dinosaur Points you have in your wallet")

    @commands.command(aliases=['with'])
    async def withdraw(self, ctx, arg1=None, *, ammount: int=None):
        conn = sqlite3.connect('economy.db')
        c = conn.cursor()

        c.execute(f"SELECT * FROM economy WHERE user_ID = '{ctx.message.author.id}'")

        items = c.fetchall()

        none = str(items)

        if none == "[]":
            c.execute(f"INSERT INTO economy VALUES ('{ctx.message.author.id}', '{ctx.message.author}', 0 , 0, 0)")

            conn.commit()
            conn.close()

            await ctx.send("You don't have any coins to withdraw.")

        else:
            for item in items:
                wallet = int(item[2])
                bank = int(item[3])

            if arg1 == "all":
                sum = wallet + bank

                c.execute(f"""UPDATE economy SET wallet = {sum}
                    WHERE user_ID = '{ctx.message.author.id}'   
                """)

                conn.commit()

                c.execute(f"""UPDATE economy SET bank = 0
                    WHERE user_ID = '{ctx.message.author.id}'   
                """)

                conn.commit()

                embed: discord.Embed = discord.Embed(
                    title="Deposit",
                    description=f"You withdrew **{bank}** from your bank",
                    color=discord.Color.green()
                )

                await ctx.send(embed=embed)

            elif arg1=="set":
                if ammount == None:
                    await ctx.send("Please send the amount of Dinosaur Points you want to withdraw")

                else:
                    if bank >= ammount:
                        new_bank = bank - ammount

                        new_wallet = wallet + ammount

                        c.execute(f"""UPDATE economy SET wallet = {new_wallet}
                                WHERE user_ID = '{ctx.message.author.id}'   
                            """)

                        conn.commit()

                        c.execute(f"""UPDATE economy SET bank = {new_bank}
                                WHERE user_ID = '{ctx.message.author.id}'   
                            """)

                        conn.commit()

                        embed: discord.Embed = discord.Embed(
                            title="Deposit",
                            description=f"You withdrew **{ammount}** from your bank",
                            color=discord.Color.green()
                        )

                        await ctx.send(embed=embed)

                    else:
                        await ctx.send("Please only send the ammount of Dinosaur Points you have in your bank")

    @commands.command()
    async def shop(self, ctx, arg1=None, buyID: str=None):
        embed: discord.Embed = discord.Embed(
            title="Shop",
            description="Bellow is all the stuff you can buy with your Dinosaur Points",
            color=discord.Color.green()
        )
        embed.add_field(name="**Common Mystery Egg**", value="Can get anywhere from 5 to 25 Dinosaur Points in the egg.\nPrice - 10 Dinosaur Points\nID - 1", inline=False)
        embed.add_field(name="**Un-Common Mystery Egg**", value="Can get anywhere from 10 to 50 Dinosaur Points in the egg.\nPrice - 20 Dinosaur Points\nID - 2", inline=False)
        embed.add_field(name="**Rare Mystery Egg**", value="Can get anywhere from 80 to 130 Dinosaur Points in the egg.\nPrice - 100 Dinosaur Points\nID - 3", inline=False)

        await ctx.send(embed=embed)

    @commands.command()
    async def buy(self, ctx, *, message=None):
        conn = sqlite3.connect('shop.db')
        conn_econ = sqlite3.connect('economy.db')
        c = conn.cursor()
        c_econ = conn_econ.cursor()

        if message == None:
            await ctx.send("Please send the name or the ID of the item you would like to buy.")

        elif message.lower() in "1 or common mystery egg":
            c_econ.execute(f"SELECT * FROM economy WHERE user_ID = '{ctx.message.author.id}' LIMIT 1")

            items = c_econ.fetchall()

            none = str(items)

            if none == "[]":
                c_econ.execute(f"INSERT INTO economy VALUES ('{ctx.message.author.id}', '{ctx.message.author}', 0 , 0, 0)")

                conn_econ.commit()
                conn_econ.close()

                await ctx.send("You do not have enough Dinosaur Points to buy the **Common Mystery Egg**")

            else:
                for item  in items:
                    wallet = int(item[2])
                    bank = int(item[3])

                if wallet >= 10:
                    new_wallet = wallet - 10

                    c_econ.execute(f"""UPDATE economy SET wallet = {new_wallet}
                        WHERE user_ID = '{ctx.message.author.id}'   
                    """)

                    conn_econ.commit()

                    sum = new_wallet + bank

                    c_econ.execute(f"""UPDATE economy SET net = {sum}
                        WHERE user_ID = '{ctx.message.author.id}'   
                    """)

                    conn_econ.commit()

                    c.execute(f"SELECT * FROM common WHERE user_ID = '{ctx.message.author.id}' LIMIT 1")

                    items = c.fetchall()

                    none = str(items)

                    if none == "[]":
                        c.execute(f"INSERT INTO common VALUES ('{ctx.message.author.id}', 1)")

                        conn.commit()

                        await ctx.send("You successfully bought a **Common Mystry Egg**")

                    else:
                        for item in items:
                            ammount = int(item[1])

                        new_ammount = ammount + 1

                        c.execute(f"""UPDATE common SET ammount = {new_ammount}
                            WHERE user_id = '{ctx.message.author.id}'   
                        """)

                        conn.commit()
                

                        await ctx.send("You successfully bought a **Common Mystry Egg**")

                else:
                    await ctx.send("You do not have enough Dinosaur Points to buy the **Common Mystery Egg**")

        elif message.lower() in "2 or un-common mystery egg or un common mystery egg":
            c_econ.execute(f"SELECT * FROM economy WHERE user_ID = '{ctx.message.author.id}' LIMIT 1")

            items = c_econ.fetchall()

            none = str(items)

            if none == "[]":
                c_econ.execute(f"INSERT INTO economy VALUES ('{ctx.message.author.id}', '{ctx.message.author}', 0 , 0, 0)")

                conn_econ.commit()
                conn_econ.close()

                await ctx.send("You do not have enough Dinosaur Points to buy the **Un-Common Mystery Egg**")

            else:
                for item  in items:
                    wallet = int(item[2])
                    bank = item[3]

                if wallet >= 20:
                    new_wallet = wallet - 20

                    c_econ.execute(f"""UPDATE economy SET wallet = {new_wallet}
                        WHERE user_ID = '{ctx.message.author.id}'   
                    """)

                    conn_econ.commit()

                    sum = new_wallet + bank

                    c_econ.execute(f"""UPDATE economy SET net = {sum}
                        WHERE user_ID = '{ctx.message.author.id}'   
                    """)

                    conn_econ.commit()

                    c.execute(f"SELECT * FROM un_common WHERE user_ID = '{ctx.message.author.id}' LIMIT 1")

                    items = c.fetchall()

                    none = str(items)

                    if none == "[]":
                        c.execute(f"INSERT INTO un_common VALUES ('{ctx.message.author.id}', 1)")

                        conn.commit()

                        await ctx.send("You successfully bought a **Un-Common Mystry Egg**")

                    else:
                        for item in items:
                            ammount = int(item[1])

                        new_ammount = ammount + 1

                        c.execute(f"""UPDATE un_common SET ammount = {new_ammount}
                            WHERE user_id = '{ctx.message.author.id}'   
                        """)

                        conn.commit()
                

                        await ctx.send("You successfully bought a **Un-Common Mystry Egg**")

                else:
                    await ctx.send("You do not have enough Dinosaur Points to buy the **Un-Common Mystery Egg**")

        elif message.lower() in "3 or rare mystery egg":
            c_econ.execute(f"SELECT * FROM economy WHERE user_ID = '{ctx.message.author.id}' LIMIT 1")

            items = c_econ.fetchall()

            none = str(items)

            if none == "[]":
                c_econ.execute(f"INSERT INTO economy VALUES ('{ctx.message.author.id}', '{ctx.message.author}', 0 , 0, 0)")

                conn_econ.commit()
                conn_econ.close()

                await ctx.send("You do not have enough Dinosaur Points to buy the **Rare Mystery Egg**")

            else:
                for item  in items:
                    wallet = int(item[2])
                    bank = item[3]

                if wallet >= 100:
                    new_wallet = wallet - 100

                    c_econ.execute(f"""UPDATE economy SET wallet = {new_wallet}
                        WHERE user_ID = '{ctx.message.author.id}'   
                    """)

                    conn_econ.commit()

                    sum = new_wallet + bank

                    c_econ.execute(f"""UPDATE economy SET net = {sum}
                        WHERE user_ID = '{ctx.message.author.id}'   
                    """)

                    conn_econ.commit()

                    c.execute(f"SELECT * FROM rare WHERE user_ID = '{ctx.message.author.id}' LIMIT 1")

                    items = c.fetchall()

                    none = str(items)

                    if none == "[]":
                        c.execute(f"INSERT INTO rare VALUES ('{ctx.message.author.id}', 1)")

                        conn.commit()

                        await ctx.send("You successfully bought a **Rare Mystry Egg**")

                    else:
                        for item in items:
                            ammount = int(item[1])

                        new_ammount = ammount + 1

                        c.execute(f"""UPDATE rare SET ammount = {new_ammount}
                            WHERE user_id = '{ctx.message.author.id}'   
                        """)

                        conn.commit()
                

                        await ctx.send("You successfully bought a **Rare Mystry Egg**")

                else:
                    await ctx.send("You do not have enough Dinosaur Points to buy the **Rare Mystery Egg**")

    @commands.command(aliases=['inv'])
    async def inventory(self, ctx):
        conn = sqlite3.connect('shop.db')
        c = conn.cursor()

        c.execute(f"SELECT * FROM rare WHERE user_ID = '{ctx.message.author.id}' LIMIT 1")

        items = c.fetchall()

        none = str(items)

        if none == "[]":
            rare = "0"
            pass

        else:
            for item in items:
                rare = int(item[1])
                pass

        c.execute(f"SELECT * FROM un_common WHERE user_ID = '{ctx.message.author.id}' LIMIT 1")

        items = c.fetchall()

        none = str(items)

        if none == "[]":
            un_common = "0"
            pass

        else:
            for item in items:
                un_common = int(item[1])
                pass

        c.execute(f"SELECT * FROM common WHERE user_ID = '{ctx.message.author.id}' LIMIT 1")

        items = c.fetchall()

        none = str(items)

        if none == "[]":
            common = "0"
            pass

        else:
            for item in items:
                common = int(item[1])
                pass

        conn.commit()
        conn.close()

        embed: discord.Embed = discord.Embed(
            title="Inventory",
            description=f"Bellow are all the items you have from the shop\n\n**Common Mystery Egg** - {common}\n**Un-Comon Mystery Egg** - {un_common}\n**Rare Mystery Egg** - {rare}",
            color=discord.Color.green()
        )

        await ctx.send(embed=embed)

    @commands.command()
    async def use(self, ctx, *, message=None):
        conn = sqlite3.connect('shop.db')
        conn_econ = sqlite3.connect('economy.db')

        c = conn.cursor()
        c_econ = conn_econ.cursor()

        if message == None:
            await ctx.send("Please send the ID or the name of the item you would like to use.")

        elif message.lower() in "1 or common mystery egg":
            c.execute(f"SELECT * FROM common WHERE user_ID = '{ctx.message.author.id}' LIMIT 1")

            items = c.fetchall()

            none = str(items)

            if none == "[]":
                await ctx.send("You do not have a **Common Mystery Egg** in your inentory")

            else:
                for item in items:
                    ammount = item[1]

                if ammount == 0:
                    await ctx.send("You do not have a **Common Mystery Egg** in your inentory")
                    
                else:
                    new_ammount = ammount - 1

                    c.execute(f"""UPDATE common SET ammount = {new_ammount}
                                WHERE user_id = '{ctx.message.author.id}'   
                    """)

                    conn.commit()

                    number = int(random.randint(5, 25))

                    c_econ.execute(f"SELECT * FROM economy WHERE user_ID = '{ctx.message.author.id}'")

                    items = c_econ.fetchall()

                    none = str(items)

                    if none == "[]":
                        c_econ.execute(f"INSERT INTO economy VALUES ('{ctx.message.author.id}', '{ctx.message.author}', 0 , 0, 0)")

                        conn_econ.commit()
                        conn_econ.close()

                        await ctx.send("You do not have a **Common Mystery Egg** in your inentory")
                        
                    else:
                        for item in items:
                            wallet = item[2]
                            bank = item[3]

                        new_wallet = wallet + number

                        c_econ.execute(f"""UPDATE economy SET wallet = {new_wallet}
                            WHERE user_id = '{ctx.message.author.id}'   
                        """)

                        conn_econ.commit()

                        sum = bank + new_wallet

                        c_econ.execute(f"""UPDATE economy SET net = {sum}
                            WHERE user_id = '{ctx.message.author.id}'   
                        """)

                        conn_econ.commit()

                        conn_econ.close()

                        embed: discord.Embed = discord.Embed(
                            title="Common Mystery Egg Open",
                            description=f"You earned **{number}** Dinosaur Points from a Common Mystery Egg",
                            color=discord.Color.green()
                        )

                        await ctx.send(embed=embed)

        elif message.lower() in "2 or un-common mystery egg or un common mystery egg":
            c.execute(f"SELECT * FROM un_common WHERE user_ID = '{ctx.message.author.id}' LIMIT 1")

            items = c.fetchall()

            none = str(items)

            if none == "[]":
                await ctx.send("You do not have a **Un-Common Mystery Egg** in your inentory")

            else:
                for item in items:
                    ammount = item[1]

                if ammount == 0:
                    await ctx.send("You do not have a **Un-Common Mystery Egg** in your inentory")
                    
                else:
                    new_ammount = ammount - 1

                    c.execute(f"""UPDATE un_common SET ammount = {new_ammount}
                                WHERE user_id = '{ctx.message.author.id}'   
                    """)

                    conn.commit()

                    number = int(random.randint(10, 50))

                    c_econ.execute(f"SELECT * FROM economy WHERE user_ID = '{ctx.message.author.id}'")

                    items = c_econ.fetchall()

                    none = str(items)

                    if none == "[]":
                        c_econ.execute(f"INSERT INTO economy VALUES ('{ctx.message.author.id}', '{ctx.message.author}', 0 , 0, 0)")

                        conn_econ.commit()
                        conn_econ.close()

                        await ctx.send("You do not have a **Common Mystery Egg** in your inentory")
                        
                    else:
                        for item in items:
                            wallet = item[2]
                            bank = item[3]

                        new_wallet = wallet + number

                        c_econ.execute(f"""UPDATE economy SET wallet = {new_wallet}
                            WHERE user_id = '{ctx.message.author.id}'   
                        """)

                        conn_econ.commit()

                        sum = bank + new_wallet

                        c_econ.execute(f"""UPDATE economy SET net = {sum}
                            WHERE user_id = '{ctx.message.author.id}'   
                        """)

                        conn_econ.commit()
                        conn_econ.close()

                        embed: discord.Embed = discord.Embed(
                            title="Un-Common Mystery Egg Open",
                            description=f"You earned **{number}** Dinosaur Points from a Un-Common Mystery Egg",
                            color=discord.Color.green()
                        )

                        await ctx.send(embed=embed)
                
        elif message.lower() in "3 or rare mystery egg":
            c.execute(f"SELECT * FROM rare WHERE user_ID = '{ctx.message.author.id}' LIMIT 1")

            items = c.fetchall()

            none = str(items)

            if none == "[]":
                await ctx.send("You do not have a **Rare Mystery Egg** in your inentory")

            else:
                for item in items:
                    ammount = item[1]

                if ammount == 0:
                    await ctx.send("You do not have a **Rare Mystery Egg** in your inentory")
                    
                else:
                    new_ammount = ammount - 1

                    c.execute(f"""UPDATE rare SET ammount = {new_ammount}
                                WHERE user_id = '{ctx.message.author.id}'   
                    """)

                    conn.commit()

                    number = int(random.randint(80, 130))

                    c_econ.execute(f"SELECT * FROM economy WHERE user_ID = '{ctx.message.author.id}'")

                    items = c_econ.fetchall()

                    none = str(items)

                    if none == "[]":
                        c_econ.execute(f"INSERT INTO economy VALUES ('{ctx.message.author.id}', '{ctx.message.author}', 0 , 0, 0)")

                        conn_econ.commit()
                        conn_econ.close()

                        await ctx.send("You do not have a **Rare Mystery Egg** in your inentory")
                        
                    else:
                        for item in items:
                            wallet = item[2]
                            bank = item[3]

                        new_wallet = wallet + number

                        c_econ.execute(f"""UPDATE economy SET wallet = {new_wallet}
                            WHERE user_id = '{ctx.message.author.id}'   
                        """)

                        conn_econ.commit()

                        sum = bank + new_wallet

                        c_econ.execute(f"""UPDATE economy SET net = {sum}
                            WHERE user_id = '{ctx.message.author.id}'   
                        """)

                        conn_econ.commit()

                        conn_econ.close()

                        embed: discord.Embed = discord.Embed(
                            title="Rare Mystery Egg Open",
                            description=f"You earned **{number}** Dinosaur Points from a Rare Mystery Egg",
                            color=discord.Color.green()
                        )

                        await ctx.send(embed=embed)


def setup(client):
	client.add_cog(Economy(client))