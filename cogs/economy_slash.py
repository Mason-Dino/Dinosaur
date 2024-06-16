#----------------------------------------------------------------------#
#
#       leaderboard: -lb, -top
#       Balance: -bal
#       Work: -work
#       Deposit: -dep
#       Withdraw: -with
#       Shop: -shop
#       Buy: -buy
#       Inventory: -inv
#       Use: -use
#       Slots: -slot
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

class Economy_Slash(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Leaderboard Command -top, -lb
    @app_commands.command(name="leaderboard", description="lets you see the top 10 people in dinosaur economy")
    async def slash_leaderboard(self, interaction: discord.Interaction):
        top_1 = results.top(place=1)
        top_2 = results.top(place=2)
        top_3 = results.top(place=3)
        top_4 = results.top(place=4)
        top_5 = results.top(place=5)
        top_6 = results.top(place=6)
        top_7 = results.top(place=7)
        top_8 = results.top(place=8)
        top_9 = results.top(place=9)
        top_10 = results.top(place=10)
        
        user_1 = self.client.get_user(top_1.user_ID())
        user_2 = self.client.get_user(top_2.user_ID())
        user_3 = self.client.get_user(top_3.user_ID())
        user_4 = self.client.get_user(top_4.user_ID())
        user_5 = self.client.get_user(top_5.user_ID())
        user_6 = self.client.get_user(top_6.user_ID())
        user_7 = self.client.get_user(top_7.user_ID())
        user_8 = self.client.get_user(top_8.user_ID())
        user_9 = self.client.get_user(top_9.user_ID())
        user_10 = self.client.get_user(top_10.user_ID())
        
        if user_1 == None:
            user_1_lb = top_1.user_ID()
            
        else:
            user_1_lb = user_1.name
            pass
            
        if user_2 == None:
            user_2_lb = top_2.user_ID()
            pass
            
        else:
            user_2_lb = user_2.name
            pass
        
        if user_3 == None:
            user_3_lb = top_3.user_ID()
            pass
            
        else:
            user_3_lb = user_3.name
            pass
        
        if user_4 == None:
            user_4_lb = top_4.user_ID()
            pass
            
        else:
            user_4_lb = user_4.name
            pass
        
        if user_5 == None:
            user_5_lb = top_5.user_ID()
            pass
            
        else:
            user_5_lb = user_5.name
            pass
        
        if user_6 == None:
            user_6_lb = top_6.user_ID()
            pass
            
        else:
            user_6_lb = user_6.name
            pass
        
        if user_7 == None:
            user_7_lb = top_7.user_ID()
            pass
            
        else:
            user_7_lb = user_7.name
            pass
        
        if user_8 == None:
            user_8_lb = top_8.user_ID()
            pass
            
        else:
            user_8_lb = user_8.name
            pass
        
        if user_9 == None:
            user_9_lb = top_9.user_ID()
            pass
            
        else:
            user_9_lb = user_9.name
            pass
            
        if user_10 == None:
            user_10_lb = top_10.user_ID()
            pass
            
        else:
            user_10_lb = user_10.name
            pass
        
        net_1 = top_1.net()
        net_2 = top_2.net()
        net_3 = top_3.net()
        net_4 = top_4.net()
        net_5 = top_5.net()
        net_6 = top_6.net()
        net_7 = top_7.net()
        net_8 = top_8.net()
        net_9 = top_9.net()
        net_10 = top_10.net()
        
        embed: discord.Embed = discord.Embed(
            title="Dinosaur Leaderboard",
            description=f"Below are the top 10 people\n\n:first_place: {user_1_lb} - {net_1}\n:second_place: {user_2_lb} - {net_2}\n:third_place: {user_3_lb} - {net_3}\n:medal: {user_4_lb} - {net_4}\n:medal: {user_5_lb} - {net_5}\n:medal: {user_6_lb} - {net_6}\n:medal: {user_7_lb} - {net_7}\n:medal: {user_8_lb} - {net_8}\n:medal: {user_9_lb} - {net_9}\n:medal: {user_10_lb} - {net_10}\n",
            color=discord.Color.green()
        )

        await interaction.response.send_message(embed=embed)

    #Balance Command -bal
    @app_commands.command(name="balance", description="It lets you see your current balance")
    async def slash_balance(self, interaction: discord.Interaction):
        view = results.view(user_ID=interaction.message.author.id)
        
        wallet = view.wallet()
        bank = view.bank()
        
        embed: discord.Embed = discord.Embed(
            title="Dinosaur Balace",
            description=f"{interaction.message.author.mention} Dinosaur Balance\n\nWallet Amount: **{wallet}**\n\nBank Amount: **{bank}**",
            color=discord.Color.green()
        )
        
        await interaction.response.send_message(embed=embed)

    #Work Command -work
    @app_commands.command(name="work", description="lets you work to earn dinosaur points")
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def slash_work(self, interaction: discord.Interaction):
        number = int(random.randint(5, 25))
        
        wallet = money.wallet(amount=number, user_ID=interaction.message.author.id)
        wallet.add()
            
        embed: discord.Embed = discord.Embed(
            title="Work",
            description=f"You gained **{number}** Dinosaur Points form working",
            color=discord.Color.green()
        )

        await interaction.response.send_message(embed=embed)

async def setup(client):
	await client.add_cog(Economy_Slash(client))