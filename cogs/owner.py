import discord
import os
from discord.audit_logs import _transform_verification_level
from discord.ext import commands
from discord.ext.commands import BucketType
import asyncio
import random
import math
import sqlite3

class Owner(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def owner(self, ctx):

        OwnerID = 638092957756555291

        if ctx.message.author.id == OwnerID:
            embed: discord.Embed = discord.Embed(
                title="Owner Only Commands",
                description="Bellow are all the owner commands",
                color=discord.Color.green()
            )
            #embed.add_field(name="**Clear**", value="If you do **d/clear [member id]** it will clear a users balance")
            #embed.add_field(name="**Change Log Set**", value="If you do **d/change set [message]** it will set the change log")

            await ctx.send(embed=embed)

        else:
            await ctx.send('You are not allowed to execute this command!')

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

    @commands.command()
    async def add_money(self, ctx, user: discord.Member, ammount: int=None):
        conn = sqlite3.connect('economy.db')
        c = conn.cursor()

        OwnerID = 638092957756555291

        if ctx.message.author.id == OwnerID:
            if ammount == None:
                await ctx.send("Please send the ammount of money you would like to add to the user")

            else:
                c.execute(f"SELECT * FROM economy WHERE user_ID = '{user.id}' LIMIT 1")

                items = c.fetchall()

                none = str(items)

                if none == "[]":
                    c.execute(f"INSERT INTO economy VALUES ('{user.id}', '{user}', {ammount} , 0, {ammount})")

                    conn.commit()
                    conn.close()

                    embed: discord.Embed = discord.Embed(
                        title="Add Money",
                        description=f"{ctx.message.author.mention} gave {user.mention} {ammount} of Dinosaur Points",
                        color=discord.Color.green()
                    )

                    await ctx.send(embed=embed)

                else:
                    for item in items:
                        wallet = int(item[2])
                        bank = int(item[3])

                    new_wallet = wallet + ammount

                    c.execute(f"""UPDATE economy SET wallet = {new_wallet}
                            WHERE user_ID = '{user.id}'   
                    """)

                    conn.commit()
                    
                    sum = new_wallet + bank
                    
                    c.execute(f"""UPDATE economy SET net = {sum}
                            WHERE user_ID = '{user.id}'   
                    """)

                    conn.commit()
                                    
                    conn.close()

                    embed: discord.Embed = discord.Embed(
                        title="Add Money",
                        description=f"{ctx.message.author.mention} gave {user.mention} {ammount} of Dinosaur Points",
                        color=discord.Color.green()
                    )

                    await ctx.send(embed=embed)

        else:
            await ctx.send("You do not have permssion to use this command.")
            
    @commands.group()
    async def items(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("Invalid sub command")

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
                        c.execute(f"SELECT rowid, * WHERE rowid={shop}")
                        
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
                                
                                msg = await self.client.wait_for("message", check=check)
                                
                                if msg.content.lower() == "no":
                                    await ctx.send("Use updating process stoped")
                                    
                                else:
                                    use = msg.content
                                    
                                    c.execute(f"""UPDATE shop_items SET use = "{use}"
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
                                
                                msg = await self.client.wait_for("message", check=check)
                                
                                if msg.content.lower() == "no":
                                    await ctx.send("Use updating process stoped")
                                    
                                else:
                                    use = msg.content
                                    
                                    c.execute(f"""UPDATE shop_items SET use = "{use}"
                                                WHERE rowid = {shop}
                                            """)
                                    
                                    conn.commit()
                                    conn.close()
                                    
                                    await ctx.send("Use Updating process complete")
        
        else:
            await ctx.send("Not a valid owner ID")
                                    
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
                                    
def setup(client):
	client.add_cog(Owner(client))  