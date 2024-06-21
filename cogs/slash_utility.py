#----------------------------------------------------------------------#
#
#       Feeback: -feedback
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

    

async def setup(client):
	await client.add_cog(Utility_Slash(client))