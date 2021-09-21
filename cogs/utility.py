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
        
    
    #feedback
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
            
    @slash_commands.command(
        name="feedback",
        description="It allows you to give feedback about Dinosaur",
        options=[
            Option("feedback",  "this is where you give the feedback", Type.STRING, required=True)
        ]
    )
    async def slash_feedback(self, ctx, feedback=None):
        feedback_channel = self.client.get_channel(840422064975249418)
        
        if feedback == None:
            await ctx.reply("Please provide some feedback!")
            
        else:
            embed: discord.Embed = discord.Embed(
                title="Feedback",
                description=f"<@!{ctx.author.id}> gave some feedback!",
                color=discord.Color.green()
            )
            embed.add_field(name="User Name:", value=f"{ctx.author}")
            embed.add_field(name="User ID:", value=f"{ctx.author.id}")
            embed.add_field(name="Feedback:", value=feedback, inline=False)

            await feedback_channel.send(embed=embed)

            await ctx.reply("Feedback Was Submitted!")

    #bot
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
        
    @slash_commands.command(
        name="bot",
        description="shows you some infomation about the discord bot."
    )
    async def slash_bot(self, ctx):
        bot_version = "2.24.07"
        servers = len(self.client.guilds)
        members = sum(len(guild.members) for guild in self.client.guilds)
        dev = "<@!638092957756555291>"
        test="none"

        embed: discord.Embed = discord.Embed(
            title="Bot Infomation",
            description=f"Bot Version - {bot_version}\nServers - {servers}\nMembers - {members}\nBot Developer - {dev}",
            color=discord.Color.green()
        )

        await ctx.reply(embed=embed)

    #invite command
    @commands.command()
    async def invite(self, ctx):
        await ctx.send("https://discord.com/oauth2/authorize?client_id=840025172861386762&permissions=2683662023&scope=bot%20applications.commands")

    
    @slash_commands.command(
        name="invite",
        description="It gives you a invite link for the discord bot."
    )
    async def slash_invite(self, ctx):
        await ctx.reply("https://discord.com/oauth2/authorize?client_id=840025172861386762&permissions=2683662023&scope=bot%20applications.commands")
    
    #ping commands
    @commands.command(
        aliases=['latency', 'lag']    
    )
    async def ping(self, ctx):
        embed: discord.Embed = discord.Embed(
            title=":ping_pong: pong!",
            description=f'The Latency is {round(self.client.latency * 1000)}ms',
            color=discord.Color.green()
        )
        
        await ctx.send(embed=embed)
        
    @slash_commands.command(
        name="ping",
        description="It shows the ping of the bot.",
        guild_ids=[840354954074128405]
    )
    async def slash_ping(self, ctx):
        embed: discord.Embed = discord.Embed(
            title=":ping_pong: pong!",
            description=f"The Latency is {round(self.client.latency * 1000)}ms",
            color=discord.Color.green()
        )
        
        await ctx.reply(embed=embed)

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
            
    @slash_commands.command(
        name="bug",
        description="It allows you to report a bug if there is one.",
        options=[
            Option("bug",  "this is where you will report the bug.", Type.STRING, required=True)    
        ]
    )
    async def slash_bug(self, ctx, bug=None):
        bug_channel = self.client.get_channel(842160990196203520)
        user_id = ctx.author.id
        user_name = ctx.author

        if bug == None:
            await ctx.send("Please report the bug after you do the command.")

        else:
            embed: discord.Embed = discord.Embed(
                tilte="Bug Report",
                description=f"<@!{user_id}> Has reported a bug!!",
                color=discord.Color.green() 
            )
            embed.add_field(name="User Name:", value=f"{user_name}")
            embed.add_field(name="User ID:", value=f"{user_id}")
            embed.add_field(name="Bug:", value=bug, inline=False)

            await bug_channel.send(embed=embed)

            await ctx.reply("The bug was reported!")

    
    #servers commands
    @commands.command()
    async def servers(self, ctx):
        servers = len(self.client.guilds)

        await ctx.send(f"I'm in ``{servers}`` servers!")
        
        
    @slash_commands.command(
        name="servers",
        description="allows you to see the ammount of servers Dinosaur is in"
    )
    async def slash_servers(self, ctx):
        servers = len(self.client.guilds)
        
        await ctx.reply(f"I'm in `{servers}` servers!")

    
    #support commadns
    @commands.command()
    async def support(self, ctx):
        await ctx.send("If you ever need support with Dinosaur join with the link bellow\nhttps://discord.gg/KxPuFvazuF")
            
    @slash_commands.command(
        name="support",
        description="If you ever need support with Dinosaur this is the command for you."
    )
    async def slash_support(self, ctx):
        await ctx.reply("If you ever need support with Dinosaur join with the link bellow\nhttps://discord.gg/KxPuFvazuF")
        
    
def setup(client):
	client.add_cog(Utility(client)) 