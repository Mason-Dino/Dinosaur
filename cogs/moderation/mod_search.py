import discord
import os
from discord.ext import commands
from discord.ext.commands import BucketType
import asyncio
import random
import math
import sqlite3

class Mod_Search(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def case(self, ctx, case: int):
        conn = sqlite3.connect("moderation.db")
        c = conn.cursor()

        c.execute(f"SELECT rowid, * FROM moderation_log WHERE rowid = {case} AND guild_ID = '{ctx.guild.id}' ORDER BY rowid DESC LIMIT 1")

        items = c.fetchall()

        none = str(items)

        if none == "[]":
            await ctx.send("That is not a vaild case ID")

        else:
            for item in items:
                case_ID = item[0]
                user = item[2]
                user_ID = item[3]
                mod = item[4]
                mod_ID = item[5]
                action = item[6]
                reason = item[7]

            embed: discord.Embed = discord.Embed(
                title="Case Information",
                description=f"Case ID - {case_ID}",
                color=discord.Color.green()
            )
            embed.add_field(name="**User**", value=f"User Name - {user}\nUser ID - {user_ID}", inline=False)
            embed.add_field(name="**Mod**", value=f"Mod Name - {mod}\nMod ID - {mod_ID}", inline=False)
            embed.add_field(name="**Action**", value=f"Action - {action}", inline=False)
            embed.add_field(name="**Reason**", value=f"The reason for the {action} is\n```{reason}```", inline=False)

            await ctx.send(embed=embed)

    @commands.command()
    async def mod(self, ctx, user: discord.Member = None):
        conn =  sqlite3.connect("moderation.db")
        c = conn.cursor()

        if user == None:
            c.execute(f"SELECT rowid, * FROM moderation_log WHERE mod_ID = '{ctx.message.author.id}' AND guild_ID = '{ctx.guild.id}' ORDER BY rowid DESC LIMIT 1")

            items = c.fetchall()

            none = str(items)

            if none == "[]":
                await ctx.send("You have no mod actions.")

                conn.commit()
                conn.close()

            else:
                for item in items:
                    action_1 = f"{item[0]} | {item[2]} | {item[4]} | {item[6]}"
                

                c.execute(f"SELECT rowid, * FROM moderation_log WHERE mod_ID = '{ctx.message.author.id}' AND guild_ID = '{ctx.guild.id}' ORDER BY rowid DESC LIMIT 1 OFFSET 1")

                items = c.fetchall()

                none = str(items)

                if none == "[]":
                    embed: discord.Embed = discord.Embed(
                        title="Mod Search",
                        description=f"Bellow are the mod infractions of {ctx.message.author.mention}\n\n```Case ID | User | Moderator | Action\n\n{action_1}```",
                        color=discord.Color.green()
                    )

                    await ctx.send(embed=embed)

                    conn.commit()
                    conn.close()

                else:
                    for item in items:
                        action_2 = f"{item[0]} | {item[2]} | {item[4]} | {item[6]}"


                    c.execute(f"SELECT rowid, * FROM moderation_log WHERE mod_ID = '{ctx.message.author.id}' AND guild_ID = '{ctx.guild.id}' ORDER BY rowid DESC LIMIT 1 OFFSET 2")

                    items = c.fetchall()

                    none = str(items)

                    if none == "[]":
                        embed: discord.Embed = discord.Embed(
                            title="Mod Search",
                            description=f"Bellow are the mod infractions of {ctx.message.author.mention}\n\n```Case ID | User | Moderator | Action\n\n{action_1}\n{action_2}```",
                            color=discord.Color.green()
                        )
                        
                        await ctx.send(embed=embed)

                        conn.commit()
                        conn.close()

                    else:
                        for item in items:
                            action_3 = f"{item[0]} | {item[2]} | {item[4]} | {item[6]}"


                        c.execute(f"SELECT rowid, * FROM moderation_log WHERE mod_ID = '{ctx.message.author.id}' AND guild_ID = '{ctx.guild.id}' ORDER BY rowid DESC LIMIT 1 OFFSET 3")

                        items = c.fetchall()

                        none = str(items)

                        if none == "[]":
                            embed: discord.Embed = discord.Embed(
                                title="Mod Search",
                                description=f"Bellow are the mod infractions of {ctx.message.author.mention}\n\n```Case ID | User | Moderator | Action\n\n{action_1}\n{action_2}\n{action_3}```",
                                color=discord.Color.green()
                            )
                            
                            await ctx.send(embed=embed)

                            conn.commit()
                            conn.close()

                        else: 
                            for item in items:
                                action_4 = f"{item[0]} | {item[2]} | {item[4]} | {item[6]}"


                            c.execute(f"SELECT rowid, * FROM moderation_log WHERE mod_ID = '{ctx.message.author.id}' AND guild_ID = '{ctx.guild.id}' ORDER BY rowid DESC LIMIT 1 OFFSET 4")

                            items = c.fetchall()

                            none = str(items)

                            if none == "[]":
                                embed: discord.Embed = discord.Embed(
                                    title="Mod Search",
                                    description=f"Bellow are the mod infractions of {ctx.message.author.mention}\n\n```Case ID | User | Moderator | Action\n\n{action_1}\n{action_2}\n{action_3}\n{action_4}```",
                                    color=discord.Color.green()
                                )
                                
                                await ctx.send(embed=embed)

                                conn.commit()
                                conn.close()

                            else:
                                for item in items:
                                    action_5 = f"{item[0]} | {item[2]} | {item[4]} | {item[6]}"

                                embed: discord.Embed = discord.Embed(
                                    title="Mod Search",
                                    description=f"Bellow are the mod infractions of {ctx.message.author.mention}\n\n```Case ID | User | Moderator | Action\n\n{action_1}\n{action_2}\n{action_3}\n{action_4}\n{action_5}```",
                                    color=discord.Color.green()
                                )

                                await ctx.send(embed=embed)

                                conn.commit()
                                conn.close()

        else:
            c.execute(f"SELECT rowid, * FROM moderation_log WHERE mod_ID = '{user.id}' AND guild_ID = '{ctx.guild.id}' ORDER BY rowid DESC LIMIT 1")

            items = c.fetchall()

            none = str(items)

            if none == "[]":
                await ctx.send("User has not givin out any mod actions.")

                conn.commit()
                conn.close()

            else:
                for item in items:
                    action_1 = f"{item[0]} | {item[2]} | {item[4]} | {item[6]}"
                

                c.execute(f"SELECT rowid, * FROM moderation_log WHERE mod_ID = '{user.id}' AND guild_ID = '{ctx.guild.id}' ORDER BY rowid DESC LIMIT 1 OFFSET 1")

                items = c.fetchall()

                none = str(items)

                if none == "[]":
                    embed: discord.Embed = discord.Embed(
                        title="Mod Search",
                        description=f"Bellow are the mod infractions of {user.mention}\n\n```Case ID | User | Moderator | Action\n\n{action_1}```",
                        color=discord.Color.green()
                    )

                    await ctx.send(embed=embed)

                    conn.commit()
                    conn.close

                else:
                    for item in items:
                        action_2 = f"{item[0]} | {item[2]} | {item[4]} | {item[6]}"


                    c.execute(f"SELECT rowid, * FROM moderation_log WHERE mod_ID = '{user.id}' AND guild_ID = '{ctx.guild.id}' ORDER BY rowid DESC LIMIT 1 OFFSET 2")

                    items = c.fetchall()

                    none = str(items)

                    if none == "[]":
                        embed: discord.Embed = discord.Embed(
                            title="Mod Search",
                            description=f"Bellow are the mod infractions of {user.mention}\n\n```Case ID | User | Moderator | Action\n\n{action_1}\n{action_2}```",
                            color=discord.Color.green()
                        )
                        
                        await ctx.send(embed=embed)

                        conn.commit()
                        conn.close()

                    else:
                        for item in items:
                            action_3 = f"{item[0]} | {item[2]} | {item[4]} | {item[6]}"


                        c.execute(f"SELECT rowid, * FROM moderation_log WHERE mod_ID = '{user.id}' AND guild_ID = '{ctx.guild.id}' ORDER BY rowid DESC LIMIT 1 OFFSET 3")

                        items = c.fetchall()

                        none = str(items)

                        if none == "[]":
                            embed: discord.Embed = discord.Embed(
                                title="Mod Search",
                                description=f"Bellow are the mod infractions of {user.mention}\n\n```Case ID | User | Moderator | Action\n\n{action_1}\n{action_2}\n{action_3}```",
                                color=discord.Color.green()
                            )
                            
                            await ctx.send(embed=embed)

                            conn.commit()
                            conn.close()

                        else: 
                            for item in items:
                                action_4 = f"{item[0]} | {item[2]} | {item[4]} | {item[6]}"


                            c.execute(f"SELECT rowid, * FROM moderation_log WHERE mod_ID = '{user.id}' AND guild_ID = '{ctx.guild.id}' ORDER BY rowid DESC LIMIT 1 OFFSET 4")

                            items = c.fetchall()

                            none = str(items)

                            if none == "[]":
                                embed: discord.Embed = discord.Embed(
                                    title="Mod Search",
                                    description=f"Bellow are the mod infractions of {user.mention}\n\n```Case ID | User | Moderator | Action\n\n{action_1}\n{action_2}\n{action_3}\n{action_4}```",
                                    color=discord.Color.green()
                                )
                                
                                await ctx.send(embed=embed)
                                
                                conn.commit()
                                conn.close()


                            else:
                                for item in items:
                                    action_5 = f"{item[0]} | {item[2]} | {item[4]} | {item[6]}"

                                embed: discord.Embed = discord.Embed(
                                    title="Mod Search",
                                    description=f"Bellow are the mod infractions of {user.mention}\n\n```Case ID | User | Moderator | Action\n\n{action_1}\n{action_2}\n{action_3}\n{action_4}\n{action_5}```",
                                    color=discord.Color.green()
                                )

                                await ctx.send(embed=embed)

                                conn.commit()
                                conn.close()

    @commands.command()
    async def user(self, ctx, user: discord.Member = None):
        conn =  sqlite3.connect("moderation.db")
        c = conn.cursor()

        if user == None:
            c.execute(f"SELECT rowid, * FROM moderation_log WHERE user_ID = '{ctx.message.author.id}' AND guild_ID = '{ctx.guild.id}' ORDER BY rowid DESC LIMIT 1")

            items = c.fetchall()

            none = str(items)

            if none == "[]":
                await ctx.send("User has no infractions.")

                conn.commit()
                conn.close()

            else:
                for item in items:
                    action_1 = f"{item[0]} | {item[2]} | {item[4]} | {item[6]}"
                

                c.execute(f"SELECT rowid, * FROM moderation_log WHERE user_ID = '{ctx.message.author.id}' AND guild_ID = '{ctx.guild.id}' ORDER BY rowid DESC LIMIT 1 OFFSET 1")

                items = c.fetchall()

                none = str(items)

                if none == "[]":
                    embed: discord.Embed = discord.Embed(
                        title="User Search",
                        description=f"Bellow are the mod infractions of {ctx.message.author.mention}\n\n```Case ID | User | Moderator | Action\n\n{action_1}```",
                        color=discord.Color.green()
                    )

                    await ctx.send(embed=embed)

                    conn.commit()
                    conn.close()

                else:
                    for item in items:
                        action_2 = f"{item[0]} | {item[2]} | {item[4]} | {item[6]}"


                    c.execute(f"SELECT rowid, * FROM moderation_log WHERE user_ID = '{ctx.message.author.id}' AND guild_ID = '{ctx.guild.id}' ORDER BY rowid DESC LIMIT 1 OFFSET 2")

                    items = c.fetchall()

                    none = str(items)

                    if none == "[]":
                        embed: discord.Embed = discord.Embed(
                            title="User Search",
                            description=f"Bellow are the mod infractions of {ctx.message.author.mention}\n\n```Case ID | User | Moderator | Action\n\n{action_1}\n{action_2}```",
                            color=discord.Color.green()
                        )
                        
                        await ctx.send(embed=embed)

                        conn.commit()
                        conn.close()

                    else:
                        for item in items:
                            action_3 = f"{item[0]} | {item[2]} | {item[4]} | {item[6]}"


                        c.execute(f"SELECT rowid, * FROM moderation_log WHERE user_ID = '{ctx.message.author.id}' AND guild_ID = '{ctx.guild.id}' ORDER BY rowid DESC LIMIT 1 OFFSET 3")

                        items = c.fetchall()

                        none = str(items)

                        if none == "[]":
                            embed: discord.Embed = discord.Embed(
                                title="User Search",
                                description=f"Bellow are the mod infractions of {ctx.message.author.mention}\n\n```Case ID | User | Moderator | Action\n\n{action_1}\n{action_2}\n{action_3}```",
                                color=discord.Color.green()
                            )
                            
                            await ctx.send(embed=embed)

                            conn.commit()
                            conn.close()

                        else: 
                            for item in items:
                                action_4 = f"{item[0]} | {item[2]} | {item[4]} | {item[6]}"


                            c.execute(f"SELECT rowid, * FROM moderation_log WHERE user_ID = '{ctx.message.author.id}' AND guild_ID = '{ctx.guild.id}' ORDER BY rowid DESC LIMIT 1 OFFSET 4")

                            items = c.fetchall()

                            none = str(items)

                            if none == "[]":
                                embed: discord.Embed = discord.Embed(
                                    title="User Search",
                                    description=f"Bellow are the mod infractions of {ctx.message.author.mention}\n\n```Case ID | User | Moderator | Action\n\n{action_1}\n{action_2}\n{action_3}\n{action_4}```",
                                    color=discord.Color.green()
                                )
                                
                                await ctx.send(embed=embed)

                                conn.commit()
                                conn.close()

                            else:
                                for item in items:
                                    action_5 = f"{item[0]} | {item[2]} | {item[4]} | {item[6]}"

                                embed: discord.Embed = discord.Embed(
                                    title="User Search",
                                    description=f"Bellow are the mod infractions of {ctx.message.author.mention}\n\n```Case ID | User | Moderator | Action\n\n{action_1}\n{action_2}\n{action_3}\n{action_4}\n{action_5}```",
                                    color=discord.Color.green()
                                )

                                await ctx.send(embed=embed)

                                conn.commit()
                                conn.close()

        else:
            c.execute(f"SELECT rowid, * FROM moderation_log WHERE user_ID = '{user.id}' AND guild_ID = '{ctx.guild.id}' ORDER BY rowid DESC LIMIT 1")

            items = c.fetchall()

            none = str(items)

            if none == "[]":
                await ctx.send("User has no infractions.")

                conn.commit()
                conn.close()

            else:
                for item in items:
                    action_1 = f"{item[0]} | {item[2]} | {item[4]} | {item[6]}"
                

                c.execute(f"SELECT rowid, * FROM moderation_log WHERE user_ID = '{user.id}' AND guild_ID = '{ctx.guild.id}' ORDER BY rowid DESC LIMIT 1 OFFSET 1")

                items = c.fetchall()

                none = str(items)

                if none == "[]":
                    embed: discord.Embed = discord.Embed(
                        title="User Search",
                        description=f"Bellow are the mod infractions of {user.mention}\n\n```Case ID | User | Moderator | Action\n\n{action_1}```",
                        color=discord.Color.green()
                    )

                    await ctx.send(embed=embed)

                    conn.commit()
                    conn.close()

                else:
                    for item in items:
                        action_2 = f"{item[0]} | {item[2]} | {item[4]} | {item[6]}"


                    c.execute(f"SELECT rowid, * FROM moderation_log WHERE user_ID = '{user.id}' AND guild_ID = '{ctx.guild.id}' ORDER BY rowid DESC LIMIT 1 OFFSET 2")

                    items = c.fetchall()

                    none = str(items)

                    if none == "[]":
                        embed: discord.Embed = discord.Embed(
                            title="User Search",
                            description=f"Bellow are the mod infractions of {user.mention}\n\n```Case ID | User | Moderator | Action\n\n{action_1}\n{action_2}```",
                            color=discord.Color.green()
                        )
                        
                        await ctx.send(embed=embed)

                        conn.commit()
                        conn.close()

                    else:
                        for item in items:
                            action_3 = f"{item[0]} | {item[2]} | {item[4]} | {item[6]}"


                        c.execute(f"SELECT rowid, * FROM moderation_log WHERE user_ID = '{user.id}' AND guild_ID = '{ctx.guild.id}' ORDER BY rowid DESC LIMIT 1 OFFSET 3")

                        items = c.fetchall()

                        none = str(items)

                        if none == "[]":
                            embed: discord.Embed = discord.Embed(
                                title="User Search",
                                description=f"Bellow are the mod infractions of {user.mention}\n\n```Case ID | User | Moderator | Action\n\n{action_1}\n{action_2}\n{action_3}```",
                                color=discord.Color.green()
                            )
                            
                            await ctx.send(embed=embed)

                            conn.commit()
                            conn.close()

                        else: 
                            for item in items:
                                action_4 = f"{item[0]} | {item[2]} | {item[4]} | {item[6]}"


                            c.execute(f"SELECT rowid, * FROM moderation_log WHERE user_ID = '{user.id}' AND guild_ID = '{ctx.guild.id}' ORDER BY rowid DESC LIMIT 1 OFFSET 4")

                            items = c.fetchall()

                            none = str(items)

                            if none == "[]":
                                embed: discord.Embed = discord.Embed(
                                    title="User Search",
                                    description=f"Bellow are the mod infractions of {user.mention}\n\n```Case ID | User | Moderator | Action\n\n{action_1}\n{action_2}\n{action_3}\n{action_4}```",
                                    color=discord.Color.green()
                                )
                                
                                await ctx.send(embed=embed)

                                conn.commit()
                                conn.close()

                            else:
                                for item in items:
                                    action_5 = f"{item[0]} | {item[2]} | {item[4]} | {item[6]}"

                                embed: discord.Embed = discord.Embed(
                                    title="User Search",
                                    description=f"Bellow are the mod infractions of {user.mention}\n\n```Case ID | User | Moderator | Action\n\n{action_1}\n{action_2}\n{action_3}\n{action_4}\n{action_5}```",
                                    color=discord.Color.green()
                                )

                                await ctx.send(embed=embed)

                                conn.commit()
                                conn.close()


    @commands.command()
    async def delete(self, ctx, case: int = None):
        conn = sqlite3.connect("moderation.db")
        c = conn.cursor()

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        c.execute(f"SELECT rowid, * FROM role WHERE guild_ID = '{ctx.guild.id}' ORDER BY rowid DESC LIMIT 1")

        items = c.fetchall()

        none = str(items)

        if none == "[]":
            await ctx.send("Pleae contact a user with admin perms to set up moderation commands. You can use **d/moderation start** to set up the moderation commands")

        elif case == None:
            await ctx.send("Please send a case ID")
            
        else:
            for item in items:
                delete_inf = item[7]
                ban = item[8]
                unban = item[9]
                all_perm = item[10]

                mod_log = item[12]

            log = self.client.get_channel(mod_log)

            if f"{delete_inf}" in f"{ctx.author.roles}" or f"{ban}" in f"{ctx.author.roles}" or f"{unban}" in f"{ctx.author.roles}" or f"{all_perm}" in f"{ctx.author.roles}":
                c.execute(f"SELECT rowid, * FROM moderation_log WHERE rowid = {case} AND guild_ID = '{ctx.guild.id}'")

                items = c.fetchall()
                none = str(items)

                if none == "[]":
                    await ctx.send("Please send a vaild case ID")

                else:
                    embed: discord.Embed = discord.Embed(
                        title="Delete Infration",
                        description="Are you sure you want to delete the infration?\nSay **Yes** to delete it.\nSay **No** to no delete it.\nSay **Info** to see the information of the case ID.",
                        color=discord.Color.green()
                    )

                    await ctx.send(embed=embed)

                    msg = await self.client.wait_for("message", check=check)
            
                    if msg.content.lower() == "yes":
                        c.execute(f"DELETE from moderation_log WHERE rowid = {case} AND guild_ID = '{ctx.guild.id}'")

                        conn.commit()
                        conn.close()

                        await ctx.send(f"Case Infration `{case}`\nHas been deleted")
                        await log.sed(f"Case Infraction `{case}` was delete by `{ctx.message.author}`")

                    elif msg.content.lower() == "no":
                        await ctx.send(f"Case Infration `{case}`\nHas not been deleted")

                    elif msg.content.lower() == "info":

                        c.execute(f"SELECT rowid, * FROM moderation_log WHERE rowid = {case} AND guild_ID = '{ctx.guild.id}'")

                        items = c.fetchall()

                        for item in items:
                            case_ID = item[0]
                            user = item[2]
                            user_ID = item[3]
                            mod = item[4]
                            mod_ID = item[5]
                            action = item[6]
                            reason = item[7]

                        embed: discord.Embed = discord.Embed(
                            title="Case Information",
                            description=f"Case ID - {case_ID}",
                            color=discord.Color.green()
                        )
                        embed.add_field(name="**User**", value=f"User Name - {user}\nUser ID - {user_ID}", inline=False)
                        embed.add_field(name="**Mod**", value=f"Mod Name - {mod}\nMod ID - {mod_ID}", inline=False)
                        embed.add_field(name="**Action**", value=f"Action - {action}", inline=False)
                        embed.add_field(name="**Reason**", value=f"The reason for the {action} is\n```{reason}```", inline=False)
                        embed.add_field(name="**Case Infration Delete**", value="Say **Yes** to delete the case infration\nSay **No** to not delete the case infration", inline=False)

                        await ctx.send(embed=embed)

                        msg = await self.client.wait_for("message", check=check)

                        if msg.content.lower() == "yes":
                            c.execute(f"DELETE from moderation_log WHERE rowid = {case} AND guild_ID = '{ctx.guild.id}'")

                            conn.commit()
                            conn.close()

                            await ctx.send(f"Case Infration `{case}`\nHas been deleted")
                            await log.send(f"Case Infraction `{case}` was delete by `{ctx.message.author}`")

                        elif msg.content.lower() == "no":
                            await ctx.send(f"Case Infration `{case}`\nHas not been deleted")

                        else:
                            await ctx.send(f"Case Infration `{case}`\nHas not been deleted")

                    else:
                            await ctx.send(f"Case Infration `{case}`\nHas not been deleted")

            else:
                await ctx.send("You do not have permssion to use this commaand")

    @commands.command()
    async def search(self, ctx, arg1=None):
        conn = sqlite3.connect("moderation.db")
        c = conn.cursor()

        if arg1 == "all":

            c.execute(f"SELECT rowid, * FROM role WHERE guild_ID = '{ctx.guild.id}' ORDER BY rowid DESC LIMIT 1")

            items = c.fetchall()

            none = str(items)

            if none == "[]":
                await ctx.send("Pleae contact a user with admin perms to set up moderation commands. You can use **d/moderation start** to set up the moderation commands")

            else:
                for item in items:
                    warn = item[2]
                    tempmute = item[3]
                    mute = item[4]
                    unmute = item[5]
                    kick = item[6]
                    delete_inf = item[7]
                    ban = item[8]
                    unban = item[9]
                    all_perm = item[10]

                    log = item[12]

                if f"{warn}" in f"{ctx.author.roles}" or f"{tempmute}" in f"{ctx.author.roles}" or f"{mute}" in f"{ctx.author.roles}" or f"{unmute}" in f"{ctx.author.roles}" or f"{kick}" in f"{ctx.author.roles}" or f"{delete_inf}" in f"{ctx.author.roles}" or f"{ban}" in f"{ctx.author.roles}" or f"{unban}" in f"{ctx.author.roles}" or f"{all_perm}" in f"{ctx.author.roles}":
                    
                    c.execute(f"SELECT rowid, * FROM moderation_log WHERE guild_ID = '{ctx.guild.id}' ORDER BY rowid DESC LIMIT 1")

                    items = c.fetchall()

                    none = str(items)

                    if none == "[]":
                        await ctx.send("Sever has no moderation actions.")

                    else:
                        for item in items:
                            action_1 = f"{item[0]} | {item[2]} | {item[4]} | {item[6]}"

                        c.execute(f"SELECT rowid, * FROM moderation_log WHERE guild_ID = '{ctx.guild.id}' ORDER BY rowid DESC LIMIT 1 OFFSET 1")

                        items = c.fetchall()

                        none = str(items)

                        if none == "[]":
                            embed: discord.Embed = discord.Embed(
                                title="All Search",
                                description=f"Bellow are the moderation infractions of the server\n\n```Case ID | User | Moderator | Action\n\n{action_1}```",
                                color=discord.Color.green()
                            )

                            await ctx.send(embed=embed)

                        else:
                            for item in items:
                                action_2 = f"{item[0]} | {item[2]} | {item[4]} | {item[6]}"

                            
                            c.execute(f"SELECT rowid, * FROM moderation_log WHERE guild_ID = '{ctx.guild.id}' ORDER BY rowid DESC LIMIT 1 OFFSET 2")

                            items = c.fetchall()

                            none = str(items)

                            if none == "[]":
                                embed: discord.Embed = discord.Embed(
                                    title="All Search",
                                    description=f"Bellow are the moderation infractions of the server\n\n```Case ID | User | Moderator | Action\n\n{action_1}\n{action_2}```",
                                    color=discord.Color.green()
                                )

                                await ctx.send(embed=embed)

                            else:
                                for item in items:
                                    action_3 = f"{item[0]} | {item[2]} | {item[4]} | {item[6]}"

                                c.execute(f"SELECT rowid, * FROM moderation_log WHERE guild_ID = '{ctx.guild.id}' ORDER BY rowid DESC LIMIT 1 OFFSET 3")
                        
                                items = c.fetchall()

                                none = str(items)

                                if none == "[]":
                                    embed: discord.Embed = discord.Embed(
                                        title="All Search",
                                        description=f"Bellow are the moderation infractions of the server\n\n```Case ID | User | Moderator | Action\n\n{action_1}\n{action_2}\n{action_3}```",
                                        color=discord.Color.green()
                                    )

                                    await ctx.send(embed=embed)

                                else:
                                    for item in items:
                                        action_4 = f"{item[0]} | {item[2]} | {item[4]} | {item[6]}"

                                    c.execute(f"SELECT rowid, * FROM moderation_log WHERE guild_ID = '{ctx.guild.id}' ORDER BY rowid DESC LIMIT 1 OFFSET 4")
                        
                                    items = c.fetchall()

                                    none = str(items)

                                    if none == "[]":
                                        embed: discord.Embed = discord.Embed(
                                            title="All Search",
                                            description=f"Bellow are the moderation infractions of the server\n\n```Case ID | User | Moderator | Action\n\n{action_1}\n{action_2}\n{action_3}\n{action_4}```",
                                            color=discord.Color.green()
                                        )

                                        await ctx.send(embed=embed)

                                    else: 
                                        for item in items:
                                            action_5 = f"{item[0]} | {item[2]} | {item[4]} | {item[6]}"

                                        embed: discord.Embed = discord.Embed(
                                            title="All Search",
                                            description=f"Bellow are the moderation infractions of the server\n\n```Case ID | User | Moderator | Action\n\n{action_1}\n{action_2}\n{action_3}\n{action_4}\n{action_5}```",
                                            color=discord.Color.green()
                                        )
                                        
                                        await ctx.send(embed=embed)

        elif arg1 == "recent":
            c.execute(f"SELECT rowid, * FROM moderation_log WHERE guild_ID = '{ctx.guild.id}' ORDER BY rowid DESC LIMIT 1")

            items = c.fetchall()

            none = str(items)

            if none == "[]":
                await ctx.send("That is not a vaild case ID")

            else:
                for item in items:
                    case_ID = item[0]
                    user = item[2]
                    user_ID = item[3]
                    mod = item[4]
                    mod_ID = item[5]
                    action = item[6]
                    reason = item[7]

                embed: discord.Embed = discord.Embed(
                    title="Case Information",
                    description=f"Case ID - {case_ID}",
                    color=discord.Color.green()
                )
                embed.add_field(name="**User**", value=f"User Name - {user}\nUser ID - {user_ID}", inline=False)
                embed.add_field(name="**Mod**", value=f"Mod Name - {mod}\nMod ID - {mod_ID}", inline=False)
                embed.add_field(name="**Action**", value=f"Action - {action}", inline=False)
                embed.add_field(name="**Reason**", value=f"The reason for the {action} is\n```{reason}```", inline=False)

                await ctx.send(embed=embed)
                                    



def setup(client):
	client.add_cog(Mod_Search(client))