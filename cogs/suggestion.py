import discord
import os
from discord.ext import commands
from discord.ext.commands import BucketType
import asyncio
import random
import math
import sqlite3
import datetime
import string

class Suggestion(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def suggest(self, ctx, *, message=None):
        conn = sqlite3.connect('suggestion.db')
        c = conn.cursor()

        if message == None:
            await ctx.send("Please send something you would like to suggest.")

        else:
            c.execute(f"SELECT * FROM set_up WHERE guild_ID = '{ctx.guild.id}' LIMIT 1")

            items = c.fetchall()

            none = str(items)

            conn.commit()

            if none == "[]":
                await ctx.send("Please contact a admin to set up the suggestions")
            
            else:
                for item in items:
                    aprove_ID = item[1]

                x = datetime.datetime.now()

                date = x.strftime("%x")

                letter = string.ascii_uppercase

                random_letter_1 = random.choice(letter)
                random_letter_2 = random.choice(letter)
                random_number_1 = random.randint(0, 9)
                random_number_2 = random.randint(0, 9)
                random_number_3 = random.randint(0, 9)
                random_number_4 = random.randint(0, 9)
                random_number_5 = random.randint(0, 9)
                    
                channel = self.client.get_channel(aprove_ID)
                
                suggestion_ID = f"{random_number_1}{random_number_2}{random_letter_1}{random_number_3}{random_number_4}{random_number_5}{random_letter_2}"

                c.execute(f"INSERT INTO suggestion VALUES ('{suggestion_ID}', '{ctx.guild.id}', '{ctx.message.author.id}', '{message}')")

                conn.commit()
                conn.close()

                embed: discord.Embed = discord.Embed(
                    title="Suggestion",
                    description=f"{ctx.message.author.mention} Gave a suggestion\n\n{message}",
                    color=discord.Color.green()
                )
                embed.add_field(name="Approval or Denial", value=f"If you would like to aprove the idea do - **d/aprove {random_number_1}{random_number_2}{random_letter_1}{random_number_3}{random_number_4}{random_number_5}{random_letter_2}**\n If you would deny the idea do **d/deny {random_number_1}{random_number_2}{random_letter_1}{random_number_3}{random_number_4}{random_number_5}{random_letter_2}**")
                embed.set_footer(text=f"Suggestion ID - {suggestion_ID} • Subbmited On - {date}")

                await channel.send(embed=embed)

                await ctx.send("You suggestion was submited!")

    @commands.command()
    async def suggestion(self, ctx, arg1=None):
        conn = sqlite3.connect('suggestion.db')
        c = conn.cursor()

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        if arg1 == "start":
            if ctx.message.author.guild_permissions.administrator:

                embed: discord.Embed = discord.Embed(
                    title="Suggestion Set Up",
                    description="Say **start** if you want to get started.\nSay **stop** at any moment and it will stop, this includs right now.",
                    color=discord.Color.green()
                )

                await ctx.send(embed=embed)

                msg = await self.client.wait_for("message", check=check)

                if msg.content == "start":
                    embed: discord.Embed = discord.Embed(
                        title="Suggestions Set Up",
                        description="Please send the **Channel ID** that you would like to have pennding suggestions wait till they are approved.",
                        color=discord.Color.green()
                    )

                    await ctx.send(embed=embed)

                    msg = await self.client.wait_for("message", check=check)
                    aprove = msg.content

                    if msg.content == "stop":
                        await ctx.send("You have stoped setting up suggestions.")

                    else:
                        embed: discord.Embed = discord.Embed(
                            title="Suggestion Set Up",
                            description="Please send the **Channel ID** that you would like to have all the aproved suggestions to go",
                            color= discord.Color.green()
                        )

                        await ctx.send(embed=embed)

                        msg = await self.client.wait_for("message", check=check)
                        aproved = msg.content

                        if msg.content == "stop":
                            await ctx.send("You have stoped setting up suggestions.")

                        else:
                            embed: discord.Embed = discord.Embed(
                                title="Suggestion Set Up",
                                description="Please send the **Role ID** that you would like to be able approve suggestions",
                                color=discord.Color.green()
                            )

                            await ctx.send(embed=embed)

                            msg = await self.client.wait_for("message", check=check)
                            role_1 = msg.content

                            if msg.content == "stop":
                                await ctx.send("You have stoped setting up suggestions")

                            else:
                                embed: discord.Embed = discord.Embed(
                                    title="Suggestions Set Up",
                                    description="Please send the second **Role ID** that you would like to be able to aprove suggestions",
                                    color=discord.Color.green()
                                )

                                await ctx.send(embed=embed)

                                msg = await self.client.wait_for("message", check=check)
                                role_2 = msg.content
                                
                                if msg.content == "stop":
                                    await ctx.send("You have stoped setting up suggestions")

                                else:
                                    embed: discord.Embed = discord.Embed(
                                        title="Suggestions Set Up",
                                        description=f"Bellow Are the channels and roles that you said for setting up suggestions.\n\nPending Approval - <#{aprove}>\nApproved - <#{aproved}>\n\nRole Approval 1 - <@&{role_1}>\nRole Approval 2 - <@&{role_2}>",
                                        color=discord.Color.green()
                                    )
                                    embed.add_field(name="Set Up", value="Say **continue** if you would like to set up the suggestions.\nSay **stop** if you would not like to set up suggestions.")

                                    await ctx.send(embed=embed)

                                    msg = await self.client.wait_for("message", check=check)

                                    if msg.content == "continue":
                                        c.execute(f"INSERT INTO set_up VALUES ('{ctx.guild.id}', '{aprove}', '{aproved}', '{role_2}', '{role_2}')")

                                        conn.commit()
                                        conn.close()

                                        await ctx.send("Suggestions are now set up!")

                                    else:
                                        await ctx.send("You stoped setting up suggestions.")

            else: 
                await ctx.send("You have stoped setting up suggestions.")

    @commands.command()
    async def approve(self, ctx, *, message=None):
        conn = sqlite3.connect('suggestion.db')
        c = conn.cursor()

        if message == None:
            await ctx.send("Please send a suggestion ID you would like to approve")

        else:
            c.execute(f"SELECT * FROM suggestion WHERE suggestion_ID = '{message}' AND guild_ID = '{ctx.guild.id}'")

            items = c.fetchall()

            none = str(items)

            if none == "[]":
                await ctx.send("Please send a vaild suggestion id that you would like to approve")

            else:
                c.execute(f"SELECT * FROM set_up WHERE guild_ID = '{ctx.guild.id}'")

                items = c.fetchall()

                for item in items:
                    approve = int(item[2])

                channel = self.client.get_channel(approve)

                c.execute(f"SELECT * FROM suggestion WHERE suggestion_ID = '{message}' AND guild_ID = '{ctx.guild.id}'")

                items = c.fetchall()

                for item in items:
                    suggestion_ID = str(item[0])
                    user = int(item[2])
                    suggestion = str(item[3])

                embed: discord.Embed = discord.Embed(
                    title="Suggestion",
                    description=f"<@!{user}> suggestion this idea.\n\n{suggestion}",
                    color=discord.Color.green()
                )

                await channel.send(embed=embed)

                c.execute(f"DELETE from suggestion WHERE suggestion_ID = '{message}' AND guild_ID = '{ctx.guild.id}'")

                conn.commit()
                conn.close()

                await ctx.send(f"You approve Suggestion **{suggestion_ID}**")

    @commands.command()
    async def deny(self, ctx, *, message=None):
        await ctx.send("hi")

def setup(client):
	client.add_cog(Suggestion(client)) 