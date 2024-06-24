#----------------------------------------------------------------------#
#               DONE WITH ALL SLASH COMMANDS IN ECON
#
#       -top
#
#       leaderboard: -lb, -top
#       Balance: -bal
#       Work: -work
#           Work Error: -work--cool, -work--error
#       Deposit: -dep
#       Withdraw: -with
#       Shop: -shop
#       Buy: -buy
#           Buy Error: -buy--cool, -buy--error
#       Inventory: -inv
#       Use: -use
#           Use Error: -use--cool, -use--error
#       Slots: -slot
#           Slots Error: -slot--cool, -slot--error
#
#----------------------------------------------------------------------#

import discord
import os
from discord.ext import commands
from discord import app_commands
from discord.ext.commands import BucketType
from Disecon import *
import asyncio
import random
import math
import sqlite3

class Pet_Slash(commands.Cog):
    def __init__(self, client):
        self.client = client

async def setup(client):
	await client.add_cog(Pet_Slash(client))