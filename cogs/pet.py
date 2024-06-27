#----------------------------------------------------------------------#
#
#
#
#----------------------------------------------------------------------#

import discord
import os
from discord.ext import commands
from discord.ext.commands import BucketType
from Disecon import *
import asyncio
import random
import math
import sqlite3

class Pet(commands.Cog):
    def __init__(self, client):
        self.client = client


async def setup(client):
	await client.add_cog(Pet(client))