#----------------------------------------------------------------------#
#
#       leaderboard: -lb, -top
#       Balance: -bal
#       Work: -work
#           Work Error: -work--cool, -work--error
#       Deposit: -dep
#       Withdraw: -with
#       Shop: -shop
#       Buy: -buy
#           Buy Error: -buy--cool, -buy--error
#       Inventory: -inv
#       Use: -use
#       Slots: -slot
#
#----------------------------------------------------------------------#

import discord
import os
from discord.ext import commands
from discord import app_commands
from discord.ext.commands import BucketType
from Disecon import *
import asyncio
import random
import math
import sqlite3

class Economy_Slash(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Leaderboard Command -top, -lb
    @app_commands.command(name="leaderboard", description="lets you see the top 10 people in dinosaur economy")
    async def slash_leaderboard(self, interaction: discord.Interaction):
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
            description=f"Below are the top 10 people\n\n:first_place: {user_1_lb} - {net_1}\n:second_place: {user_2_lb} - {net_2}\n:third_place: {user_3_lb} - {net_3}\n:medal: {user_4_lb} - {net_4}\n:medal: {user_5_lb} - {net_5}\n:medal: {user_6_lb} - {net_6}\n:medal: {user_7_lb} - {net_7}\n:medal: {user_8_lb} - {net_8}\n:medal: {user_9_lb} - {net_9}\n:medal: {user_10_lb} - {net_10}\n",
            color=discord.Color.green()
        )

        await interaction.response.send_message(embed=embed)

    #Balance Command -bal
    @app_commands.command(name="balance", description="It lets you see your current balance")
    async def slash_balance(self, interaction: discord.Interaction):
        view = results.view(user_ID=interaction.user.id)
        
        wallet = view.wallet()
        bank = view.bank()
        
        embed: discord.Embed = discord.Embed(
            title="Dinosaur Balace",
            description=f"{interaction.user.mention} Dinosaur Balance\n\nWallet Amount: **{wallet}**\n\nBank Amount: **{bank}**",
            color=discord.Color.green()
        )
        
        await interaction.response.send_message(embed=embed)

    #Work Command -work
    @app_commands.command(name="work", description="lets you work to earn dinosaur points")
    @app_commands.checks.cooldown(1, 360, key=lambda i: (i.guild_id, i.user.id))
    async def slash_work(self, interaction: discord.Interaction):
        number = int(random.randint(5, 25))
        
        wallet = money.wallet(amount=number, user_ID=interaction.user.id)
        wallet.add()
            
        embed: discord.Embed = discord.Embed(
            title="Work",
            description=f"You gained **{number}** Dinosaur Points form working",
            color=discord.Color.green()
        )

        await interaction.response.send_message(embed=embed)

    #Work Error: -work--cool -work--error
    @slash_work.error
    async def on_work_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):
            await interaction.response.send_message(str(error), ephemeral=True)

    #Deposit Command -dep
    @app_commands.command(name="deposit", description="lets you deposit into the bank")
    async def slash_deposit(self, interaction: discord.Interaction, deposit: str = None):
        view = results.view(user_ID=interaction.user.id)
        
        if deposit == None:
            await interaction.response.send_message("Invalid use of command do **d/dep all** or **d/dep [number]**")
            
        else:
            what_check = deposit.isdigit()
            
            if what_check == True:
                what = int(deposit)
                
                if view.wallet() >= what:
                    wallet = money.wallet(amount=what, user_ID=interaction.user.id)
                    wallet.sub()
                    
                    bank = money.bank(amount=what, user_ID=interaction.user.id)
                    bank.add()
                    
                    embed: discord.Embed = discord.Embed(
                        title="Deposit",
                        description=f"You deposited **{what}** coins into your bank",
                        color=discord.Color.green()
                    )
                    
                    await interaction.response.send_message(embed=embed)
                    
                else:
                    await interaction.response.send_message("You don't have that many coins in your wallet")
                
            if what_check == False:
                all = view.wallet()
                
                wallet = money.wallet(amount=all, user_ID=interaction.user.id)
                wallet.sub()
                
                bank = money.bank(amount=all, user_ID=interaction.user.id)
                bank.add()
                
                embed: discord.Embed = discord.Embed(
                    title="Deposit",
                    description=f"You deposited **{all}** coins into your bank",
                    color=discord.Color.green()
                )
                
                await interaction.response.send_message(embed=embed)
        
    #Withdraw Command -with
    @app_commands.command(name="withdraw", description="lets you withdraw money from the bank")
    async def slash_withdraw(self, interaction: discord.Interaction, withdraw: str = None):
        view = results.view(user_ID=interaction.user.id)
        
        if withdraw == None:
            await interaction.response.send_message("Invalid use of command do **d/with all** or **d/with [number]**")
            
        else:
            what_check = withdraw.isdigit()
            
            if what_check == True:
                what = int(withdraw)
                
                if view.bank() >= what:
                    bank = money.bank(amount=what, user_ID=interaction.user.id)
                    bank.sub()
                    
                    wallet = money.wallet(amount=what, user_ID=interaction.user.id)
                    wallet.add()
                    
                    embed: discord.Embed = discord.Embed(
                        title="Withdraw",
                        description=f"You withdrew **{what}** coins into your wallet",
                        color=discord.Color.green()
                    )
                    
                    await interaction.response.send_message(embed=embed)
                    
                else:
                    await interaction.response.send_message("You don't have that many coins in your bank")
            
            elif what_check == False:
                all = view.bank()
                
                bank = money.bank(amount=all, user_ID=interaction.user.id)
                bank.sub()
                
                wallet = money.wallet(amount=all, user_ID=interaction.user.id)
                wallet.add()
                
                embed: discord.Embed = discord.Embed(
                    title="Withdraw",
                    description=f"You withdrew **{all}** coins into your bank",
                    color=discord.Color.green()
                )
                
                await interaction.response.send_message(embed=embed)

    #Shop Command -shop
    @app_commands.command(name="shop", description="lets you see the items you can buy")
    async def slash_shop(self, interaction: discord.Interaction):
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
                
                embed.add_field(name=f"**{name}**", value=f"Can get anywhere from {lower} to {higher} Dinosaur Points in the egg.\nPrice - {price}\nID - {id}", inline=False)
                
            elif option == "b":
                embed.add_field(name=f"**{name}**", value=f"You can get {use} Dinosaur Points for selling (using) it.\nPrice - {price}\nID - {id}", inline=False)

        await interaction.response.send_message(embed=embed)

    #Buy Command -buy
    @app_commands.command(name="buy", description="lets you buy items from the shop")
    @app_commands.checks.cooldown(1, 300, key=lambda i: (i.guild_id, i.user.id))
    async def slash_buy(self, interaction: discord.Interaction, shop_id: str=None, amount: int = None):
        if amount == None:
            amount = 1
            pass
        
        if 10 >= amount:
            view = results.view(user_ID=interaction.user.id)
            
            conn = sqlite3.connect('shop.db')
            conn_shop_items = sqlite3.connect("shop_items.db")
            
            s = conn.cursor()
            i = conn_shop_items.cursor()
            
            i.execute(f"SELECT rowid, * FROM shop_items WHERE rowid='{shop_id}' AND visible='True'")
            
            items = i.fetchall()
            
            none = str(items)
            
            if none == "[]":
                await interaction.response.send_message("Please send a valid shop ID")
            
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
                        
                s.execute(f"SELECT * FROM items_own WHERE user_id='{interaction.user.id}' AND item_name='{name}'")
                
                items = s.fetchall()
                
                none = str(items)
                
                amount_price = amount * price
                
                wallet = view.wallet()
                bank = view.bank()
                
                if wallet >= amount_price:
                    if none == "[]":
                        s.execute(f"INSERT INTO items_own VALUES ('{interaction.user.id}', '{name}', '{amount}')")
                        
                        conn.commit()
                        conn.close()
                        
                        conn_shop_items.close()
                        
                        wallet = money.wallet(amount=amount_price, user_ID=interaction.user.id)
                        wallet.sub()
                        
                        await interaction.response.send_message(f"You successfully bought a **{name}**")
                        
                    else:
                        for item in items:
                            user_ID_items = item[0]
                            name_items = item[1]
                            amount_items = int(item[2])
                            
                        sum = amount_items + amount
                            
                        s.execute(f"""UPDATE items_own SET amount = {sum}
                                        WHERE user_id = '{interaction.user.id}' AND item_name='{name}'   
                                    """)
                        
                        conn.commit()
                        conn.close()
                        
                        conn_shop_items.close()
                        
                        wallet = money.wallet(amount=amount_price, user_ID=interaction.user.id)
                        wallet.sub()
                        
                        await interaction.response.send_message(f"You successfully bought {amount} of **{name}**")
                        
                elif wallet == amount_price:
                    if none == "[]":
                        s.execute(f"INSERT INTO items_own VALUES ('{interaction.user.id}', '{name}', '{amount}')")
                        
                        conn.commit()
                        conn.close()

                        conn_shop_items.close()
                        
                        wallet = money.wallet(amount=amount_price, user_ID=interaction.user.id)
                        wallet.sub()
                        
                        await interaction.response.send_message(f"You successfully bought a **{name}**")
                        
                    else:
                        for item in items:
                            user_ID_items = item[0]
                            name_items = item[1]
                            amount_items = int(item[2])
                            
                        sum = amount_items + amount
                            
                        s.execute(f"""UPDATE items_own SET amount = {sum}
                                        WHERE user_id = '{interaction.user.id}' AND item_name='{name}'   
                                    """)
                        
                        conn.commit()
                        conn.close()
                        
                        wallet = money.wallet(amount=amount_price, user_ID=interaction.user.id)
                        wallet.sub()
                        
                        await interaction.response.send_message(f"You successfully bought {amount} of **{name}**")
                    
                else:
                    await interaction.response.send_message("You do not have enough coins in your wallet")  

        else: 
            await interaction.response.send_message("You cannot buy more than 10 items", ephemeral=True)

    #Buy Error: -buy--cool, -buy--error
    @slash_buy.error
    async def on_buy_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):
            await interaction.response.send_message(str(error), ephemeral=True)


    #Inventory Command -inv
    @app_commands.command(name="inventory", description="lets you check how many items you own")
    async def slash_inventory(self, interaction: discord.Interaction):
        conn = sqlite3.connect("shop.db")
        c = conn.cursor()
        
        c.execute(f"SELECT * FROM items_own WHERE user_id = '{interaction.user.id}'")
        
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
                    
                    await interaction.response.send_message(embed=embed)
                    
                for item in items:
                    name = item[1]
                    amount = item[2]
                    
                    test += f"**{name}** - {amount}\n"

                embed: discord.Embed = discord.Embed(
                    title="Inventory",
                    description=f"Below are all the items you have from the shop\n\n{test}",
                    color=discord.Color.green()
                )
            
                await interaction.response.send_message(embed=embed)
            
            if attempts == max_attempts:
                return
            
    #Use Command -use
    @app_commands.command(name="use", description="lets you use items you bought in the shop")
    @app_commands.checks.cooldown(1, 300, key=lambda i: (i.guild_id, i.user.id))
    async def slash_use(self, interaction: discord.Interaction, shop_id: str = None, amount: int = None):
        if amount == None:
            amount = 1
            pass
        
        if 10 >= amount:
            view = results.view(user_ID=interaction.user.id)
            
            wallet = view.wallet()
            
            conn = sqlite3.connect('shop.db')
            conn_shop_items = sqlite3.connect("shop_items.db")
            
            s = conn.cursor()
            i = conn_shop_items.cursor()
            
            i.execute(f"SELECT rowid, * FROM shop_items WHERE rowid='{shop_id}'")
            
            items = i.fetchall()
            
            none = str(items)
            
            if none == "[]":
                await interaction.response.send_message("Please send a valid shop ID")
            
            else:
                for item in items:
                    id = item[0]
                    name = item[1]
                    price = item[2]
                    option = item[3]
                    if option == "a":
                        use = item[4]
                        
                    elif option == "b":
                        use = int(item[4])
                    
                if wallet == "0":
                    await interaction.response.send_message("You do not have enough Dinosaur Points to buy the item.")
                    
                else:
                    if amount == None:
                        amount = 1
                        
                        pass
                    
                    else:               
                        if amount == None:
                            amount = 1
                            pass
                        
                        elif amount >= 1:
                            amount = amount
                            pass
                            
                    s.execute(f"SELECT * FROM items_own WHERE user_id='{interaction.user.id}' AND item_name='{name}'")
                
                    items = s.fetchall()            
                    none = str(items)
                    
                    if none == "[]":
                        await interaction.response.send_message("You do not own any of the item")
                        
                    else:
                        if option == "a":
                            s.execute(f"SELECT * FROM items_own WHERE user_id = '{interaction.user.id}' AND item_name ='{name}'")
                            
                            items = s.fetchall()
                            
                            none = str(items)
                            
                            if none == "[]":
                                await interaction.response.send_message("You own none of that item") 
                                
                            else:
                                for item in items:
                                    user_id = item[0]
                                    item_name = item[1]
                                    items_own = int(item[2])
                                        
                                sum = items_own - amount
                                
                                if -1 >= sum:
                                    await interaction.response.send_message(f"You do not have **{amount}** of {item_name}")
                                    
                                else:
                                    s.execute(f"""UPDATE items_own SET amount = {sum}
                                                    WHERE user_id = '{interaction.user.id}' AND item_name='{name}'
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
                                    
                                    wallet = money.wallet(amount=number, user_ID=interaction.user.id)
                                    wallet.add()
                                    
                                    embed: discord.Embed = discord.Embed(
                                        title=f"{item_name} Open",
                                        description=f"You earned **{number}** of Dinosaur Points",
                                        color=discord.Color.green()
                                    )

                                    await interaction.response.send_message(embed=embed)
                                    
                        elif option == "b":
                            s.execute(f"SELECT * FROM items_own WHERE user_id = '{interaction.user.id}' AND item_name ='{name}'")
                            
                            items = s.fetchall()
                            
                            none = str(items)
                            
                            if none == "[]":
                                await interaction.response.send_message("You own none of that item") 
                                
                            else:
                                for item in items:
                                    user_id = item[0]
                                    item_name = item[1]
                                    items_own = int(item[2])
                                        
                                sum = items_own - amount
                                
                                if -1 >= sum:
                                    await interaction.response.send_message(f"You do not have **{amount}** of {item_name}")
                                    
                                else:
                                    s.execute(f"""UPDATE items_own SET amount = {sum}
                                                    WHERE user_id = '{interaction.user.id}' AND item_name='{name}'
                                                """)
                                    
                                    conn.commit()
                                    
                                    number = use * amount
                                    
                                    wallet = money.wallet(amount=number, user_ID=interaction.user.id)
                                    wallet.add()
                                    
                                    embed: discord.Embed = discord.Embed(
                                        title=f"{item_name} Open",
                                        description=f"You earned **{number}** of Dinosaur Points",
                                        color=discord.Color.green()
                                    )
                                    
                                    await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message("You can't use more than 10 at once!")

    @slash_use.error
    async def on_use_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):
            await interaction.response.send_message(str(error), ephemeral=True)

async def setup(client):
	await client.add_cog(Economy_Slash(client))