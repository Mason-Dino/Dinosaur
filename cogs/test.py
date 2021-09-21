import discord
import os
from discord.ext import commands
from discord.ext.commands import BucketType
#from PIL import Image
from io import BytesIO
import asyncio
import random
import math
import sqlite3
import datetime
import string
from dislash.slash_commands import slash_command
from dislash import *

class Test(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def working_test(self, ctx):
        await ctx.end("hi")
        
    @commands.command()
    async def button(self, ctx):
        row = ActionRow(
            Button(
                style=ButtonStyle.link,
                label="Click me!",
                #custom_id="test_button",
                url="https://www.google.com"
            )
        )
        msg = await ctx.send("I have a button!", components=[row])

    # Here timeout=60 means that the listener will
    # finish working after 60 seconds of inactivity
        on_click = msg.create_click_listener(timeout=30)

        @on_click.matching_id("test_button")
        async def on_test_button(inter):
            await inter.reply("You've clicked the button!")

        @on_click.timeout
        async def on_timeout():
            await msg.edit(components=[])   

def setup(client):
	client.add_cog(Test(client)) 