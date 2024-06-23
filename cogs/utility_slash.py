#----------------------------------------------------------------------#
#
#       Feedback: -feedback
#       Bot: -bot
#       Invite -invite
#       Ping: -ping
#       Bug: -bug
#       Servers: -servers
#       Support: -support
#       Uptime: -uptime
#
#----------------------------------------------------------------------#

import discord
import os
from discord.ext import commands
from discord import app_commands
from discord.ext.commands import BucketType
import asyncio
import random
import math
import psutil
import time
from functions.version import version
from functions.dev import developers

class Utility_Slash(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="bot", description="lets you see information about the bot")
    async def slash_bot(self, interaction: discord.Interaction):
        bot_version = version()
        servers = len(self.client.guilds)
        members = sum([len(guild.members) for guild in self.client.guilds])
        dev = developers()

        embed: discord.Embed = discord.Embed(
            title="Bot Information",
            description=f"Bot Version - {bot_version}\nServers - {servers}\nMembers - {members}\nBot Developer - {dev}",
            color=discord.Color.green()
        )

        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="invite", description="invite dinosaur discord bot")
    async def slash_invite(self, interaction: discord.Interaction):
        embed: discord.Embed = discord.Embed(
            name="**Invite Dinosaur!**",
            description="[Invite Link](https://discord.com/oauth2/authorize?client_id=840025172861386762&permissions=2683662023&scope=bot%20applications.commands)",
            color=discord.Color.green()
        )

        await interaction.response.send_message(embed=embed)

    #Ping Command -ping
    @app_commands.command(name="ping", description="get the latency of the bot")
    async def ping(self, interaction: discord.Interaction):
        embed: discord.Embed = discord.Embed(
            title=":ping_pong: pong!",
            description=f'The Latency is {round(self.client.latency * 1000)}ms',
            color=discord.Color.green()
        )
        
        await interaction.response.send_message(embed=embed)

    #Servers Command -servers
    @app_commands.command(name="servers", description="lets you see the number of servers")
    async def slash_servers(self, interaction: discord.Interaction):
        servers = len(self.client.guilds)

        await interaction.response.send_message(f"I'm in ``{servers}`` servers!")

    #Support Command -support
    @app_commands.command(name="support", description="join to get support with dinosaur")
    async def slash_support(self, interaction: discord.Interaction):
        embed: discord.Embed = discord.Embed(
            title="**Support Sever**",
            description="Join for Dinosaur Support\n[Support Server](https://discord.gg/KxPuFvazuF)",
            color=discord.Color.green()
        )

        await interaction.response.send_message(embed=embed)

    #Uptime Command -uptime
    @app_commands.command(name="uptime", description="see how long the bot has been running for")
    async def slash_uptime(self, interaction: discord.Interaction):
        p = psutil.Process(os.getpid())
        p.create_time()

        secUptime = int(p.create_time())

        #<t:1649334120:f>

        uptime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(p.create_time()))

        uptime = f"<t:{secUptime}:f>"

        embed: discord.Embed = discord.Embed(
            title="Uptime",
            description=f"The bot has been online sense {uptime}",
            color=discord.Color.green()
        )

        await interaction.response.send_message(embed=embed)

async def setup(client):
	await client.add_cog(Utility_Slash(client))