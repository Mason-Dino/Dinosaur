import discord
import os
from discord.ext import commands
from discord import app_commands
from discord.ext.commands import BucketType
#from PIL import Image
from io import BytesIO
import asyncio
import random
import math
import sqlite3
import datetime
import string

class Test(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def working_test(self, ctx):
        await ctx.send("hi")
            
    @commands.group()
    async def test_group(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("Invalid Sub Command")
            
    @test_group.command()
    async def phone(self, ctx):
        await ctx.send("phone")

    @app_commands.command(name="test", description="testing out stuff in discord.py")
    async def test(self, interaction: discord.Interaction):
        await interaction.response.send_message("hey")
        message = await interaction.original_response()
        print(message)

    @app_commands.command(name="pop", description="testing")
    async def pop(self, interaction: discord.Interaction):
        await interaction.response.send_message("hey")
        message = await interaction.original_response()

        def check():
            return message.author.id == interaction.user.id and message.channel.id == interaction.channel.id
        
        message = await self.client.wait_for("message",check = check)
        guess = message.content.lower()
        
        print(guess)


async def setup(client):
	await client.add_cog(Test(client)) 