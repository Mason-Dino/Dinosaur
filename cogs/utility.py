import discord
import os
from discord.ext import commands
from discord.ext.commands import BucketType
import asyncio
import random
import math
from dislash.slash_commands import slash_command
from dislash import *
#from time import time
#from psutil import *
from datetime import *


class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def feedback(self, ctx, *, message=None):
        feedback = self.client.get_channel(840422064975249418)
        user_id = ctx.message.author.id
        user_name = ctx.message.author

        if message == None:
            await ctx.send("Please provide some feedback that we can improve on!")
        
        else:
            embed: discord.Embed = discord.Embed(
                title="Feedback",
                description=f"<@!{user_id}> gave some feedback!",
                color=discord.Color.green()
            )
            embed.add_field(name="User Name:", value=f"{user_name}")
            embed.add_field(name="User ID:", value=f"{user_id}")
            embed.add_field(name="Feedback:", value=message, inline=False)

            await feedback.send(embed=embed)

            await ctx.send("Feedback Was Submitted!")

    @commands.command()
    async def bot(self, ctx):
        bot_version = "2.24.07"
        servers = len(self.client.guilds)
        members = sum([len(guild.members) for guild in self.client.guilds])
        dev = "<@!638092957756555291>"

        embed: discord.Embed = discord.Embed(
            title="Bot Infomation",
            description=f"Bot Version - {bot_version}\nServers - {servers}\nMembers - {members}\nBot Developer - {dev}",
            color=discord.Color.green()
        )

        await ctx.send(embed=embed)

    @commands.command()
    async def invite(self, ctx):
        await ctx.send("https://discord.com/oauth2/authorize?client_id=840025172861386762&permissions=2683662023&scope=bot%20applications.commands")

    @commands.command(aliases=['latency', 'lag'])
    async def ping(self, ctx):
        embed: discord.Embed = discord.Embed(
            title=":ping_pong: pong!",
            description=f'The Latency is {round(self.client.latency * 1000)}ms',
            color=discord.Color.green())
        await ctx.send(embed=embed)

    @commands.command()
    async def bug(self, ctx, *, message=None):
        bug = self.client.get_channel(842160990196203520)
        user_id = ctx.message.author.id
        user_name = ctx.message.author

        if message == None:
            await ctx.send("Please report the bug after you do the command.")

        else:
            embed: discord.Embed = discord.Embed(
                tilte="Bug Report",
                description=f"<@!{user_id}> Has reported a bug!!",
                color=discord.Color.green() 
            )
            embed.add_field(name="User Name:", value=f"{user_name}")
            embed.add_field(name="User ID:", value=f"{user_id}")
            embed.add_field(name="Bug:", value=message, inline=False)

            await bug.send(embed=embed)

            await ctx.send("The bug was reported!")

    @commands.command()
    async def servers(self, ctx):
        servers = len(self.client.guilds)

        await ctx.send(f"I'm in ``{servers}`` servers!")

    @commands.command()
    async def support(self, ctx):
        await ctx.send("If you need support with the bot please join discord.gg/KxPuFvazuF")
        
    
def setup(client):
	client.add_cog(Utility(client)) 