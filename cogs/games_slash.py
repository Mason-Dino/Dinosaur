#----------------------------------------------------------------------#
#
#       Wordle: -wordle
#       RPS: -rps
#       Coinflip: -coin, -coinflip
#       Dice: -dice
#       8ball: -ball, -8ball
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
import json

class Slash_Games(commands.Cog):
    def __init__(self, client):
        self.client = client
            

async def setup(client):
	await client.add_cog(Slash_Games(client))  