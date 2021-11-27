import discord
import os
from discord.ext import commands
from discord.ext.commands import BucketType
from Disecon import *
import asyncio
import random
import math
import sqlite3

class Economy(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def top_test(self, ctx):
        top_1 = results.top(place=1)
        top_2 = results.top(place=2)
        top_3 = results.top(place=3)
        top_4 = results.top(place=4)
        top_5 = results.top(place=5)
        top_6 = results.top(place=6)
        top_7 = results.top(place=7)
        top_8 = results.top(place=8)
        top_9 = results.top(place=9)
        top_10 = results.top(place=10)
        
        user_1 = self.client.get_user(top_1.user_ID())
        user_2 = self.client.get_user(top_2.user_ID())
        user_3 = self.client.get_user(top_3.user_ID())
        user_4 = self.client.get_user(top_4.user_ID())
        user_5 = self.client.get_user(top_5.user_ID())
        user_6 = self.client.get_user(top_6.user_ID())
        user_7 = self.client.get_user(top_7.user_ID())
        user_8 = self.client.get_user(top_8.user_ID())
        user_9 = self.client.get_user(top_9.user_ID())
        user_10 = self.client.get_user(top_10.user_ID())
        
        if user_1 == None:
            user_1_lb = top_1.user_ID()
            
        else:
            user_1_lb = user_1.name
            pass
            
        if user_2 == None:
            user_2_lb = top_2.user_ID()
            pass
            
        else:
            user_2_lb = user_2.name
            pass
        
        if user_3 == None:
            user_3_lb = top_3.user_ID()
            pass
            
        else:
            user_3_lb = user_3.name
            pass
        
        if user_4 == None:
            user_4_lb = top_4.user_ID()
            pass
            
        else:
            user_4_lb = user_4.name
            pass
        
        if user_5 == None:
            user_5_lb = top_5.user_ID()
            pass
            
        else:
            user_5_lb = user_5.name
            pass
        
        if user_6 == None:
            user_6_lb = top_6.user_ID()
            pass
            
        else:
            user_6_lb = user_6.name
            pass
        
        if user_7 == None:
            user_7_lb = top_7.user_ID()
            pass
            
        else:
            user_7_lb = user_7.name
            pass
        
        if user_8 == None:
            user_8_lb = top_8.user_ID()
            pass
            
        else:
            user_8_lb = user_8.name
            pass
        
        if user_9 == None:
            user_9_lb = top_9.user_ID()
            pass
            
        else:
            user_9_lb = user_9.name
            pass
            
        if user_10 == None:
            user_10_lb = top_10.user_ID()
            pass
            
        else:
            user_10_lb = user_10.name
            pass
        
        net_1 = top_1.net()
        net_2 = top_2.net()
        net_3 = top_3.net()
        net_4 = top_4.net()
        net_5 = top_5.net()
        net_6 = top_6.net()
        net_7 = top_7.net()
        net_8 = top_8.net()
        net_9 = top_9.net()
        net_10 = top_10.net()
        
        embed: discord.Embed = discord.Embed(
            title="Dinosaur Leaderboard",
            description=f"Bellow are the top 10 people\n\n:first_place: {user_1_lb} - {net_1}\n:second_place: {user_2_lb} - {net_2}\n:third_place: {user_3_lb} - {net_3}\n:medal: {user_4_lb} - {net_4}\n:medal: {user_5_lb} - {net_5}\n:medal: {user_6_lb} - {net_6}\n:medal: {user_7_lb} - {net_7}\n:medal: {user_8_lb} - {net_8}\n:medal: {user_9_lb} - {net_9}\n:medal: {user_10_lb} - {net_10}\n",
            color=discord.Color.green()
        )

        await ctx.send(embed=embed)

    
    @commands.command(aliases=['bal'])
    async def balance(self, ctx):
        view = results.view(user_ID=ctx.message.author.id)
        
        wallet = view.wallet()
        bank = view.bank()
        
        embed: discord.Embed = discord.Embed(
            title="Dinosaur Balace",
            description=f"{ctx.message.author.mention} Dinosaur Balance\n\nWallet Amount: **{wallet}**\n\nBank Amount: **{bank}**",
            color=discord.Color.green()
        )
        
        await ctx.send(embed=embed)
        
        

    @commands.command(aliases=['dep'])
    async def deposit(self, ctx, what: str = None):
        view = results.view(user_ID=ctx.message.author.id)
        
        if what == None:
            await ctx.send("Invalid use of command do **d/dep all** or **d/dep [number]**")
            
        else:
            what_check = what.isdigit()
            
            if what_check == True:
                what = int(what)
                
                if view.wallet() >= what:
                    wallet = money.wallet(amount=what, user_ID=ctx.message.author.id)
                    wallet.sub()
                    
                    bank = money.bank(amount=what, user_ID=ctx.message.author.id)
                    bank.add()
                    
                    embed: discord.Embed = discord.Embed(
                        title="Deposit",
                        description=f"You deposited **{what}** coins into your bank",
                        color=discord.Color.green()
                    )
                    
                    await ctx.send(embed=embed)
                    
                else:
                    await ctx.send("You don't have that many coins in your wallet")
                
            if what_check == False:
                all = view.wallet()
                
                wallet = money.wallet(amount=all, user_ID=ctx.message.author.id)
                wallet.sub()
                
                bank = money.bank(amount=all, user_ID=ctx.message.author.id)
                bank.add()
                
                embed: discord.Embed = discord.Embed(
                    title="Deposit",
                    description=f"You deposited **{all}** coins into your bank",
                    color=discord.Color.green()
                )
                
                await ctx.send(embed=embed)
        

    @commands.command(aliases=['with'])
    async def withdraw(self, ctx, what: str = None):
        view = results.view(user_ID=ctx.message.author.id)
        
        if what == None:
            await ctx.send("Invalid use of command do **d/with all** or **d/with [number]**")
            
        else:
            what_check = what.isdigit()
            
            if what_check == True:
                what = int(what)
                
                if view.bank() >= what:
                    bank = money.bank(amount=what, user_ID=ctx.message.author.id)
                    bank.sub()
                    
                    wallet = money.wallet(amount=what, user_ID=ctx.message.author.id)
                    wallet.add()
                    
                    embed: discord.Embed = discord.Embed(
                        title="Withdraw",
                        description=f"You withdrew **{what}** coins into your wallet",
                        color=discord.Color.green()
                    )
                    
                    await ctx.send(embed=embed)
                    
                else:
                    await ctx.send("You don't have that many coins in your bank")
            
            elif what_check == False:
                all = view.bank()
                
                bank = money.bank(amount=all, user_ID=ctx.message.author.id)
                bank.sub()
                
                wallet = money.wallet(amount=all, user_ID=ctx.message.author.id)
                wallet.add()
                
                embed: discord.Embed = discord.Embed(
                    title="Withdraw",
                    description=f"You withdrew **{all}** coins into your bank",
                    color=discord.Color.green()
                )
                
                await ctx.send(embed=embed)

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
        view = results.view(user_ID=ctx.message.author.id)
        
        conn = sqlite3.connect('shop.db')
        conn_shop_items = sqlite3.connect("shop_items.db")
        
        s = conn.cursor()
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
                
            if amount == None:
                amount = 1
                
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
            
            none = str(items)
            
            amount_price = amount * price
            
            wallet = view.wallet()
            bank = view.bank()
            
            if wallet >= amount_price:
                if none == "[]":
                    s.execute(f"INSERT INTO items_own VALUES ('{ctx.message.author.id}', '{name}', '{amount}')")
                    
                    conn.commit()
                    conn.close()
                    
                    conn_shop_items.close()
                    
                    wallet = money.wallet(amount=amount_price, user_ID=ctx.message.author.id)
                    wallet.sub()
                    
                    await ctx.send(f"You successfully bought a **{name}**")
                    
                else:
                    for item in items:
                        user_ID_items = item[0]
                        name_items = item[1]
                        amount_items = int(item[2])
                        
                    sum = amount_items + amount
                        
                    s.execute(f"""UPDATE items_own SET amount = {sum}
                                    WHERE user_id = '{ctx.message.author.id}' AND item_name='{name}'   
                                """)
                    
                    conn.commit()
                    conn.close()
                    
                    conn_shop_items.close()
                    
                    wallet = money.wallet(amount=amount_price, user_ID=ctx.message.author.id)
                    wallet.sub()
                    
                    await ctx.send("all worked out 1")
                    
            elif wallet == amount_price:
                if none == "[]":
                    s.execute(f"INSERT INTO items_own VALUES ('{ctx.message.author.id}', '{name}', '{amount}')")
                    
                    conn.commit()
                    conn.close()

                    conn_shop_items.close()
                    
                    wallet = money.wallet(amount=amount_price, user_ID=ctx.message.author.id)
                    wallet.sub()
                    
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
                    
                    wallet = money.wallet(amount=amount_price, user_ID=ctx.message.author.id)
                    wallet.sub()
                    
                    
                    await ctx.send("all worked 2")
                
            else:
                await ctx.send("You do not have enough coins in your wallet")      

    @commands.command(aliases=['inv'])
    async def inventory(self, ctx):
        conn = sqlite3.connect("shop.db")
        c = conn.cursor()
        
        c.execute(f"SELECT * FROM items_own WHERE user_id = '{ctx.message.author.id}'")
        
        items = c.fetchall()
        
        sonn = sqlite3.connect("shop_items.db")
        s = sonn.cursor()
        
        s.execute("SELECT rowid, * FROM shop_items ORDER BY rowid DESC LIMIT 1")
        
        shop_items = s.fetchall()
        
        for item in shop_items:
            rowid = int(item[0])
            
        attempts = 0
        max_attempts = rowid
        
        test = ""
        
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