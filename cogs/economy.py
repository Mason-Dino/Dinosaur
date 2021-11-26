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

        embed: discord.Embed = discord.Embed(
            title="Dinosaur Leaderboard",
            description=f"Below are the top 10 people\n\n:first_place: {user_1.name} - {net_1}\n:second_place: {user_2.name} - {net_2}\n:third_place: {user_3.name} - {net_3}\n:medal: {user_4.name} - {net_4}\n:medal: {user_5.name} - {net_5}\n:medal: {user_6.name} - {net_6}\n:medal: {user_7.name} - {net_7}\n:medal: {user_8.name} - {net_8}\n:medal: {user_9.name} - {net_9}\n:medal: {user_10.name} - {net_10}\n",
            color=discord.Color.green()
        )

        await ctx.send(embed=embed)


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
    async def shop(self, ctx):
        conn = sqlite3.connect("shop_items.db")
        c = conn.cursor()
        
        c.execute(f"SELECT rowid, * FROM shop_items WHERE visible='True'")
        
        items = c.fetchall()
        
        embed: discord.Embed = discord.Embed(
            title="Shop",
            description="Bellow is all the stuff you can buy with your Dinosaur Points",
            color=discord.Color.green()
        )
        for item in items:
            id = item[0]
            name = item[1]
            price = item[2]
            option = item[3]
            use = item[4]
            
            if option == "a":
                x = use.split("-")
                
                lower = x[0]
                higher = x[1]
                
                embed.add_field(name=f"**{name}**", value=f"Can get anywhere from {lower} to {higher} Dinosaur Points int the egg.\nPrice - {price}\nID - {id}", inline=False)
                
            elif option == "b":
                embed.add_field(name=f"**{name}**", value=f"You can get {use} Dinosaur Points for selling (using) it.\nPrice - {price}\nID - {id}", inline=False)

        await ctx.send(embed=embed)
        
    @commands.command()
    async def buy(self, ctx, shop_id: str=None, amount = None):
        conn = sqlite3.connect('shop.db')
        conn_econ = sqlite3.connect("economy.db")
        conn_shop_items = sqlite3.connect("shop_items.db")
        
        s = conn.cursor()
        e = conn_econ.cursor()
        i = conn_shop_items.cursor()
        
        i.execute(f"SELECT rowid, * FROM shop_items WHERE rowid='{shop_id}'")
        
        items = i.fetchall()
        
        none = str(items)
        
        if none == "[]":
            await ctx.send("Please send a valid shop ID")
        
        else:
            for item in items:
                id = item[0]
                name = item[1]
                price = item[2]
                option = item[3]
                use = item[4]
                
            e.execute(f"SELECT * FROM economy WHERE user_ID='{ctx.message.author.id}'")
            
            econ = e.fetchall()
            
            none = str(econ)
            
            if none == "[]":
                e.execute(f"INSERT INTO economy VALUES ('{ctx.message.author.id}', '{ctx.message.author}', 0 , 0, 0)")
        
                conn_econ.commit()
                conn_econ.close()
                
                conn.close()
                conn_shop_items.close()
                
                await ctx.send("You do not have enough Dinosaur Points to buy the item.")
                
            else:
                for item in econ:
                    user_ID = item[0]
                    user_name = item[1]
                    wallet = int(item[2])
                    bank = item[3]
                    net = item[4]
                    
                if amount == None:
                    amount = 1
                    await ctx.send("ammount == None")
                    pass
                    
                else:
                    amount_check = amount.isdigit()
                
                    if amount_check == True:
                        amount = int(amount)                
                        if amount == None:
                            await ctx.send("amount == None")
                            amount = 1
                            pass
                        
                        elif amount >= 1:
                            await ctx.send("amount >= 1")
                            amount = amount
                            pass
                         
                        pass
                            
                    else:
                        await ctx.send("Please send a valid amount number")
                        
                s.execute(f"SELECT * FROM items_own WHERE user_id='{ctx.message.author.id}' AND item_name='{name}'")
                
                items = s.fetchall()
                
                await ctx.send(name)
                
                none = str(items)
                
                amount_price = amount * price
                
                print("hi")
                print(amount_price)
                print(wallet)
                
                if wallet >= amount_price:
                    print("hey")
                    if none == "[]":
                        s.execute(f"INSERT INTO items_own VALUES ('{ctx.message.author.id}', '{name}', '{amount}')")
                        
                        conn.commit()
                        conn.close()
                        
                        conn_econ.close()
                        conn_shop_items.close()
                        
                        await ctx.send(f"You successfully bought a **{name}**")
                        
                    else:
                        for item in items:
                            user_ID_items = item[0]
                            name_items = item[1]
                            amount_items = int(item[2])
                            
                        sum = amount_items + amount
                        
                        await ctx.send("hi")
                            
                        s.execute(f"""UPDATE items_own SET amount = {sum}
                                        WHERE user_id = '{ctx.message.author.id}' AND item_name='{name}'   
                                    """)
                        
                        conn.commit()
                        conn.close()
                        
                        new_wallet = wallet - amount_price
                        net = bank + new_wallet
                        
                        await ctx.send(new_wallet)
                        await ctx.send(net)
                        
                        input("is all the info correct?: ")
                        
                        e.execute(f"""UPDATE economy SET wallet = {new_wallet}
                                        WHERE user_ID = '{ctx.message.author.id}'
                                    """)
                        
                        conn_econ.commit()
                        
                        
                        e.execute(f"""UPDATE economy SET net = {net}
                                        WHERE user_ID = '{ctx.message.author.id}'
                                    """)
                        
                        conn_econ.commit()
                        conn_econ.commit()
                        
                        
                        await ctx.send("all worked out")
                    
                elif wallet == amount_price:
                    print("helllow")
                    if none == "[]":
                        s.execute(f"INSERT INTO items_own VALUES ('{ctx.message.author.id}', '{name}', '{amount}')")
                        
                        conn.commit()
                        conn.close()
                        
                        conn_econ.close()
                        conn_shop_items.close()
                        
                        await ctx.send(f"You successfully bought a **{name}**")
                        
                    else:
                        for item in items:
                            user_ID_items = item[0]
                            name_items = item[1]
                            amount_items = int(item[2])
                            
                        sum = amount_items + amount
                        
                        await ctx.send("hi")
                            
                        s.execute(f"""UPDATE items_own SET amount = {sum}
                                        WHERE user_id = '{ctx.message.author.id}' AND item_name='{name}'   
                                    """)
                        
                        conn.commit()
                        conn.close()
                        
                        new_wallet = wallet - amount_price
                        net = bank + new_wallet
                        
                        
                        await ctx.send(new_wallet)
                        await ctx.send(net)
                        
                        input("is all the info correct?: ")
                        
                        e.execute(f"""UPDATE economy SET wallet = {new_wallet}
                                        WHERE user_ID = '{ctx.message.author.id}'
                                    """)
                        
                        conn_econ.commit()
                        
                        
                        e.execute(f"""UPDATE economy SET net = {net}
                                        WHERE user_ID = '{ctx.message.author.id}'
                                    """)
                        
                        conn_econ.commit()
                        conn_econ.commit()
                        
                        
                        await ctx.send("all worked")
                    
                else:
                    await ctx.send("You do not have enough coins in your wallet")

    @commands.command(aliases=['inv'])
    async def inventory(self, ctx):
        conn = sqlite3.connect("shop.db")
        c = conn.cursor()
        
        c.execute(f"SELECT * FROM items_own WHERE user_id = '{ctx.message.author.id}'")
        
        items = c.fetchall()
        
        await ctx.send(items)
        
        sonn = sqlite3.connect("shop_items.db")
        s = sonn.cursor()
        
        s.execute("SELECT rowid, * FROM shop_items ORDER BY rowid DESC LIMIT 1")
        
        shop_items = s.fetchall()
        
        for item in shop_items:
            rowid = int(item[0])
            
        attempts = 0
        max_attempts = rowid
        
        test = ""
        
        print("hey")
        
        IsInvDone = False
        while not IsInvDone:
            
            attempts += 1
            
            if attempts == 1:
                none = str(items)
                
                if none == "[]":
                    embed: discord.Embed = discord.Embed(
                        title="Inventory",
                        description="Nothing to see here.",
                        color=discord.Color.green()
                    )
                    
                    await ctx.send(embed=embed)
                    
                for item in items:
                    name = item[1]
                    amount = item[2]
                    
                    test += f"**{name}** - {amount}\n"
                    
                await ctx.send(test)

                embed: discord.Embed = discord.Embed(
                    title="Inventory",
                    description=f"Below are all the items you have from the shop\n\n{test}",
                    color=discord.Color.green()
                )
            
                await ctx.send(embed=embed)
            
            if attempts == max_attempts:
                return

        
    @commands.command()
    async def use(self, ctx, shop_id: str = None, amount: int = None):
        conn = sqlite3.connect('shop.db')
        conn_econ = sqlite3.connect("economy.db")
        conn_shop_items = sqlite3.connect("shop_items.db")
        
        s = conn.cursor()
        e = conn_econ.cursor()
        i = conn_shop_items.cursor()
        
        i.execute(f"SELECT rowid, * FROM shop_items WHERE rowid='{shop_id}'")
        
        items = i.fetchall()
        
        none = str(items)
        
        if none == "[]":
            await ctx.send("Please send a valid shop ID")
        
        else:
            for item in items:
                id = item[0]
                name = item[1]
                price = item[2]
                option = item[3]
                use = item[4]
                
            e.execute(f"SELECT * FROM economy WHERE user_ID='{ctx.message.author.id}'")
            
            econ = e.fetchall()
            
            none = str(econ)
            
            if none == "[]":
                e.execute(f"INSERT INTO economy VALUES ('{ctx.message.author.id}', '{ctx.message.author}', 0 , 0, 0)")
        
                conn_econ.commit()
                conn_econ.close()
                
                conn.close()
                conn_shop_items.close()
                
                await ctx.send("You do not have enough Dinosaur Points to buy the item.")
                
            else:
                for item in econ:
                    user_ID = item[0]
                    user_name = item[1]
                    wallet = int(item[2])
                    bank = item[3]
                    net = item[4]
                    
                if amount == None:
                    amount = 1
                    print("amount 1")
                    
                    pass
                
                else:               
                    if amount == None:
                        await ctx.send("amount == None")
                        amount = 1
                        pass
                    
                    elif amount >= 1:
                        await ctx.send("amount >= 1")
                        amount = amount
                        pass
                        
                    s.execute(f"SELECT * FROM items_own WHERE user_id='{ctx.message.author.id}' AND item_name='{name}'")
                
                    items = s.fetchall()
                
                    await ctx.send(name)
                
                    none = str(items)
                    
                    if none == "[]":
                        await ctx.send("You do not own any of the item")
                        
                    else:
                        if option == "a":
                            s.execute(f"SELECT * FROM items_own WHERE user_id = '{ctx.message.author.id}' AND item_name ='{name}'")
                            
                            items = s.fetchall()
                            
                            none = str(items)
                            
                            if none == "[]":
                                await ctx.send("You own none of that item") 
                                
                            else:
                                for item in items:
                                    user_id = item[0]
                                    item_name = item[1]
                                    items_own = int(item[2])
                                      
                                sum = items_own - amount
                                
                                if -1 >= sum:
                                    await ctx.send(f"You do not have **{amount}** of {item_name}")
                                    
                                else:
                                    s.execute(f"""UPDATE items_own SET amount = {sum}
                                                    WHERE user_id = '{ctx.message.author.id}' AND item_name='{name}'
                                                """)
                                    
                                    conn.commit()
                                    
                                    x = use.split("-")
                                    
                                    lower = int(x[0])
                                    higher = int(x[1])
                                    
                                    lower_full = lower * amount
                                    higher_full = higher * amount
                                    
                                    number = int(random.randint(lower_full, higher_full))
                                    
                                    print(number)
                                    
                                    sum = wallet + number
                                    
                                    input(f"{sum}:")
                                    
                                    e.execute(f"""UPDATE economy SET wallet = {sum}
                                                    WHERE user_ID = '{ctx.message.author.id}'   
                                                """)
                                    
                                    conn_econ.commit()
                                    
                                    sum = sum + bank
                                    
                                    input(f"{sum}:")
                                    
                                    e.execute(f"""UPDATE economy SET net = {sum}
                                                    WHERE user_ID = '{ctx.message.author.id}'   
                                                """)
                                    
                                    conn_econ.commit()
                                    
                                    embed: discord.Embed = discord.Embed(
                                        title=f"{item_name} Open",
                                        description=f"You earned **{number}** of Dinosaur Points",
                                        color=discord.Color.green()
                                    )

                                    await ctx.send(embed=embed)

    @commands.command()
    async def bal_everyone(self, ctx):
        conn = sqlite3.connect('economy.db')
        c_econ = conn.cursor()

        c_econ.execute(f"SELECT * FROM economy WHERE user_ID = '{ctx.message.author.id}'")

        items = c_econ.fetchall()

        await ctx.send(items)


    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def slots(self, ctx, ammount: int = None):
        conn = sqlite3.connect('economy.db')
        c = conn.cursor()

        c.execute(f"SELECT * FROM economy WHERE user_ID = '{ctx.message.author.id}' LIMIT 1")

        items = c.fetchall()

        none = str(items)

        if none == "[]":
            c.execute(f"INSERT INTO economy VALUES ('{ctx.message.author.id}', '{ctx.message.author}', 0 , 0, 0)")

            conn.commit()
            conn.close()

            return await ctx.send("You do not have any coins to gamble")

        else:
            if ammount == None:
                await ctx.send("Please send the ammount of coins you want to gambel.")

            else:
                for item in items:
                    wallet = item[2]
                    bank = item[3]

                if wallet >= ammount:
                    new_wallet_2 = wallet - ammount

                    embed: discord.Embed = discord.Embed(
                        title="Slots",
                        description="Please wait 5 seconds for the spining to stop",
                        color=discord.Color.green()
                    )

                    before = await ctx.send(embed=embed)

                    responses = [
                        "<:Dinosaur:840670397901045772>"
                        #"<:Dinosaur_Yellow:858747810278670336>",
                        #"<:Dinosaur_Blue:858747768629755934>"
                        
                    ]

                    slots_1 = random.choice(responses)
                    slots_2 = random.choice(responses)
                    slots_3 = random.choice(responses)
                    slots_4 = random.choice(responses)
                    slots_5 = random.choice(responses)
                    slots_6 = random.choice(responses)
                    slots_7 = random.choice(responses)
                    slots_8 = random.choice(responses)
                    slots_9 = random.choice(responses)

                    line_1 = f"{slots_1} | {slots_2} | {slots_3}"
                    line_2 = f"{slots_4} | {slots_5} | {slots_6} :arrow_backward:"
                    line_3 = f"{slots_7} | {slots_8} | {slots_9}"

                    await asyncio.sleep(5)

                    if line_2 == "<:Dinosaur:840670397901045772> | <:Dinosaur:840670397901045772> | <:Dinosaur:840670397901045772> :arrow_backward:":
                        new_ammount = ammount * 3

                        new_wallet = new_wallet_2 + new_ammount

                        c.execute(f"""UPDATE economy SET wallet = {new_wallet}
                            WHERE user_id = '{ctx.message.author.id}'   
                        """)

                        conn.commit()

                        sum = new_wallet + bank

                        c.execute(f"""UPDATE economy SET net = {sum}
                            WHERE user_id = '{ctx.message.author.id}'   
                        """)

                        conn.commit()

                        embed: discord.Embed = discord.Embed(
                            title="Slots",
                            description=f"You Won **{new_ammount}** Dinosaur Points\n\n{line_1}\n{line_2}\n{line_3}",
                            color=discord.Color.green()
                        )
                    
                        conn.close()
                        await before.edit(embed=embed)

                    elif line_2 == "<:Dinosaur_Yellow:858747810278670336> | <:Dinosaur_Yellow:858747810278670336> | <:Dinosaur_Yellow:858747810278670336> :arrow_backward:":
                        new_ammount = ammount * 1.5

                        new_ammount = new_ammount // 1

                        new_wallet = new_wallet_2 + new_ammount

                        c.execute(f"""UPDATE economy SET wallet = {new_wallet}
                            WHERE user_id = '{ctx.message.author.id}'   
                        """)

                        conn.commit()

                        sum = new_wallet + bank

                        c.execute(f"""UPDATE economy SET net = {sum}
                            WHERE user_id = '{ctx.message.author.id}'   
                        """)

                        conn.commit()

                        embed: discord.Embed = discord.Embed(
                            title="Slots",
                            description=f"You Won **{new_ammount:,.0f}** Dinosaur Points\n\n{line_1}\n{line_2}\n{line_3}",
                            color=discord.Color.green()
                        )
                        
                        conn.close()
                        await before.edit(embed=embed)

                    elif line_2 == "<:Dinosaur_Blue:858747768629755934> | <:Dinosaur_Blue:858747768629755934> | <:Dinosaur_Blue:858747768629755934> :arrow_backward:":
                        new_ammount = ammount * 2

                        new_wallet = new_wallet_2 + new_ammount

                        c.execute(f"""UPDATE economy SET wallet = {new_wallet}
                            WHERE user_id = '{ctx.message.author.id}'   
                        """)

                        conn.commit()

                        sum = new_wallet + bank

                        c.execute(f"""UPDATE economy SET net = {sum}
                            WHERE user_id = '{ctx.message.author.id}'   
                        """)

                        conn.commit()

                        embed: discord.Embed = discord.Embed(
                            title="Slots",
                            description=f"You Won **{new_ammount:,.0f}** Dinosaur Points\n\n{line_1}\n{line_2}\n{line_3}",
                            color=discord.Color.green()
                        )
                        
                        conn.close()
                        await before.edit(embed=embed)

                    elif slots_4 == slots_6:
                        if slots_4 == "<:Dinosaur:840670397901045772>":
                            new_ammount = ammount * 1.75

                            new_ammount = new_ammount // 1

                            new_ammount = f"{new_ammount:,.0f}"

                            new_ammount = int(new_ammount)

                            new_wallet = new_wallet_2 + new_ammount

                            c.execute(f"""UPDATE economy SET wallet = {new_wallet}
                                WHERE user_id = '{ctx.message.author.id}'   
                            """)

                            conn.commit()

                            sum = new_wallet + bank

                            c.execute(f"""UPDATE economy SET net = {sum}
                                WHERE user_id = '{ctx.message.author.id}'   
                            """)

                            conn.commit()

                            embed: discord.Embed = discord.Embed(
                                title="Slots",
                                description=f"You Won **{new_ammount:,.0f}** Dinosaur Points\n\n{line_1}\n{line_2}\n{line_3}",
                                color=discord.Color.green()
                            )

                            conn.close()
                            await before.edit(embed=embed)

                        elif slots_4 == "<:Dinosaur_Blue:858747768629755934>":
                            new_ammount = ammount * 1.5

                            new_ammount = new_ammount // 1

                            new_ammount = f"{new_ammount:,.0f}"

                            new_ammount = int(new_ammount)

                            new_wallet = new_wallet_2 + new_ammount

                            c.execute(f"""UPDATE economy SET wallet = {new_wallet}
                                WHERE user_id = '{ctx.message.author.id}'   
                            """)

                            conn.commit()

                            sum = new_wallet + bank

                            c.execute(f"""UPDATE economy SET net = {sum}
                                WHERE user_id = '{ctx.message.author.id}'   
                            """)

                            conn.commit()

                            embed: discord.Embed = discord.Embed(
                                title="Slots",
                                description=f"You Won **{new_ammount:,.0f}** Dinosaur Points\n\n{line_1}\n{line_2}\n{line_3}",
                                color=discord.Color.green()
                            )
                    
                            conn.close()
                            await before.edit(embed=embed)


                        elif slots_4 == "<:Dinosaur_Yellow:858747810278670336>":
                            new_ammount = ammount * 1.25

                            new_ammount = new_ammount // 1

                            new_ammount = int(new_ammount)

                            new_wallet = new_wallet_2 + new_ammount

                            c.execute(f"""UPDATE economy SET wallet = {new_wallet}
                                WHERE user_id = '{ctx.message.author.id}'   
                            """)

                            conn.commit()

                            sum = new_wallet + bank

                            c.execute(f"""UPDATE economy SET net = {sum}
                                WHERE user_id = '{ctx.message.author.id}'   
                            """)

                            conn.commit()

                            embed: discord.Embed = discord.Embed(
                                title="Slots",
                                description=f"You Won **{new_ammount:,.0f}** Dinosaur Points\n\n{line_1}\n{line_2}\n{line_3}",
                                color=discord.Color.green()
                            )
                            
                            conn.close()
                            await before.edit(embed=embed)


                    else:
                        new_wallet = wallet - ammount
                        c.execute(f"""UPDATE economy SET wallet = {new_wallet}
                                WHERE user_id = '{ctx.message.author.id}'   
                            """)
                        
                        conn.commit()

                        sum = new_wallet + bank

                        c.execute(f"""UPDATE economy SET net = {sum}
                                WHERE user_id = '{ctx.message.author.id}'   
                            """)

                        conn.commit()

                        embed: discord.Embed = discord.Embed(
                            title="Slots",
                            description=f"You Lost **{ammount}** Dinosaur Points\n\n{line_1}\n{line_2}\n{line_3}",
                            color=discord.Color.green()
                        )


                        conn.close()
                        await before.edit(embed=embed)


                else:
                    await ctx.send("You do not have enought coins in wallet")

    @commands.command()
    async def rob(self, ctx, user: discord.Member = None):
        conn = sqlite3.connect('economy.db')
        c = conn.cursor()

        if user == None:
            await ctx.send("Please send a user you would like to rob.")

        else:
            c.execute(f"SELECT * FROM economy WHERE user_ID = '{user.id}'")

            items = c.fetchall()

            none = str(items)

            if none == "[]":
                await ctx.send("That use has no money to steal")

            else:
                for item in items:
                    wallet = item[2]
                    bank = item[3]

                


def setup(client):
	client.add_cog(Economy(client))