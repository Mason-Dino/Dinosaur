import discord
import os
from discord.ext import commands
from discord.ext.commands import BucketType
from dislash.slash_commands import slash_command
from dislash import *
import asyncio
import random
import math
import sqlite3

class Vote(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def vote(self, ctx):
        embed: discord.Embed = discord.Embed(
            title="Vote for Dinosaur on top.gg",
            description="Use the link bellow to vote for Dinosaur\n\nhttps://top.gg/bot/840025172861386762/vote",
            color=discord.Color.green()
        )

        await ctx.send(embed=embed)
        
    @slash_commands.command(
        name="vote",
        description="Gives you a vote link for top.gg"
    )
    async def slash_vote(self, ctx):
        embed: discord.Embed = discord.Embed(
            title="Vote for Dinosaur on top.gg",
            description="Use the link bellow to vote for Dinosaur\n\nhttps://top.gg/bot/840025172861386762/vote",
            color=discord.Color.green()
        )
        
        await ctx.reply(embed=embed)



    @commands.command()
    @commands.cooldown(1, 43200, commands.BucketType.user)
    async def claim(self, ctx, arg1=None):
        if arg1 == "crate":
            if ctx.guild.id == 840354954074128405:
                if "858437928162164736" in f"{ctx.author.roles}":
                    options = [
                        3,
                        2,
                        1,
                        100,
                        500,
                        50,
                        10
                    ]

                    choice = random.choice(options)

                    if choice == 3 or choice == 2 or choice == 1:
                        if choice == 1:
                            conn = sqlite3.connect('shop.db')
                            c = conn.cursor()

                            c.execute(f"SELECT * FROM common WHERE user_ID = '{ctx.message.author.id}'")

                            items = c.fetchall()

                            none = str(items)

                            if none == "[]":
                                c.execute(f"INSERT INTO common VALUES ('{ctx.message.author.id}', 1)")

                                conn.commit()
                                conn.close()

                            else:
                                for item in items:
                                    ammount = int(item[1])

                                new_ammount = ammount + 1

                                c.execute(f"""UPDATE common SET ammount = {new_ammount}
                                    WHERE user_ID = '{ctx.message.author.id}'   
                                """)

                                conn.commit()
                                conn.close()

                                embed: discord.Embed = discord.Embed(
                                    title="Vote Crate Reward",
                                    description=f"You won 1 Common Mystrey Egg\nThanks for voting",
                                    color=discord.Color.green()
                                )
                                await ctx.send(embed=embed)

                        elif choice == 2:
                            conn = sqlite3.connect('shop.db')
                            c = conn.cursor()

                            c.execute(f"SELECT * FROM un_common WHERE user_ID = '{ctx.message.author.id}'")

                            items = c.fetchall()

                            none = str(items)

                            if none == "[]":
                                c.execute(f"INSERT INTO un_common VALUES ('{ctx.message.author.id}', 1)")

                                conn.commit()
                                conn.close()

                            else:
                                for item in items:
                                    ammount = int(item[1])

                                new_ammount = ammount + 1

                                c.execute(f"""UPDATE un_common SET ammount = {new_ammount}
                                    WHERE user_ID = '{ctx.message.author.id}'   
                                """)

                                conn.commit()
                                conn.close()

                                embed: discord.Embed = discord.Embed(
                                    title="Vote Crate Reward",
                                    description=f"You won 1 Un-Common Mystrey Egg\nThanks for voting",
                                    color=discord.Color.green()
                                )
                                await ctx.send(embed=embed)

                        elif choice == 3:
                            conn = sqlite3.connect('shop.db')
                            c = conn.cursor()

                            c.execute(f"SELECT * FROM rare WHERE user_ID = '{ctx.message.author.id}'")

                            items = c.fetchall()

                            none = str(items)

                            if none == "[]":
                                c.execute(f"INSERT INTO rare VALUES ('{ctx.message.author.id}', 1)")

                                conn.commit()
                                conn.close()

                            else:
                                for item in items:
                                    ammount = int(item[1])

                                new_ammount = ammount + 1

                                c.execute(f"""UPDATE rare SET ammount = {new_ammount}
                                    WHERE user_ID = '{ctx.message.author.id}'   
                                """)

                                conn.commit()
                                conn.close()

                                embed: discord.Embed = discord.Embed(
                                    title="Vote Crate Reward",
                                    description=f"You won 1 Rare Mystrey Egg\nThanks for voting",
                                    color=discord.Color.green()
                                )
                                await ctx.send(embed=embed)

                    else:
                        conn = sqlite3.connect("economy.db")
                        c = conn.cursor()

                        c.execute(f"SELECT * FROM economy WHERE user_ID = '{ctx.message.author.id}'")

                        items = c.fetchall()

                        none = str(items)

                        if none == "[]":
                            c.execute(f"INSERT INTO economy VALUES ('{ctx.message.author.id}', '{ctx.message.author}', {choice} , 0, {choice})")

                            conn.commit()
                            conn.close()

                            embed: discord.Embed = discord.Embed(
                                title="Vote Crate Reward",
                                description=f"You won {choice} Dinosaur Points\nThanks for voting",
                                color=discord.Color.green()
                            )
        
                            await ctx.send(embed=embed)

                        else:
                            for item in items:
                                wallet = int(item[2])
                                bank = int(item[3])

                            new_wallet = wallet + choice

                            net = new_wallet + bank

                            c.execute(f"""UPDATE economy SET wallet = {new_wallet}
                                          WHERE user_id = '{ctx.message.author.id}'   
                             """)

                            conn.commit()

                            c.execute(f"""UPDATE economy SET net = {net}
                                    WHERE user_id = '{ctx.message.author.id}'   
                                """)

                            conn.commit()
                            conn.close()

                            embed: discord.Embed = discord.Embed(
                                title="Vote Crate Reward",
                                description=f"You won {choice} Dinosaur Points\nThanks for voting",
                                color=discord.Color.green()
                            )
        
                            await ctx.send(embed=embed)

                else:
                    embed: discord.Embed = discord.Embed(
                        title="Vote",
                        description="Make sure you vote for Dinosaur. You can do `d/vote` to be able to do this command",
                        color=discord.Color.green()
                    )

                    await ctx.send(embed=embed)
            else:
                embed: discord.Embed = discord.Embed(
                    title="Support Server",
                    description="Make sure you join the support server to claim your rewards!",
                    color=discord.Color.green()
                )

                await ctx.send(embed=embed)

                  
def setup(client):
	client.add_cog(Vote(client)) 