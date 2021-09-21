import discord
import os
from discord.ext import commands
from discord.ext.commands import BucketType
import asyncio
import random
import math
import sqlite3

class Mod_Set_Up(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def moderation(self, ctx, arg1=None, arg2=None):
        conn = sqlite3.connect("moderation.db")
        c = conn.cursor()

        guild_id = ctx.guild.id

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        if arg1 == "start":
            if ctx.message.author.guild_permissions.administrator:

                embed: discord.Embed = discord.Embed(
                    title="Moderation Roles Start",
                    description="Say **start** if you want to get started.\nSay **stop** at any moment and it will stop, this includs right now.",
                    color=discord.Color.green()
                )

                await ctx.send(embed=embed)

                msg = await self.client.wait_for("message", check=check)

                if msg.content.lower() == "stop":
                    await ctx.send("The moderation role process was stoped.")

                elif msg.content.lower() == "start":
                    embed: discord.Embed = discord.Embed(
                        title="Warn Command",
                        description="Send the Role ID that you would like to be able to use the warn command.",
                        color=discord.Color.green()
                    )

                    await ctx.send(embed=embed)

                    msg = await self.client.wait_for("message", check=check)
                    warn = msg.content

                    if msg.content.lower() == "stop":
                        await ctx.send("The moderation role process was stoped.")

                    else:
                        embed: discord.Embed = discord.Embed(
                            title="Tempmute Command",
                            description="Send the Role ID that you would like to be able to use the tempmute command.",
                            color=discord.Color.green()
                        )

                        await ctx.send(embed=embed)

                        msg = await self.client.wait_for("message", check=check)
                        tempmute = msg.content

                        if msg.content.lower() == "stop":
                            await ctx.send("The moderation role process was stoped.")

                        else:
                            embed: discord.Embed = discord.Embed(
                                title="Mute Command",
                                description="Send the Role ID that you would like to be able to use the mute command.",
                                color=discord.Color.green()
                            )

                            await ctx.send(embed=embed)

                            msg = await self.client.wait_for("message", check=check)
                            mute = msg.content

                            if msg.content.lower() == "stop":
                                await ctx.send("The moderation role process was stoped.")

                            else:
                                embed: discord.Embed = discord.Embed(
                                    title="Unmute Command",
                                    description="Send the Role ID that you would like to be able to use the unmute command.",
                                    color=discord.Color.green()
                                )

                                await ctx.send(embed=embed)

                                msg = await self.client.wait_for("message", check=check)
                                unmute = msg.content

                                if msg.content.lower() == "stop":
                                    await ctx.send("The moderation role process was stoped.")

                                else:
                                    embed: discord.Embed = discord.Embed(
                                        title="Kick Command",
                                        description="Send the Role ID that you would like to be able to use the kick command.",
                                        color=discord.Color.green()
                                    )

                                    await ctx.send(embed=embed)

                                    msg = await self.client.wait_for("message", check=check)
                                    kick = msg.content

                                    if msg.content.lower() == "stop":
                                        await ctx.send("The moderation role process was stoped.")

                                    else:
                                        embed: discord.Embed = discord.Embed(
                                            title="Delete infraction Command",
                                            description="Send the Role ID that you would like to be able to use the delete infraction command.",
                                            color=discord.Color.green()
                                        )

                                        await ctx.send(embed=embed)

                                        msg = await self.client.wait_for("message", check=check)
                                        delete_inf = msg.content

                                        if msg.content.lower() == "stop":
                                            await ctx.send("The moderation role process was stoped.")

                                        else:
                                            embed: discord.Embed = discord.Embed(
                                                title="Ban Command",
                                                description="Send the Role ID that you would like to be able to use the ban command.",
                                                color=discord.Color.green()
                                            )

                                            await ctx.send(embed=embed)

                                            msg = await self.client.wait_for("message", check=check)
                                            ban = msg.content

                                            if msg.content.lower() == "stop":
                                                await ctx.send("The moderation role process was stoped.")

                                            else:
                                                embed: discord.Embed = discord.Embed(
                                                    title="Unban Command",
                                                    description="Send the Role ID that you would like to be able to use the unban command",
                                                    color=discord.Color.green()
                                                )

                                                await ctx.send(embed=embed)

                                                msg = await self.client.wait_for("message", check=check)
                                                unban = msg.content

                                                if msg.content.lower() == "stop":
                                                    await ctx.send("The moderation role process was stoped.")

                                                else:
                                                    embed: discord.Embed = discord.Embed(
                                                        title="All Perms",
                                                        description="Send the Role ID that you would like to be able to use all commands",
                                                        color=discord.Color.green()
                                                    )

                                                    await ctx.send(embed=embed)

                                                    msg = await self.client.wait_for("message", check=check)
                                                    all_perm = msg.content

                                                    if msg.content.lower() == "stop":
                                                        await ctx.send("The moderation role process was stoped.")

                                                    else:
                                                        embed: discord.Embed = discord.Embed(
                                                            title="Mute Role",
                                                            description="Send the Role ID that will be added to users that get muted",
                                                            color=discord.Color.green()
                                                        )

                                                        await ctx.send(embed=embed)

                                                        msg = await self.client.wait_for("message", check=check)
                                                        mute_role = msg.content

                                                        if msg.content.lower() == "stop":
                                                            await ctx.send("The moderation role process was stoped.")

                                                        else:
                                                            embed: discord.Embed = discord.Embed(
                                                                title="Moderation Log Channel",
                                                                description="Send the Channel ID that when all moderation commands will be sent too.",
                                                                color=discord.Color.green()
                                                            )

                                                            await ctx.send(embed=embed)

                                                            msg = await self.client.wait_for("message", check=check)
                                                            log = msg.content

                                                            if msg.content.lower() == "stop":
                                                                await ctx.send("The moderation role process was stoped.")

                                                            else:
                                                                embed: discord.Embed = discord.Embed(
                                                                    title="Moderation Roles",
                                                                    description=f"Bellow are the roles that go with each command.\n\n**Moderation Roles**\nWarn Command - <@&{warn}>\nTempmute Command - <@&{tempmute}>\nMute Command - <@&{mute}>\nUnmute Command - <@&{unmute}>\nKick Command - <@&{kick}>\nDelete Infraction Command - <@&{delete_inf}>\nBan Command - <@&{ban}>\nUnban Command - <@&{unban}>\nAll Perms - <@&{all_perm}>\n\n**Miscellaneous Roles\n**Muted Role - <@&{mute_role}>\n\n**Moderation Channels**\nModeration Log - <#{log}>",
                                                                    color=discord.Color.green()
                                                                )
                                                                embed.add_field(name="**Notice**", value="People who have permision to do the ban command will be able to do the warn command and the kick command.", inline=False)
                                                                embed.add_field(name="**Continue**", value="If you say **continue** all the perms above will be set in place you can edit at any time. If you say **stop** all the perms will be deleted")

                                                                await ctx.send(embed=embed)

                                                                msg = await self.client.wait_for("message", check=check)

                                                                if msg.content == "stop":
                                                                    await ctx.send("The moderation role process was stoped.")

                                                                elif msg.content == "continue":
                                                                   c.execute(f"INSERT INTO role VALUES ('{ctx.guild.id}', '{warn}', '{tempmute}', '{mute}', '{unmute}', '{kick}', '{delete_inf}', '{ban}', '{unban}', '{all_perm}', '{mute_role}', '{log}')")

                                                                   conn.commit()
                                                                   conn.close()

                                                                   await ctx.send("Dinosaur Moderation is now fully set up!")

                                                                else:
                                                                    await ctx.send("The moderation role process was stoped.")
                                            
            else: 
                await ctx.send("You do not have permission to use this command.")


        elif arg1 == "info":
            if ctx.message.author.guild_permissions.administrator:
                conn = sqlite3.connect("moderation.db")
                c = conn.cursor()

                c.execute(f"SELECT rowid, * FROM role WHERE guild_ID = '{ctx.guild.id}' ORDER BY rowid DESC LIMIT 1")

                items = c.fetchall()

                none = str(items)

                if none == "[]":
                    await ctx.send("You need to set up the moderation prcess you can do **d/moderation start** to set up the diffrent commands")
                
                else:
                    for item in items:
                        print(ctx.guild.id)

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
                    log = item[12]

                    embed: discord.Embed = discord.Embed(
                        title="Moderation Roles",
                        description=f"Bellow are the roles that go with each command.\n\n**Moderation Roles**\nWarn Command - <@&{warn}>\nTempmute Command - <@&{tempmute}>\nMute Command - <@&{mute}>\nUnmute Command - <@&{unmute}>\nKick Command - <@&{kick}>\nDelete Infraction Command - <@&{delete_inf}>\nBan Command - <@&{ban}>\nUnban Command - <@&{unban}>\nAll Perms - <@&{all_perm}>\n\n**Miscellaneous Roles\n**Muted Role - <@&{mute_role}>\n\n**Moderation Channels**\nModeration Log - <#{log}>",
                        color=discord.Color.green()
                    )

                    await ctx.send(embed=embed)

            else:
                await ctx.send("You do no have permission to ue this command.")

        elif arg1 == "update":

            guild_id = ctx.guild.id

            c.execute(f"SELECT rowid, * FROM role WHERE guild_ID = '{ctx.guild.id}' ORDER BY rowid DESC LIMIT 1")

            items = c.fetchall()

            none = str(items)

            if none == "[]":
                await ctx.send("Please set up Dinosaur Moderation first by doing **d/moderation start**")

            else:
                if arg2 == "warn":
                    if ctx.message.author.guild_permissions.administrator:
                        embed: discord.Emed = discord.Embed(
                            title="Warn Command",
                            description="Send the Role ID that you would like to be able to use the warn command.",
                            color=discord.Color.green()
                        )
                        embed.set_footer(text="You may say stop to stop the process")

                        await ctx.send(embed=embed)

                        msg = await self.client.wait_for("message", check=check)
                        warn_update = msg.content

                        if msg.content == "stop":
                            await ctx.send("You have stop the update procces of the warn command")

                        else:
                            c.execute(f"""UPDATE role SET warn = {warn_update}
                                    WHERE guild_ID = '{ctx.guild.id}'   
                                """)

                            embed: discord.Embed = discord.Embed(
                                title="Warn Role Id Update",
                                description=f"The new role ID is\n\nWarn Command - <@&{warn_update}>",
                                color=discord.Color.green()
                            )

                            conn.commit()
                            conn.close()

                            await ctx.send(embed=embed)
                
                    else: 
                        await ctx.send("You do not have permission to use this command.")

                elif arg2 == "tempmute":
                    if ctx.message.author.guild_permissions.administrator:
                        embed: discord.Emed = discord.Embed(
                            title="Tempmute Command",
                            description="Send the Role ID that you would like to be able to use the tempmute command.",
                            color=discord.Color.green()
                        )
                        embed.set_footer(text="You may say stop to stop the process")

                        await ctx.send(embed=embed)

                        msg = await self.client.wait_for("message", check=check)
                        tempmute_update = msg.content

                        if msg.content == "stop":
                            await ctx.send("You have stop the update procces of the tempmute command")

                        else:
                            c.execute(f"""UPDATE role SET tempmute = {tempmute_update}
                                    WHERE guild_ID = '{ctx.guild.id}'   
                                """)

                            conn.commit()
                            conn.close()

                            embed: discord.Embed = discord.Embed(
                                title="Tempmute Role Id Update",
                                description=f"The new role ID is\n\nTempmute Command - <@&{tempmute_update}>",
                                color=discord.Color.green()
                            )

                            await ctx.send(embed=embed)
                
                    else: 
                        await ctx.send("You do not have permission to use this command.")

                elif arg2 == "mute":
                    if ctx.message.author.guild_permissions.administrator:
                        embed: discord.Emed = discord.Embed(
                            title="Mute Command",
                            description="Send the Role ID that you would like to be able to use the mute command.",
                            color=discord.Color.green()
                        )
                        embed.set_footer(text="You may say stop to stop the process")

                        await ctx.send(embed=embed)

                        msg = await self.client.wait_for("message", check=check)
                        mute_update = msg.content

                        if msg.content == "stop":
                            await ctx.send("You have stop the update procces of the mute command")

                        else:
                            c.execute(f"""UPDATE role SET mute = {mute_update}
                                    WHERE guild_ID = '{ctx.guild.id}'   
                                """)

                            conn.commit()
                            conn.close()

                            embed: discord.Embed = discord.Embed(
                                title="Mute Role Id Update",
                                description=f"The new role ID is\n\nMute Command - <@&{mute_update}>",
                                color=discord.Color.green()
                            )

                            await ctx.send(embed=embed)
                
                    else: 
                        await ctx.send("You do not have permission to use this command.")

                elif arg2 == "unmute":
                    if ctx.message.author.guild_permissions.administrator:
                        embed: discord.Emed = discord.Embed(
                            title="Unmute Command",
                            description="Send the Role ID that you would like to be able to use the unmute command.",
                            color=discord.Color.green()
                        )
                        embed.set_footer(text="You may say stop to stop the process")

                        await ctx.send(embed=embed)

                        msg = await self.client.wait_for("message", check=check)
                        unmute_update = msg.content

                        if msg.content == "stop":
                            await ctx.send("You have stop the update procces of the unmute command")

                        else:
                            c.execute(f"""UPDATE role SET unmute = {unmute_update}
                                    WHERE guild_ID = '{ctx.guild.id}'   
                                """)

                            conn.commit()
                            conn.close()

                            embed: discord.Embed = discord.Embed(
                                title="Unmute Role Id Update",
                                description=f"The new role ID is\n\nUnmute Command - <@&{unmute_update}>",
                                color=discord.Color.green()
                            )

                            await ctx.send(embed=embed)
                
                    else: 
                        await ctx.send("You do not have permission to use this command.")

                elif arg2 == "kick":
                    if ctx.message.author.guild_permissions.administrator:
                        embed: discord.Emed = discord.Embed(
                            title="Kick Command",
                            description="Send the Role ID that you would like to be able to use the kick command.",
                            color=discord.Color.green()
                        )
                        embed.set_footer(text="You may say stop to stop the process")

                        await ctx.send(embed=embed)

                        msg = await self.client.wait_for("message", check=check)
                        kick_update = msg.content

                        if msg.content == "stop":
                            await ctx.send("You have stop the update procces of the kick command")

                        else:
                            c.execute(f"""UPDATE role SET kick = {kick_update}
                                    WHERE guild_ID = '{ctx.guild.id}'   
                                """)

                            conn.commit()
                            conn.close()

                            embed: discord.Embed = discord.Embed(
                                title="Kick Role Id Update",
                                description=f"The new role ID is\n\nKick Command - <@&{kick_update}>",
                                color=discord.Color.green()
                            )

                            await ctx.send(embed=embed)
                
                    else: 
                        await ctx.send("You do not have permission to use this command.")

                elif arg2 == "ban":
                    if ctx.message.author.guild_permissions.administrator:
                        embed: discord.Emed = discord.Embed(
                            title="Ban Command",
                            description="Send the Role ID that you would like to be able to use the ban command.",
                            color=discord.Color.green()
                        )
                        embed.set_footer(text="You may say stop to stop the process")

                        await ctx.send(embed=embed)

                        msg = await self.client.wait_for("message", check=check)
                        ban_update = msg.content

                        if msg.content == "stop":
                            await ctx.send("You have stop the update procces of the ban command")

                        else:
                            c.execute(f"""UPDATE role SET ban = {ban_update}
                                    WHERE guild_ID = '{ctx.guild.id}'   
                                """)

                            conn.commit()
                            conn.close()

                            embed: discord.Embed = discord.Embed(
                                title="Ban Role Id Update",
                                description=f"The new role ID is\n\nBan Command - <@&{ban_update}>",
                                color=discord.Color.green()
                            )

                            await ctx.send(embed=embed)
                
                    else: 
                        await ctx.send("You do not have permission to use this command.")

                elif arg2 == "unban":
                    if ctx.message.author.guild_permissions.administrator:
                        embed: discord.Emed = discord.Embed(
                            title="unban Command",
                            description="Send the Role ID that you would like to be able to use the unban command.",
                            color=discord.Color.green()
                        )
                        embed.set_footer(text="You may say stop to stop the process")

                        await ctx.send(embed=embed)

                        msg = await self.client.wait_for("message", check=check)
                        unban_update = msg.content

                        if msg.content == "stop":
                            await ctx.send("You have stop the update procces of the unban command")

                        else:
                            c.execute(f"""UPDATE role SET unban = {unban_update}
                                    WHERE guild_ID = '{ctx.guild.id}'   
                                """)

                            conn.commit()
                            conn.close()

                            embed: discord.Embed = discord.Embed(
                                title="Unban Role Id Update",
                                description=f"The new role ID is\n\nUnban Command - <@&{unban_update}>",
                                color=discord.Color.green()
                            )

                            await ctx.send(embed=embed)
                
                    else: 
                        await ctx.send("You do not have permission to use this command.")

                elif arg2 == "all":
                    if ctx.message.author.guild_permissions.administrator:
                        embed: discord.Emed = discord.Embed(
                            title="All Perm",
                            description="Send the Role ID that you would like to be able to use all the commands.",
                            color=discord.Color.green()
                        )
                        embed.set_footer(text="You may say stop to stop the process")

                        await ctx.send(embed=embed)

                        msg = await self.client.wait_for("message", check=check)
                        all_perm_update = msg.content

                        if msg.content == "stop":
                            await ctx.send("You have stop the update procces of the all perms")

                        else:
                            c.execute(f"""UPDATE role SET all_perm = {all_perm_update}
                                    WHERE guild_ID = '{ctx.guild.id}'   
                                """)

                            conn.commit()
                            conn.close()

                            embed: discord.Embed = discord.Embed(
                                title="Warn Role Id Update",
                                description=f"The new role ID is\n\nAll Perms - <@&{all_perm_update}>",
                                color=discord.Color.green()
                            )

                            await ctx.send(embed=embed)
                
                    else: 
                        await ctx.send("You do not have permission to use this command.")

                elif arg2 == "mute_role":
                    if ctx.message.author.guild_permissions.administrator:
                        embed: discord.Emed = discord.Embed(
                            title="Mute Role",
                            description="Send the Role ID that you would like to be able to use the mute role.",
                            color=discord.Color.green()
                        )
                        embed.set_footer(text="You may say stop to stop the process")

                        await ctx.send(embed=embed)

                        msg = await self.client.wait_for("message", check=check)
                        mute_role_update = msg.content

                        if msg.content == "stop":
                            await ctx.send("You have stop the update procces of the mute role")

                        else:
                            c.execute(f"""UPDATE role SET all_perm = {mute_role_update}
                                    WHERE guild_ID = '{ctx.guild.id}'   
                                """)

                            conn.commit()
                            conn.close()

                            embed: discord.Embed = discord.Embed(
                                title="Warn Role Id Update",
                                description=f"The new role ID is\n\nMuted Role - <@&{mute_role_update}>",
                                color=discord.Color.green()
                            )

                            await ctx.send(embed=embed)
                
                    else: 
                        await ctx.send("You do not have permission to use this command.")

                elif arg2 == "log":
                    if ctx.message.author.guild_permissions.administrator:
                        embed: discord.Emed = discord.Embed(
                            title="Log Channel",
                            description="Send the Channel ID that will replcae the old Log Channel.",
                            color=discord.Color.green()
                        )
                        embed.set_footer(text="You may say stop to stop the process")

                        await ctx.send(embed=embed)

                        msg = await self.client.wait_for("message", check=check)
                        log_update = msg.content

                        if msg.content == "stop":
                            await ctx.send("You have stop the update procces of the log channel")

                        else:
                            c.execute(f"""UPDATE role SET all_perm = {log_update}
                                    WHERE guild_ID = '{ctx.guild.id}'   
                                """)

                            conn.commit()
                            conn.close()

                            embed: discord.Embed = discord.Embed(
                                title="Moderation Log Channel Id Update",
                                description=f"The new Channel ID is\n\nModeration Log - <#{log_update}>",
                                color=discord.Color.green()
                            )

                            await ctx.send(embed=embed)
                
                    else: 
                        await ctx.send("You do not have permission to use this command.")



def setup(client):
	client.add_cog(Mod_Set_Up(client))