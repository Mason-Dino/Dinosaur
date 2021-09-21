import discord
import os
from discord.enums import Status
from discord.ext import commands
from discord.ext.commands import BucketType
import asyncio
import random
import math
import sqlite3

from dislash.slash_commands import slash_command
from dislash import *

class Partner(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def apply(self, ctx):
        user = int(ctx.message.author.id)
        user = self.client.get_user(user)

        embed: discord.Embed = discord.Embed(
            title="Start Application",
            description="Say **start** if you would want to start the application\nSay **stop** if you would not like to start the application",
            color=discord.Color.green()
        )
        embed.set_footer(text="You may say stop at any time to stop the partner application process.")

        try:
            await user.send(embed=embed)

        except:
            await ctx.send("Please turn on your dms so that Dinosaur can DM you.")

        await ctx.send("Check your DM's with Dinosaur")

        def check(msg):
            return msg.author == ctx.author


        msg = await self.client.wait_for("message", check=check)
        
        if msg.content.lower() == "start":
            embed: discord.Embed = discord.Embed(
                title="Question #1",
                description="What is your servers name?",
                color=discord.Color.green()
            )

            await user.send(embed=embed)

            msg = await self.client.wait_for("message", check=check)
            question_1 = msg.content

            if msg.content.lower() == "stop":
                await user.send("You have stoped the partner application process")

            else:
                embed: discord.Embed = discord.Embed(
                    title="Question #2",
                    description="What is your server's ID",
                    color=discord.Color.green()
                )

                await user.send(embed=embed)

                msg = await self.client.wait_for("message", check=check)
                question_2 = msg.content

                if msg.content.lower() == "stop":
                    await user.send("You have stoped the partner application process")

                else:
                    embed: discord.Embed = discord.Embed(
                        title="Question #3",
                        description="Give all the owners IDs of the server",
                        color=discord.Color.green()
                    )
                    embed.set_footer(text="Seprate all owner ID's by commas.")

                    await user.send(embed=embed)

                    msg = await self.client.wait_for("message", check=check)
                    question_3 = msg.content

                    if msg.content.lower() == "stop":
                        await user.send("You have stoped the partner application process")

                    else:
                        embed: discord.Embed = discord.Embed(
                            title="Question #4",
                            description="How many members does your server have right now?",
                            color=discord.Color.green()
                        )

                        await user.send(embed=embed)

                        msg = await self.client.wait_for("message", check=check)
                        question_4 = msg.content

                        if msg.content.lower() == "stop":
                            await user.send("You have stoped the partner application process")

                        else:
                            embed: discord.Embed = discord.Embed(
                                title="Question #5",
                                description="What is your server about?",
                                color=discord.Color.green()
                            )

                            await user.send(embed=embed)

                            msg = await self.client.wait_for("message", check=check)
                            question_5 = msg.content

                            if msg.content.lower() == "stop":
                                await user.send("You have stoped the partner application process")
                            
                            else:
                                embed: discord.Embed = discord.Embed(
                                    title="Question #6",
                                    description="Why do you want to be a partnered server with Dinosaur?",
                                    color=discord.Color.green()
                                )

                                await user.send(embed=embed)

                                msg = await self.client.wait_for("message", check=check)
                                question_6 = msg.content

                                if msg.content.lower() == "stop":
                                    await user.send("You have stoped the partner application process")

                                else:
                                    embed: discord.Embed = discord.Embed(
                                        title="Qestion #7",
                                        description="On average how many people react to your giveaways",
                                        color=discord.Color.green()
                                    )

                                    await user.send(embed=embed)

                                    msg = await self.client.wait_for("message", check=check)
                                    question_7 = msg.content

                                    if msg.content.lower() == "stop":
                                        await user.send("You have stoped the partner application process")

                                    else:
                                        embed: discord.Embed = discord.Embed(
                                            title="Application Done",
                                            color=discord.Color.green()
                                        )
                                        embed.add_field(name="Question #1", value=f"```{question_1}```")
                                        embed.add_field(name="Question #2", value=f"```{question_2}```")
                                        embed.add_field(name="Question #3", value=f"```{question_3}```")
                                        embed.add_field(name="Question #4", value=f"```{question_4}```")
                                        embed.add_field(name="Question #5", value=f"```{question_5}```")
                                        embed.add_field(name="Question #6", value=f"```{question_6}```")
                                        embed.add_field(name="Question #7", value=f"```{question_7}```")
                                        embed.add_field(name="Done?", value="If everything looks good say **send**\nIf something is not right send **stop**")
                                        embed.set_footer(text="When you say stop you will have to redo the application again")

                                        await user.send(embed=embed)

                                        msg = await self.client.wait_for("message", check=check)

                                        if msg.content.lower() == "send":
                                            embed: discord.Embed = discord.Embed(
                                                title="New Application",
                                                color=discord.Color.green()
                                            )
                                            embed.add_field(name="Question #1", value=f"```{question_1}```", inline=False)
                                            embed.add_field(name="Question #2", value=f"```{question_2}```", inline=False)
                                            embed.add_field(name="Question #3", value=f"```{question_3}```", inline=False)
                                            embed.add_field(name="Question #4", value=f"```{question_4}```", inline=False)
                                            embed.add_field(name="Question #5", value=f"```{question_5}```", inline=False)
                                            embed.add_field(name="Question #6", value=f"```{question_6}```", inline=False)
                                            embed.add_field(name="Question #7", value=f"```{question_7}```", inline=False)

                                            partner_channel = self.client.get_channel(840355852589596712)

                                            astro = "<@!750087608226545846>"

                                            message = await partner_channel.send("<@!638092957756555291>", embed=embed)

                                            guild_server = int(question_2)
                                            guild_owners = str(question_3)

                                            guild = self.client.get_guild(guild_server)

                                            if guild is None:
                                                guild_check = "<:no:867801048554799105>"
                                                guild_owners_check = "<:no:867801048554799105>"
                                                guild_invite_check = "<:no:867801048554799105>"
                                                
                                                embed: discord.Embed = discord.Embed(
                                                    title="Partner Check",
                                                    description=f"{guild_check} Sever Check\n{guild_owners_check} Message Author Sever Owner Check\n{guild_invite_check} Invite Link",
                                                    color=discord.Color.green()
                                                )
                                                embed.set_footer(text="Green = passed, Red = not passed")

                                                await partner_channel.send(embed=embed)

                                            elif guild is not None:
                                                guild_check = "<:yes:867801015234461717>"

                                                channel = guild.text_channels[0]

                                                try:
                                                    invitelink = await channel.create_invite()
                                                    guild_invite_check = "<:yes:867801015234461717>"
                                                    pass

                                                except:
                                                    guild_invite_check = "<:no:867801048554799105>"
                                                    pass

                                                if f"{ctx.message.author.id}" in guild_owners:
                                                    guild_owners_check = "<:yes:867801015234461717>"
                                                    pass

                                                else:
                                                    guild_owners_check = "<:no:867801048554799105>"
                                                    pass

                                                embed: discord.Embed = discord.Embed(
                                                    title="Partner Check",
                                                    description=f"{guild_check} Sever Check\n{guild_owners_check} Message Author Sever Owner Check\n{guild_invite_check} {invitelink} Invite Link",
                                                    color=discord.Color.green()
                                                )
                                                embed.set_footer(text="Green = passed, Red = not passed")

                                                await partner_channel.send(embed=embed)

                                            reaction = ["<:yes:867801015234461717>", "<:no:867801048554799105>"]

                                            conn = sqlite3.connect("partner.db")
                                            c = conn.cursor()
                                            
                                            status = "Waiting"
                                            
                                            await partner_channel.send(message.id)

                                            c.execute(f"INSERT INTO application VALUES ('{message.id}', 0, 0, '{question_1}', '{question_2}', '{question_3}', '{question_4}', '{question_5}', '{question_6}', '{question_7}', '{status}')")
                                            
                                            conn.commit()
                                            conn.close()

                                            for emoji in reaction:
                                                await message.add_reaction(emoji)

                                        else:
                                            await user.send("You have stoped the partner application process")

        
        
        else:
            await user.send("You have stoped the partner application process")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        join_channel = discord.utils.get(member.guild.channels, id=840354954074128408)

        await join_channel.send(f"Welcome {member.mention}") 
        
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.member.bot == True:
            return
        
        else:
            conn = sqlite3.connect("partner.db")
            c = conn.cursor()
            
            c.execute(f"SELECT * FROM application WHERE message_id = '{payload.message_id}'")
            
            items = c.fetchall()
            
            for item in items:
                yes = int(item[1])
                no = int(item[2])
                
            if payload.emoji.name == "yes":
                sum = yes + 1
                
                c.execute(f"""UPDATE application SET ammount_yes = {sum}
                        WHERE message_id = '{payload.message_id}'   
                    """)
                
                conn.commit()
                conn.close()
                
            elif payload.emoji.name == "no":
                sum = no + 1
                
                c.execute(f"""UPDATE application SET ammount_no = {sum}
                        WHERE message_id = '{payload.message_id}'   
                    """)
                
                conn.commit()
                conn.close()
            
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        user = self.client.get_user(payload.user_id)
        
        test = self.client.get_channel(payload.channel_id)
        
        if not user.bot:
            conn = sqlite3.connect("partner.db")
            c = conn.cursor()
            
            c.execute(f"SELECT * FROM application WHERE message_id = '{payload.message_id}'")
            
            items = c.fetchall()
            
            for item in items:
                yes = int(item[1])
                no = int(item[2])
                
            if payload.emoji.name == "yes":
                sum = yes - 1
                
                c.execute(f"""UPDATE application SET ammount_yes = {sum}
                        WHERE message_id = '{payload.message_id}'   
                    """)
                
                conn.commit()
                conn.close()
                
            elif payload.emoji.name == "no":
                sum = no - 1
                
                c.execute(f"""UPDATE application SET ammount_no = {sum}
                        WHERE message_id = '{payload.message_id}'      
                    """)
                
                conn.commit()
                conn.close()
                
            #await test.send(f"<:{payload.emoji.name}:{payload.emoji.id}>")
            
            
            
        else:
            return

    @commands.command()
    async def beta(self, ctx):
        guild = self.client.get_guild(816245302428172298)

        await ctx.send(guild)

        channel = self.client.get_channel(841021173629583370)

        await ctx.send(guild.text_channels[0])

        channel = guild.text_channels[0]

        invitelink = await channel.create_invite()

        await ctx.send(invitelink)


        try:
            guild.get_member(840025172861386762)

            await ctx.send("hey")

        except:
            await ctx.send("Why Dinosaur")

    @commands.command()
    async def partner(self, ctx, message_ID: int = None):
        conn = sqlite3.connect("partner.db")
        c = conn.cursor()
        
        c.execute(f"SELECT * FROM application WHERE message_id = '{message_ID}'")
        
        items = c.fetchall()
        
        await ctx.send(items)


def setup(client):
	client.add_cog(Partner(client)) 