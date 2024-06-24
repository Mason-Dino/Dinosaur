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

    #8ball Command: -ball, -8ball
    @app_commands.command(name="8ball", description="let you mess around with an 8 ball")
    async def slash_ball(self, interaction: discord.Interaction, message: str):
        responses=[
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."
        ]

        bot_responses = random.choice(responses)

        msg = await interaction.response.send_message("https://tenor.com/view/8ball-bart-simpson-shaking-shake-magic-ball-gif-17725278")

        await asyncio.sleep(8)

        embed: discord.Embed = discord.Embed(
            title="8ball Results",
            description=f"Your message - **{message}**\n8ball message - **{bot_responses}**",
            color=discord.Color.green()
        )

        await interaction.edit_original_response(content="", embed=embed)

    #RPS Command -rps
    @app_commands.command(name="rps", description="play rock paper scissors with dinosaur")
    async def rps(self, interaction: discord.Interaction, arg1: str):

        responses = [
            "Scissors", 
            "Paper", 
            "Rock"
            ]

        if arg1 == None:
            await interaction.response.send_message("Please chose one of the following: **Rock, Paper, or Scissors**")

        elif arg1.lower() == "rock":
            embed: discord.Embed = discord.Embed(
                title="Rock Paper Scissors Results",
                description=f"You chose **Rock**\nBot chose **{random.choice(responses)}**", 
                color=discord.Color.green()
            )

            await interaction.response.send_message(embed=embed)

        elif arg1.lower() == "paper":
            embed: discord.Embed = discord.Embed(
                title="Rock Paper Scissors Results",
                description=f"You chose **Paper**\nBot chose **{random.choice(responses)}**",
                color=discord.Color.green()
            )

            await interaction.response.send_message(embed=embed)

        elif arg1.lower() == "scissors":
            embed: discord.Embed = discord.Embed(
                title="Rock Paper Scissors Results",
                description=f"You chose **Scissors**\nBot chose **{random.choice(responses)}**",
                color=discord.Color.green()
            )

            await interaction.response.send_message(embed=embed)
        else:
          awai interaction.response.send_message("Please choose either **Rock, Paper, Or Scissors**\nExample - `d/rps rock`")
    

async def setup(client):
	await client.add_cog(Slash_Games(client))  