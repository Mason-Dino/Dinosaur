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


async def setup(client):
	await client.add_cog(Utility_Slash(client))