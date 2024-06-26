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
    @app_commands.describe(message="what are you wishing for...")
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
    async def slash_rps(self, interaction: discord.Interaction, choice: str):

        responses = [
            "Scissors", 
            "Paper", 
            "Rock"
            ]

        if choice == None:
            await interaction.response.send_message("Please chose one of the following: **Rock, Paper, or Scissors**")

        elif choice.lower() == "rock":
            embed: discord.Embed = discord.Embed(
                title="Rock Paper Scissors Results",
                description=f"You chose **Rock**\nBot chose **{random.choice(responses)}**", 
                color=discord.Color.green()
            )

            await interaction.response.send_message(embed=embed)

        elif choice.lower() == "paper":
            embed: discord.Embed = discord.Embed(
                title="Rock Paper Scissors Results",
                description=f"You chose **Paper**\nBot chose **{random.choice(responses)}**",
                color=discord.Color.green()
            )

            await interaction.response.send_message(embed=embed)

        elif choice.lower() == "scissors":
            embed: discord.Embed = discord.Embed(
                title="Rock Paper Scissors Results",
                description=f"You chose **Scissors**\nBot chose **{random.choice(responses)}**",
                color=discord.Color.green()
            )

            await interaction.response.send_message(embed=embed)
        else:
          await interaction.response.send_message("Please choose either **Rock, Paper, Or Scissors**\nExample - `d/rps rock`")

    #Coinflip Command -coin, -coinflip
    @app_commands.command(name="coinflip", description="let you predict a coin-flip or just flip a coin")
    async def slash_coinflip(self, interaction: discord.Interaction, choice: str=None):

        responses=[
            "Head",
            "Tails"
        ]

        if choice == None:
            embed: discord.Embed = discord.Embed(
                title="coin-flip Results",
                description=f"The bot chose **{random.choice(responses)}**",
                color=discord.Color.green()
            )
            embed.set_footer(text="You can also do d/coin-flip [heads or tails] to predict the results of the coin-flip")

            await interaction.response.send_message(embed=embed)

        elif choice.lower() == "heads" or choice.lower() == "head":
            embed: discord.Embed = discord.Embed(
                title="coin-flip Results",
                description=f"You chose **Heads**\nThe bot chose **{random.choice(responses)}**",
                color=discord.Color.green()
            )

            await interaction.response.send_message(embed=embed)

        elif choice.lower() == "tails" or choice.lower() == "tail":
            embed: discord.Embed = discord.Embed(
                title="coin-flip Results",
                description=f"You chose **Tails**\nThe bot chose **{random.choice(responses)}**",
                color=discord.Color.green()
            )

            await interaction.response.send_message(embed=embed)

        else:
          await interaction.response.send_message("Please choose either **Heads or Tails**")

    #Dice Command -dice
    @app_commands.command(name="dice", description="roll a dice")
    async def slash_dice(self, interaction: discord.Interaction, choice: str=None):

        sides=[
            "1",
            "2",
            "3",
            "4",
            "5",
            "6"
        ]
        
        bot_side = random.choice(sides)

        if choice == None:
            embed: discord.Embed = discord.Embed(
                title="Dice Roll Results",
                description=f"The Bot chose **{bot_side}**",
                color=discord.Color.green()
            )
            await interaction.response.send_message(embed = embed)
        else:
            if choice in sides:
                embed: discord.Embed = discord.Embed(
                title="Dice Roll Results",
                description=f"You chose **{choice}**\nThe Bot chose **{bot_side}**",
                color=discord.Color.green()
                )
                await interaction.response.send_message(embed = embed)
            else:
                await interaction.response.send_message("Invalid prediction, try **/dice [(optional) 1-6]**")

async def setup(client):
	await client.add_cog(Slash_Games(client))  