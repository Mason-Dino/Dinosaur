import discord
import os
from discord.ext import commands
from discord.ext.commands import BucketType
import asyncio
import random
import math
import sqlite3

class Mod_Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def warn(self, ctx, user: discord.Member = None, *, message=None):
        conn = sqlite3.connect("moderation.db")
        c = conn.cursor()

        c.execute(f"SELECT rowid, * FROM role WHERE guild_ID = '{ctx.guild.id}' ORDER BY rowid DESC LIMIT 1")

        items = c.fetchall()

        none = str(items)

        if none == "[]":
            await ctx.send("Pleae contact a user with admin perms to set up moderation commands. You can use **d/moderation start** to set up the moderation commands")

        else:
            if message == None:
                message = "No reason provided"
                pass

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

                c.execute(f"INSERT INTO moderation_log VALUES ('{ctx.guild.id}', '{user}', '{user.id}', '{ctx.message.author}', '{ctx.message.author.id}', 'Warn', '{message}')")

                conn.commit()
                conn.close()

                log = self.client.get_channel(log)

                await ctx.send(f"You warned `{user}` for `{message}`.")

                await log.send(f"`{ctx.message.author}` warned `{user}` for `{message}`.")

                embed: discord.Embed = discord.Embed(
                    title="You Have Been Warned",
                    description=f"You have been warend in **{ctx.guild.name}**\nthe reason is:```{message}```",
                    color=discord.Color.green() 
                )

                await user.send(embed=embed)

            else:
                await ctx.send("You do have permmsion to use this command.")

    @commands.command()
    async def tempmute(self, ctx, user: discord.Member, time=None, *, message=None):
        conn = sqlite3.connect("moderation.db")
        c = conn.cursor()

        c.execute(f"SELECT rowid, * FROM role WHERE guild_ID = '{ctx.guild.id}' ORDER BY rowid DESC LIMIT 1")

        items = c.fetchall()

        none = str(items)

        if none == "[]":
            await ctx.send("Pleae contact a user with admin perms to set up moderation commands. You can use **d/moderation start** to set up the moderation commands")

        else:
            if message == None:
                message = "No reason provided"
                pass

            elif time == None:
                await ctx.send("Please include a time for the tempmute.")
                pass

            for item in items:
                tempmute = item[3]
                mute = item[4]
                unmute = item[5]
                kick = item[6]
                delete_inf = item[7]
                ban = item[8]
                unban = item[9]
                all_perm = item[10]

                mute_role = item[11]
                mute_role_str = str(item[11])
                mod_log = item[12]

            if f"{tempmute}" in f"{ctx.author.roles}" or f"{mute}" in f"{ctx.author.roles}" or f"{unmute}" in f"{ctx.author.roles}" or f"{kick}" in f"{ctx.author.roles}" or f"{delete_inf}" in f"{ctx.author.roles}" or f"{ban}" in f"{ctx.author.roles}" or f"{unban}" in f"{ctx.author.roles}" or f"{all_perm}" in f"{ctx.author.roles}":
                if f"{mute_role_str}" in f"{user.roles}":
                    await ctx.send("User is already muted")

                else:
                    time_converter = {"s":1, "m":60, "h":3600, "d":8600}

                    if "s" in time:
                        unit = "seconds"
                        number = time.split("s")
                        number_time = int(number[0]) 
                        pass

                    elif "m" in time:
                        unit = "minutes"
                        number = time.split("m")
                        number_time = int(number[0]) 
                        pass

                    elif "h" in time:
                        unit = "hours"
                        number = time.split("h")
                        number_time = int(number[0])
                        pass

                    elif "d" in time:
                        unit = "days"
                        number = time.split("d")
                        number_time = int(number[0])
                        pass

                    temptime = int(number_time) * time_converter[time[-1]]



                    c.execute(f"INSERT INTO moderation_log VALUES ('{ctx.guild.id}', '{user}', '{user.id}', '{ctx.message.author}', '{ctx.message.author.id}', 'Tempmute', '{message}')")

                    conn.commit()
                    conn.close()

                    log = self.client.get_channel(mod_log)
                
                    role = discord.utils.get(user.guild.roles, id=mute_role)
                    
                    await user.add_roles(role)

                    await ctx.send(f"You tempmuted `{user}` for `{number_time} {unit}`, the reason they are muted is `{message}`")
                    await log.send(f"`{ctx.message.author}` tempmuted `{user}` for `{message}` it is `{number_time} {unit}` long")

                    embed: discord.Embed = discord.Embed(
                        title="You Have Been Tempmuted",
                        description=f"You have been tempmuted in **{ctx.guild.name}**\nthe reason is:\n```{message}```",
                        color=discord.Color.green()
                    )

                    await user.send(embed=embed)

                    await asyncio.sleep(temptime)

                    await user.remove_roles(role)

                    await ctx.send(f"`{user}` was unmuted.")

                    await user.send(f"You were unmuted in **{ctx.guild.name}**")


                    

    @commands.command()
    async def mute(self, ctx, user: discord.Member, *, message=None):
        conn = sqlite3.connect("moderation.db")
        c = conn.cursor()

        c.execute(f"SELECT rowid, * FROM role WHERE guild_ID = '{ctx.guild.id}' ORDER BY rowid DESC LIMIT 1")

        items = c.fetchall()

        none = str(items)

        if none == "[]":
            await ctx.send("Pleae contact a user with admin perms to set up moderation commands. You can use **d/moderation start** to set up the moderation commands")

        else:
            if message == None:
                message = "No reason provided"
                pass

            for item in items:
                mute = item[4]
                unmute = item[5]
                kick = item[6]
                delete_inf = item[7]
                ban = item[8]
                unban = item[9]
                all_perm = item[10]

                mute_role = item[11]
                mute_role_str = str(item[11])
                mod_log = item[12]

            if f"{mute}" in f"{ctx.author.roles}" or f"{unmute}" in f"{ctx.author.roles}" or f"{kick}" in f"{ctx.author.roles}" or f"{delete_inf}" in f"{ctx.author.roles}" or f"{ban}" in f"{ctx.author.roles}" or f"{unban}" in f"{ctx.author.roles}" or f"{all_perm}" in f"{ctx.author.roles}":
                if f"{mute_role_str}" in f"{user.roles}":
                    await ctx.send("User is already muted")

                else:
                    c.execute(f"INSERT INTO moderation_log VALUES ('{ctx.guild.id}', '{user}', '{user.id}', '{ctx.message.author}', '{ctx.message.author.id}', 'Mute', '{message}')")

                    conn.commit()
                    conn.close()

                    log = self.client.get_channel(mod_log)
                    
                    role = discord.utils.get(user.guild.roles, id=mute_role)

                    await user.add_roles(role)

                    await ctx.send(f"You muted `{user}` for `{message}`")

                    await log.send(f"`{ctx.message.author}` muted `{user}` for `{message}`")

                    embed: discord.Embed = discord.Embed(
                        title="You Have Been Muted",
                        description=f"You have been muted in **{ctx.guild.name}**\nthe reason is:```{message}```",
                        color=discord.Color.green() 
                    )

                    await user.send(embed=embed)

            else:
                await ctx.send("You do not have permission to use this command.")

    @commands.command()
    async def unmute(self, ctx, user: discord.Member):
        conn = sqlite3.connect("moderation.db")
        c = conn.cursor()

        c.execute(f"SELECT rowid, * FROM role WHERE guild_ID = '{ctx.guild.id}' ORDER BY rowid DESC LIMIT 1")

        items = c.fetchall()

        none = str(items)

        if none == "[]":
            await ctx.send("Pleae contact a user with admin perms to set up moderation commands. You can use **d/moderation start** to set up the moderation commands")

        else:

            for item in items:
                unmute = item[5]
                kick = item[6]
                delete_inf = item[7]
                ban = item[8]
                unban = item[9]
                all_perm = item[10]

                mute_role = item[11]
                mute_role_str = str(item[11])
                mod_log = item[12]

            if f"{unmute}" in f"{ctx.author.roles}" or f"{kick}" in f"{ctx.author.roles}" or f"{delete_inf}" in f"{ctx.author.roles}" or f"{ban}" in f"{ctx.author.roles}" or f"{unban}" in f"{ctx.author.roles}" or f"{all_perm}" in f"{ctx.author.roles}":

                if f"{mute_role_str}" in f"{user.roles}":
                    c.execute(f"INSERT INTO moderation_log VALUES ('{ctx.guild.id}', '{user}', '{user.id}', '{ctx.message.author}', '{ctx.message.author.id}', 'Unmute', 'None')")

                    conn.commit()
                    conn.close()

                    log = self.client.get_channel(mod_log)
                    
                    role = discord.utils.get(user.guild.roles, id=mute_role)

                    await user.remove_roles(role)

                    await ctx.send(f"You unmuted `{user}`")

                    await log.send(f"`{ctx.message.author}` unmuted `{user}`")

                    embed: discord.Embed = discord.Embed(
                        title="You Have Been Unmuted",
                        description=f"You have been unmuted in **{ctx.guild.name}**",
                        color=discord.Color.green() 
                    )

                    await user.send(embed=embed)

                else:
                    await ctx.send("User is not muted")

            else:
                await ctx.send("You don't have permssion to use this command.")

    @commands.command()
    async def kick(self, ctx, user: discord.Member, *, reason=None):
        conn = sqlite3.connect("moderation.db")
        c = conn.cursor()

        c.execute(f"SELECT rowid, * FROM role WHERE guild_ID = '{ctx.guild.id}' ORDER BY rowid DESC LIMIT 1")

        items = c.fetchall()

        none = str(items)

        if none == "[]":
            await ctx.send("Pleae contact a user with admin perms to set up moderation commands. You can use **d/moderation start** to set up the moderation commands")

        else:
            if reason == None:
                reason = "No reason provided"
                pass

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

                mute_role = item[11]
                mute_role_str = str(item[11])
                mod_log = item[12]

            all_roles = f"{warn} {tempmute} {mute} {unmute} {kick} {delete_inf} {ban} {unban}"

            all_roles_perms = f"{warn} {tempmute} {mute} {unmute} {kick} {delete_inf} {ban} {unban} {all_perm}"

            if f"{kick}" in f"{ctx.author.roles}" or f"{delete_inf}" in f"{ctx.author.roles}" or f"{ban}" in f"{ctx.author.roles}" or f"{unban}" in f"{ctx.author.roles}" or f"{all_perm}" in f"{ctx.author.roles}":
                if f"{warn}" in f"{ctx.author.roles}" or f"{tempmute}" in f"{ctx.author.roles}" or f"{mute}" in f"{ctx.author.roles}" or f"{unmute}" in f"{ctx.author.roles}" or f"{kick}" in f"{ctx.author.roles}" or f"{delete_inf}" in f"{ctx.author.roles}" or f"{ban}" in f"{ctx.author.roles}" or f"{unban}" in f"{ctx.author.roles}" or f"{all_perm}" in f"{ctx.author.roles}":
                    if f"{all_perm}" in f"{ctx.author.roles}":
                        c.execute(f"INSERT INTO moderation_log VALUES ('{ctx.guild.id}', '{user}', '{user.id}', '{ctx.message.author}', '{ctx.message.author.id}', 'Kick', '{reason}')")

                        conn.commit()
                        conn.close()

                        log = self.client.get_channel(mod_log)

                        embed: discord.Embed = discord.Embed(
                            title="You Have Been Kicked",
                            description=f"You have been kicked from **{ctx.guild.name}**\nthe reason is:```{reason}```",
                            color=discord.Color.green() 
                        )
                        try:
                            await user.send(embed=embed)

                        except:
                            pass

                        await user.kick(reason=reason)

                        await ctx.send(f"You kicked `{user}` for `{reason}`")

                        await log.send(f"`{ctx.message.author}` kicked `{user}` for `{reason}`")

                    else:
                        await ctx.send("You can't kick somone with staff roles")

                else:
                    c.execute(f"INSERT INTO moderation_log VALUES ('{ctx.guild.id}', '{user}', '{user.id}', '{ctx.message.author}', '{ctx.message.author.id}', 'Kick', '{reason}')")

                    conn.commit()
                    conn.close()

                    log = self.client.get_channel(mod_log)

                    embed: discord.Embed = discord.Embed(
                        title="You Have Been Kicked",
                        description=f"You have been kicked from **{ctx.guild.name}**\nthe reason is:```{reason}```",
                        color=discord.Color.green() 
                    )
                    try:
                        await user.send(embed=embed)

                    except:
                        pass

                    await user.kick(reason=reason)

                    await ctx.send(f"You kicked `{user}` for `{reason}`")

                    await log.send(f"`{ctx.message.author}` kicked `{user}` for `{reason}`")

            else:
                await ctx.send("You do not have permission to use this command.")

    @commands.command()
    async def ban(self, ctx, user: discord.Member, *, reason=None):
        conn = sqlite3.connect("moderation.db")
        c = conn.cursor()

        c.execute(f"SELECT rowid, * FROM role WHERE guild_ID = '{ctx.guild.id}' ORDER BY rowid DESC LIMIT 1")

        items = c.fetchall()

        none = str(items)

        if none == "[]":
            await ctx.send("Pleae contact a user with admin perms to set up moderation commands. You can use **d/moderation start** to set up the moderation commands")

        else:
            if reason == None:
                reason = "No reason provided"
                pass
            

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

                mute_role = item[11]
                mute_role_str = str(item[11])
                mod_log = item[12]

            if f"{ban}" in f"{ctx.author.roles}" or f"{unban}" in f"{ctx.author.roles}" or f"{all_perm}" in f"{ctx.author.roles}":
                if f"{warn}" in f"{ctx.author.roles}" or f"{tempmute}" in f"{ctx.author.roles}" or f"{mute}" in f"{ctx.author.roles}" or f"{unmute}" in f"{ctx.author.roles}" or f"{kick}" in f"{ctx.author.roles}" or f"{delete_inf}" in f"{ctx.author.roles}" or f"{ban}" in f"{ctx.author.roles}" or f"{unban}" in f"{ctx.author.roles}" or f"{all_perm}" in f"{ctx.author.roles}":
                    if f"{all_perm}" in f"{ctx.author.roles}":
                        c.execute(f"INSERT INTO moderation_log VALUES ('{ctx.guild.id}', '{user}', '{user.id}', '{ctx.message.author}', '{ctx.message.author.id}', 'Ban', '{reason}')")

                        conn.commit()
                        conn.close()

                        log = self.client.get_channel(mod_log)

                        embed: discord.Embed = discord.Embed(
                            title="You Have Been Banned",
                            description=f"You have been banned from **{ctx.guild.name}**\nthe reason is:```{reason}```",
                            color=discord.Color.green() 
                        )

                        try:
                            await user.send(embed=embed)

                        except:
                            pass

                        await user.ban(reason=reason)

                        await ctx.send(f"You banned `{user}` for `{reason}`")

                        await log.send(f"`{ctx.message.author}` banned `{user}` for `{reason}`")

                    else:
                        await ctx.send("You can't ban somone with staff roles.")

                else:
                    c.execute(f"INSERT INTO moderation_log VALUES ('{ctx.guild.id}', '{user}', '{user.id}', '{ctx.message.author}', '{ctx.message.author.id}', 'Ban', '{reason}')")

                    conn.commit()
                    conn.close()

                    log = self.client.get_channel(mod_log)

                    embed: discord.Embed = discord.Embed(
                        title="You Have Been Banned",
                        description=f"You have been banned from **{ctx.guild.name}**\nthe reason is:```{reason}```",
                        color=discord.Color.green() 
                    )

                    try:
                        await user.send(embed=embed)

                    except:
                        pass

                    await user.ban(reason=reason)

                    await ctx.send(f"You banned `{user}` for `{reason}`")

                    await log.send(f"`{ctx.message.author}` banned `{user}` for `{reason}`")
            
            else:
                await ctx.send("You do not have permssion to use this command")



    @commands.command()
    async def unban(self, ctx, *, member):
        conn = sqlite3.connect("moderation.db")
        c = conn.cursor()

        c.execute(f"SELECT rowid, * FROM role WHERE guild_ID = '{ctx.guild.id}' ORDER BY rowid DESC LIMIT 1")

        items = c.fetchall()

        none = str(items)

        if none == "[]":
            await ctx.send("Pleae contact a user with admin perms to set up moderation commands. You can use **d/moderation start** to set up the moderation commands")

        else:
            for item in items:
                unban = item[9]
                all_perm = item[10]

                mute_role = item[11]
                mute_role_str = str(item[11])
                mod_log = item[12]

            if f"{unban}" in f"{ctx.author.roles}" or f"{all_perm}" in f"{ctx.author.roles}":

                banned_users = await ctx.guild.bans()

                member_name, member_discriminator = member.split('#')

                for ban_entry in banned_users:
                    user = ban_entry.user

                    if (user.name, user.discriminator) == (member_name, member_discriminator):
                        await ctx.guild.unban(user)

                        c.execute(f"INSERT INTO moderation_log VALUES ('{ctx.guild.id}', '{user.name}#{user.discriminator}', '{user.id}', '{ctx.message.author}', '{ctx.message.author.id}', 'Unban', 'None')")

                        conn.commit()
                        conn.close()

                        log = self.client.get_channel(mod_log)

                        await ctx.send(f"You unbaned `{user.name}#{user.discriminator}`")

                        await log.send(f"`{ctx.message.author}` unbaned `{user.name}#{user.discriminator}`")

            else:
                await ctx.send("You do not have permssion to use this command")

    


def setup(client):
	client.add_cog(Mod_Commands(client))