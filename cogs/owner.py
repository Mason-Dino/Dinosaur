#----------------------------------------------------------------------#
#
#       Owner Help: -help, -owner
#       New Command: -new
#       Money: -money
#       Balset: -bset
#       Invedit: -invedit
#       Items: -items
#           New: -items--new
#           Update: -items--update
#           View: -items--view
#           All: -items--add
#
#----------------------------------------------------------------------#

import discord
import os
from discord.ext import commands
from discord.ext.commands import BucketType
import asyncio
import random
import math
import sqlite3
from Disecon import *

class Owner(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Owner Help command -help -owner
    @commands.command()
    async def owner(self, ctx):

        OwnerID = 638092957756555291

        if ctx.message.author.id == OwnerID:
            embed: discord.Embed = discord.Embed(
                title="Owner Only Commands",
                description="Bellow are all the owner commands",
                color=discord.Color.green()
            )
            embed.add_field(name="new", value="d/new command")
            embed.add_field(name="money", value="d/money [user] [type] [amount] [place]")
            embed.add_field(name="balset", value="d/balset [User]")
            embed.add_field(name="Invedit", value="d/invedit [User] [Shop ID] [Add or Remove] [Amount]")
            embed.add_field(name="items new", value="d/items new")
            embed.add_field(name="items update", value="d/items update [shop ID] [price, visible, or use]")
            embed.add_field(name="items view", value="d/items view [shop ID]")
            embed.add_field(name="items all", value="d/items all")
            embed.add_field(name="sync", value="d/sync**")
            embed.add_field(name="reload cog", value="d/reload [cog]")

            await ctx.send(embed=embed)

        else:
            await ctx.send('You are not allowed to execute this command!')


    #New Command Command
    @commands.command()
    async def new(self, ctx, arg1=None):
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        OwnerID = 638092957756555291

        if ctx.message.author.id == OwnerID:
            if arg1 == "command":
                embed: discord.Embed = discord.Embed(
                    title="Command Name",
                    description="Please send the name of the new command",
                    color=discord.Color.green()
                )

                await ctx.send(embed=embed)

                msg = await self.client.wait_for("message", check=check)
                name = msg.content

                if msg.content == "stop":
                    await ctx.send("You have stoped the command.")

                else:
                    embed: discord.Embed = discord.Embed(
                        title="Command Aliases",
                        description="Please send the aliases of the new command",
                        color=discord.Color.green()
                    )

                    await ctx.send(embed=embed)

                    msg = await self.client.wait_for("message", check=check)
                    aliases = msg.content

                    if msg.content == "stop":
                        await ctx.send("You have stoped the command.")

                    else:
                        embed: discord.Embed = discord.Embed(
                            title="Command Usage",
                            description="Please send the usage of the new command",
                            color=discord.Color.green()
                        )

                        await ctx.send(embed=embed)

                        msg = await self.client.wait_for("message", check=check)
                        usage = msg.content

                        if msg.content == "stop":
                            await ctx.send("You have stoped the command.")

                        else:
                            embed: discord.Embed = discord.Embed(
                                title="Command Description",
                                description="Please send the command description",
                                color=discord.Color.green()
                            )

                            await ctx.send(embed=embed)

                            msg = await self.client.wait_for("message", check=check)
                            des = msg.content

                            if msg.content == "stop":
                                await ctx.send("You have stoped the command.")

                            else:
                                embed: discord.Embed = discord.Embed(
                                    title="New Command",
                                    description="Bellow is everything you did above for the new command",
                                    color=discord.Color.green()
                                )
                                embed.add_field(name="Command Name", value=f"```{name}```", inline=False)
                                embed.add_field(name="Command Aliases", value=f"```{aliases}```", inline=False)
                                embed.add_field(name="Command Usage", value=f"```{usage}```", inline=False)
                                embed.add_field(name="Command Description",  value=f"```{des}```", inline=False)
                                embed.add_field(name="Move On", value="If all the infomation looks good say **send**\nIf all the infomation does not look good say **no**")

                                await ctx.send(embed=embed)

                                msg = await self.client.wait_for("message", check=check)

                                if msg.content == "send":
                                    change = self.client.get_channel(841021318693650462)

                                    embed: discord.Embed = discord.Embed(
                                        title="New Command!",
                                        color=discord.Color.green()
                                    )
                                    embed.add_field(name="Command Name:", value=f"```{name}```", inline=False)
                                    embed.add_field(name="Command Aliases:", value=f"```{aliases}```", inline=False)
                                    embed.add_field(name="Command Usage", value=f"```{usage}```", inline=False)
                                    embed.add_field(name="Command Description",  value=f"```{des}```", inline=False)

                                    await change.send(embed=embed)


        else:
            await ctx.send("You do not have permission to use this command.")

    #Money Command -money
    @commands.command()
    async def money(self, ctx,user: discord.Member, type:str = None, amount: str=None, place: str = None):
        OwnerId = 638092957756555291
        
        if OwnerId == ctx.message.author.id:
            if type.lower() == "add":
                amount_check = amount.isdigit()
                
                if amount_check == True:
                    amount = int(amount)
                    if place.lower() == "wallet": 
                        wallet = money.wallet(amount=amount, user_ID=user.id)
                        wallet.add()
                
                        embed: discord.Embed = discord.Embed(
                            title="Add Money",
                            description=f"{user.mention} has had {amount} added to wallet",
                            color=discord.Color.green()
                        )

                        await ctx.send(embed=embed)
                        
                    elif place.lower() == "bank":
                        bank = money.bank(amount=amount, user_ID=user.id)
                        bank.add()
                        
                        embed: discord.Embed = discord.Embed(
                            title="Add Money",
                            description=f"{user.mention} has had {amount} added to bank",
                            color=discord.Color.green()
                        )

                        await ctx.send(embed=embed)
                    
                else:
                    await ctx.send("Please send a valid number")
                
            elif type.lower() == "remove":
                amount_check = amount.isdigit()
                
                if amount_check == True:
                    amount = int(amount)
                    
                    if place.lower() == "wallet":
                        wallet = money.wallet(amount=amount, user_ID=user.id)
                        wallet.sub()
                        
                        embed: discord.Embed = discord.Embed(
                            title="Money Removed",
                            description=f"{user.mention} has had {amount} removed from wallet",
                            color=discord.Color.green()
                        )
                        
                        await ctx.send(embed=embed)
                        
                    elif place.lower() == "bank":
                        bank = money.bank(amount=amount, user_ID=user.id)
                        bank.sub()
                        
                        embed: discord.Embed = discord.Embed(
                            title="Money Removed",
                            description=f"{user.mention} has had {amount} removed from bank",
                            color=discord.Color.green()
                        )
                        
                        await ctx.send(embed=embed)
                            
                else:
                    if amount.lower() == "all":
                        view = results.view(user_ID=user.id)
                        
                        wallet = int(view.wallet())
                        bank = int(view.bank())
                        
                        wallet = money.wallet(amount=wallet, user_ID=user.id)
                        wallet.sub()
                        
                        bank = money.bank(amount=bank, user_ID=user.id)
                        bank.sub()
                        
                        embed: discord.Embed = discord.Embed(
                            title="Remove Money",
                            description=f"Removed all money from {user.mention}",
                            color=discord.Color.green()
                        )
                        
                        await ctx.send(embed=embed)
                        
                    else:
                        await ctx.send("Money command failed")

        else:
            await ctx.send("You do not have permssion to use this command.")

    #BalSet Command -bset
    @commands.command()
    async def balset(self, ctx, user: discord.Member = None):
        OwnerID = 638092957756555291

        if OwnerID == ctx.author.id:
            conn = sqlite3.connect("economy.db")
            c = conn.cursor()

            view = results.view(user_ID=user.id)

            userNewBal = view.bank() + view.wallet()
            net = view.net()

            if userNewBal == view.net():
                await ctx.send(f"`{user.id}` was all good!")

            else:
                wallet = money.wallet(amount=view.wallet(), user_ID=user.id)
                bank = money.bank(amount=view.bank(), user_ID=user.id)

                wallet.sub()
                bank.sub()

                wallet = money.wallet(amount=net, user_ID=user.id)
                wallet.add()

                await ctx.send(f"`{user.id}` was not good, {net} is now their new balance.")

        else:
            await ctx.send("You do not have permission to use this command.")
            

    #Invedit Command -invedit
    @commands.command()
    async def invedit(self, ctx, user: discord.Member, shopID: int, ar: str, amount: int):
        OwnerID = 638092957756555291

        if OwnerID == ctx.author.id:
            conn = sqlite3.connect("shop.db")
            connS = sqlite3.connect("shop_items.db")

            c = conn.cursor()
            s = connS.cursor()

            s.execute(f"SELECT rowid, * FROM shop_items WHERE rowid='{shopID}'")
            
            items = s.fetchall()
            
            none = str(items)
            
            if none == "[]":
                await ctx.send("Please send a valid shop ID")

            else:
                for item in items:
                    id = item[0]
                    name = item[1]

                c.execute(f"SELECT * FROM items_own WHERE item_name='{name}' AND user_id='{user.id}'")

                if ar.lower() == "add":
                    items = c.fetchall()

                    none = str(items)

                    if none == "[]":
                        c.execute(f"INSERT INTO items_own VALUES ('{ctx.message.author.id}', '{name}', {amount})")

                        conn.commit()
                        conn.close()

                        embed: discord.Embed = discord.Embed(
                            title="Inventory Add",
                            description=f"{user.mention} has gotton {amount} {name}",
                            color=discord.Color.green()
                        )

                        await ctx.send(embed=embed)
                        
                    else:
                        for item in items:
                            amountDB = int(item[2])

                        sum = amountDB + amount

                        print(sum)

                        c.execute(f"""UPDATE items_own SET amount = {sum}
                                        WHERE user_id = '{user.id}' AND item_name='{name}'   
                                    """)

                        conn.commit()
                        conn.close()

                        embed: discord.Embed = discord.Embed(
                            title="Inventory Add",
                            description=f"{user.mention} has gotton {amount} {name} added",
                            color=discord.Color.green()
                        )

                        await ctx.send(embed=embed)

                elif ar.lower() == "remove":
                    items = c.fetchall()

                    none = str(items)

                    if none == "[]":
                        await ctx.send(f"They have nothing of {name} to be removed")

                    else:
                        for item in items:
                            amountDB = int(item[2])

                        sum = amountDB - amount

                        c.execute(f"""UPDATE items_own SET amount = {sum}
                                        WHERE user_id = '{user.id}' AND item_name='{name}'   
                                    """)

                        conn.commit()
                        conn.close()

                        embed: discord.Embed = discord.Embed(
                            title="Inventory Remove",
                            description=f"{user.mention} has gotton {amount} {name} removed",
                            color=discord.Color.green()
                        )

                        await ctx.send(embed=embed)


                else:
                    await ctx.send("Try command again")

        else:
            await ctx.send("You are not allowed to use this command")

    #Items Command Group -items 
    @commands.group()
    async def items(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("Invalid sub command")

    #Items New Command -items--new
    @items.command()
    async def new(self, ctx):
        conn = sqlite3.connect("shop_items.db")
        c = conn.cursor()
        
        OwnerID = 638092957756555291
        
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel
        
        if ctx.message.author.id == OwnerID:
            embed: discord.Embed = discord.Embed(
                title="Shop Item Add",
                description="Say **Yes** to add a shop item\nSay **No** to not add a shop item",
                color=discord.Color.green()
            )
            
            await ctx.send(embed=embed)
            
            msg = await self.client.wait_for("message", check=check)
            
            if msg.content.lower() == "yes":
                embed: discord.Embed = discord.Embed(
                    title="Name",
                    description="What is the name of the shop item you want?",
                    color=discord.Color.green()
                )
                
                await ctx.send(embed=embed)
                
                msg = await self.client.wait_for("message", check=check)
                name = msg.content
                
                if msg.content.lower() == "stop":
                    conn.close()
                    
                    await ctx.send("The shop item add process has been stoped")
                    
                else:
                    embed: discord.Embed = discord.Embed(
                        title="Price",
                        description="What is the price that you the item to be?",
                        color=discord.Color.green()
                    )
                    
                    await ctx.send(embed=embed)
                    
                    msg = await self.client.wait_for("message", check=check)
                    price = msg.content
                    
                    if msg.content.lower() == "stop":
                        conn.close()
                        
                        await ctx.send("The shop item add process has been stoped")
                        
                    else:
                        embed: discord.Embed = discord.Embed(
                            title="Option",
                            description="What is the option you want it to be?\n\n**a** - Mystery Crate / Egg\n**b** - Collectible",
                            color=discord.Color.green()
                        )
                        
                        await ctx.send(embed=embed)
                        
                        msg = await self.client.wait_for("message", check=check)
                        option = msg.content
                        
                        if msg.content.lower() == "stop":
                            conn.close()
                            
                            await ctx.send("The shop item add process has been stoped")
                            
                        else:
                            embed: discord.Embed = discord.Embed(
                                title="Use",
                                description="What is the ammount of coins you want them to gain",
                                color=discord.Color.green()
                            )
                            
                            await ctx.send(embed=embed)
                            
                            msg = await self.client.wait_for("message", check=check)
                            use = msg.content
                            
                            if msg.content == "stop":
                                conn.close()
                                
                                await ctx.send("The shop item add process has been stoped")
                                
                            else:
                                embed: discord.Embed = discord.Embed(
                                    title="Visible",
                                    description="Do you want people to able do to see it while doing `d/shop`?\n\n**Yes** for it to be visible for `d/shop`\n**No** for it not to be visible for `d/shop`",
                                    color=discord.Color.green()
                                )
                                
                                await ctx.send(embed=embed)
                                
                                msg = await self.client.wait_for("message", check=check)
                                visible = msg.content
                                
                                if msg.content == "stop":
                                    conn.close()
                                    
                                    await ctx.send("The shop item add process has been stoped")
                                    
                                else:
                                    if msg.content.lower() == "yes":
                                        visible = "True"
                                        pass
                                    
                                    elif msg.content.lower() == "no":
                                        visible = "False"
                                        pass
                                    
                                    else:
                                        visible = "False"
                                        pass
                                    
                                    embed: discord.Embed = discord.Embed(
                                        title="Shop Item Add",
                                        description=f"Item Name - {name}\nItem Price - {price}\nOption - {option}\nUse - {use}\nVisible - {visible}\n\nSay **Add** to add it to the shop\nSay **No** to not add it to the shop",
                                        color=discord.Color.green()
                                    )
                                    
                                    await ctx.send(embed=embed)
                                    
                                    msg = await self.client.wait_for("message", check=check)
                                    
                                    if msg.content.lower() == "add":
                                        c.execute(f"INSERT INTO shop_items VALUES ('{name}', '{price}', '{option}', '{use}', '{visible}')")
                                        
                                        conn.commit()
                                        conn.close()
                                        
                                        embed: discord.Embed = discord.Embed(
                                            title="Shop Item Added",
                                            description=f"Item Name - {name}\nItem Price - {price}\nOption - {option}\nUse - {use}\nVisible - {visible}",
                                            color=discord.Color.green()
                                        )
                                    
                                        await ctx.send(embed=embed)
                                        
                                    else:
                                        await ctx.send(f"The item was not added to the shop")
                
            else:
                conn.close()
                
                await ctx.send("The shop item add process has been stoped")
            
        else:
            conn.close()
            
            await ctx.send("You do not have permssion to use this command.")

    #Items Update Command -items--update
    @items.command()
    async def update(self, ctx, shop: int = None, arg1=None):
        conn = sqlite3.connect("shop_items.db")
        c = conn.cursor()
        
        OwnerID = 638092957756555291
        
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel
        
        if ctx.message.author.id == OwnerID:
            if shop == None:
                await ctx.send("Invalid Shop ID")
                
            elif arg1 == None:
                await ctx.send("No item update identify")
                
            elif shop == None and arg1 == None:
                await ctx.send("Invalid Shop ID and No item update identify")
                
            else:
                c.execute(f"SELECT rowid, * FROM shop_items WHERE rowid={shop}")
                
                items = c.fetchall()
                none = str(items)
                
                if none == "[]":
                    await ctx.send("Not a valid shop ID")
                    
                else:
                    if arg1.lower() == "price":
                        embed: discord.Embed = discord.Embed(
                            title="Price Update",
                            description="Please send the updated price for the item.\n\nSend **No** if you would not like to update the price",
                            color=discord.Color.green()
                        )
                        
                        await ctx.send(embed=embed)
                        
                        msg = await self.client.wait_for("message", check=check)
                        
                        if msg.content.lower() == "no":
                            await ctx.send("The price update was stoped")
                            
                        else:
                            price = msg.content
                            
                            price_check = price.isdigit()
                            
                            if price_check == True:
                                price = int(price)
                                
                                c.execute(f"""UPDATE shop_items SET price = {price}
                                                WHERE rowid = {shop}
                                            """)
                                
                                conn.commit()
                                conn.close()
                                
                                await ctx.send("The price is updated")
                                
                            else:
                                await ctx.send("Please redo the command and then send a valid number")
                    
                    elif arg1.lower() == "visible":
                        embed: discord.Embed = discord.Embed(
                            title="Visible Update",
                            description="Send **True** to have it be able to be viewed in shop\nSend **False** to have it not appear on the shop\n\nSend **No** if you would like to stop updating the visibility",
                            color=discord.Color.green()
                        )
                        
                        await ctx.send(embed=embed)
                        
                        msg = await self.client.wait_for("message", check=check)
                        
                        if msg.content.lower() == "no":
                            await ctx.send("Stoped updating visibility")
                            
                        elif msg.content.lower() == "true":
                            c.execute(f"""UPDATE shop_items SET visible = "True"
                                                WHERE rowid = {shop}
                                            """)
                            
                            conn.commit()
                            conn.close()
                            
                            await ctx.send("Visibility updated to **True**")
                            
                        elif msg.content.lower() == "false":
                            c.execute(f"""UPDATE shop_items SET visible = "False"
                                                WHERE rowid = {shop}
                                            """)
                            
                            conn.commit()
                            conn.close()
                            
                            await ctx.send("Visibility updated to **False**")
                            
                        else:
                            await ctx.send("Not valid visibility response")
                    
                    elif arg1.lower() == "use":
                        c.execute(f"SELECT rowid, * FROM shop_items WHERE rowid={shop}")
                        
                        items = c.fetchall()
                        none = str(items)
                        
                        if none == "[]":
                            await ctx.send("Process Failed please redo")
                            
                        else:
                            for item in items:
                                option = item[3]
                                
                            if option == "a":
                                embed: discord.Embed = discord.Embed(
                                    title="Use Update",
                                    description=f"Please send **x-x** where x is a number\n\nSend **No** if you would like to stop updating the use",
                                    color=discord.Color.green()
                                )
                                
                                await ctx.send(embed=embed)
                                
                                msg = await self.client.wait_for("message", check=check)
                                
                                if msg.content.lower() == "no":
                                    await ctx.send("Use updating process stoped")
                                    
                                else:
                                    use = msg.content
                                    
                                    c.execute(f"""UPDATE shop_items SET use = {use}
                                                WHERE rowid = {shop}
                                            """)
                                    
                                    conn.commit()
                                    conn.close()
                                    
                                    await ctx.send("Use Updating process complete")
                                    
                            elif option == "b":
                                embed: discord.Embed = discord.Embed(
                                    title="Use Update",
                                    description="Please send **x** where x is a number\n\nSend **No** if you would like to stop updating the use",
                                    color=discord.Color.green()
                                )
                                
                                await ctx.send(embed=embed)
                                
                                msg = await self.client.wait_for("message", check=check)
                                
                                if msg.content.lower() == "no":
                                    await ctx.send("Use updating process stoped")
                                    
                                else:
                                    use = msg.content
                                    
                                    c.execute(f"""UPDATE shop_items SET use = {use}
                                                WHERE rowid = {shop}
                                            """)
                                    
                                    conn.commit()
                                    conn.close()
                                    
                                    await ctx.send("Use Updating process complete")
        
        else:
            await ctx.send("Not a valid owner ID")

    #Items All Command -items--all
    @items.command()
    async def all(self, ctx):
        conn = sqlite3.connect("shop_items.db")
        c = conn.cursor()

        OwnerID = 638092957756555291

        if ctx.message.author.id == OwnerID:
            c.execute(f"SELECT rowid, * FROM shop_items")
                
            items = c.fetchall()

            embed: discord.Embed = discord.Embed(
                title="Shop Items",
                description="Below are all the shop items",
                color=discord.Color.green()
            )

            for item in items:
                embed.add_field(name=f"{item[1]}", value=f"RowID - {item[0]}\nVisible - {item[5]}", inline=False)

            await ctx.send(embed=embed)


    #Items View Command -items--view                   
    @items.command()
    async def view(self, ctx, shop: int = None):
        conn = sqlite3.connect("shop_items.db")
        c = conn.cursor()
        
        OwnerID = 638092957756555291
        
        if ctx.message.author.id == OwnerID:
            if shop == None:
                await ctx.send("Please send a shop ID")
                
            else:
                c.execute(f"SELECT rowid, * FROM shop_items WHERE rowid = {shop}")
                
                items = c.fetchall()
                none = str(items)
                
                if none == "[]":
                    await ctx.send("Please send a valid shop Id")
                    
                else:
                    for item in items:
                        id = item[0]
                        name = item[1]
                        price = item[2]
                        option = item[3]
                        use = item[4]
                        
                    embed: discord.Embed = discord.Embed(
                        title="Shop View Settings",
                        description=f"Shop ID - {id}\nItem Name - {name}\nItem Price - {price}\nItem Option - {option}\nItem Use - {use}",
                        color=discord.Color.green()   
                    )
                    
                    await ctx.send(embed=embed)
        
        else:
            await ctx.send("Not a valid owner ID")
                                    
async def setup(client):
	await client.add_cog(Owner(client))  