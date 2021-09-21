import discord
import os
from discord.ext import commands
from discord.ext.commands import BucketType
import asyncio
import random
import math
from dislash.slash_commands import slash_command
from dislash import *

class Games(commands.Cog):
    def __init__(self, client):
        self.client = client

    #rps
    @commands.command()
    async def rps(self, ctx, arg1=None):

        responses = [
            "Scissors", 
            "Paper", 
            "Rock"
            ]

        if arg1 == None:
            await ctx.send("Can you please chose one of the following **Rock, Paper, or Scissors**")

        elif arg1.lower() == "rock":
            embed: discord.Embed = discord.Embed(
                title="Rock Paper Scissors Results",
                description=f"You chose **Rock**\nBot chose **{random.choice(responses)}**", 
                color=discord.Color.green()
            )

            await ctx.send(embed=embed)

        elif arg1.lower() == "paper":
            embed: discord.Embed = discord.Embed(
                title="Rock Paper Scissors Results",
                description=f"You chose **Paper**\nBot chose **{random.choice(responses)}**",
                color=discord.Color.green()
            )

            await ctx.send(embed=embed)

        elif arg1.lower() == "scissors":
            embed: discord.Embed = discord.Embed(
                title="Rock Paper Scissors Results",
                description=f"You chose **Scissors**\nBot chose **{random.choice(responses)}**",
                color=discord.Color.green()
            )

            await ctx.send(embed=embed)
        else:
          await ctx.send("Please choose either **Rock, Paper, Or Scissors**\nExample - `d/rps rock`")
          
    @slash_commands.command(
        name="rps",
        description="lets you play rock paper scissors with Dinosaur",
        options=[
            Option("choice", "pice the item you want to play.", Type.STRING,
                choices=[
                    OptionChoice("Rock", "rock"),
                    OptionChoice("Paper", "paper"),
                    OptionChoice("Scissors", "scissors")
                ]
            )
        ]
    )
    async def slash_rps(self, ctx, choice=None):
        responses=[
            "Rock",
            "Scissors",
            "Paper"
        ]
        
        bot_repsonse = random.choice(responses)
        
        if choice == None:
            await ctx.reply("A error orcured try again.")
            
        elif choice == "rock":
            embed: discord.Embed = discord.Embed(
                title="Rock Paper Scissors Results",
                description=f"You chose **Rock**\nBot chose **{bot_repsonse}**", 
                color=discord.Color.green()
            )

            await ctx.reply(embed=embed)

        elif choice == "paper":
            embed: discord.Embed = discord.Embed(
                title="Rock Paper Scissors Results",
                description=f"You chose **Paper**\nBot chose **{bot_repsonse}**",
                color=discord.Color.green()
            )

            await ctx.reply(embed=embed)

        elif choice == "scissors":
            embed: discord.Embed = discord.Embed(
                title="Rock Paper Scissors Results",
                description=f"You chose **Scissors**\nBot chose **{bot_repsonse}**",
                color=discord.Color.green()
            )

            await ctx.reply(embed=embed)
            
        

    @commands.command()
    async def coinflip(self, ctx, arg1=None):

        responses=[
            "Head",
            "Tails"
        ]

        if arg1 == None:
            embed: discord.Embed = discord.Embed(
                title="Coinflip Results",
                description=f"The bot chose **{random.choice(responses)}**",
                color=discord.Color.green()
            )
            embed.set_footer(text="You can also do d/coinflip [heads or tails] to perdecit the results of the coinflip")

            await ctx.send(embed=embed)

        elif arg1.lower() == "heads":
            embed: discord.Embed = discord.Embed(
                title="Coinflip Results",
                description=f"You chose **Heads**\nThe bot chose **{random.choice(responses)}**",
                color=discord.Color.green()
            )

            await ctx.send(embed=embed)

        elif arg1.lower() == "tails":
            embed: discord.Embed = discord.Embed(
                title="Coinflip Results",
                description=f"You chose **Tails**\nThe bot chose **{random.choice(responses)}**",
                color=discord.Color.green()
            )

            await ctx.send(embed=embed)
        else:
          await ctx.send("Please choose either **Heads or Tails**")
          
    @slash_commands.command(
        name="coinflip",
        description="Allows you to predict a coinflip",
        options=[
            Option("choice", "pice the item you want to play.", Type.STRING,
                choices=[
                    OptionChoice("Tails", "tails"),
                    OptionChoice("Heads", "heads")
                ]
            )
        ]
    )
    async def slash_coinflip(self, ctx, choice=None):
        responses=[
            "Head",
            "Tails"
        ]
        
        if choice == None:
            await ctx.reply("Please when doing the slash command pick a side.")
            
        elif choice == "tails":
            embed: discord.Embed = discord.Embed(
                title="Coinflip Results",
                description=f"You chose **Tails**\nThe bot chose **{random.choice(responses)}**",
                color=discord.Color.green()
            )

            await ctx.reply(embed=embed)
            
        elif choice == "heads":
            embed: discord.Embed = discord.Embed(
                title="Coinflip Results",
                description=f"You chose **Heads**\nThe bot chose **{random.choice(responses)}**",
                color=discord.Color.green()
            )

            await ctx.reply(embed=embed)
    
    @commands.command()
    async def dice(self, ctx, arg1=None):

        sides=[
            "1",
            "2",
            "3",
            "4",
            "5",
            "6"
        ]
        
        bot_side = random.choice(sides)

        if arg1 == "1":
            embed: discord.Embed = discord.Embed(
                title="Dice Roll Results",
                description=f"You chose **1**\nThe Bot chose **{bot_side}**",
                color=discord.Color.green()
            )

            await ctx.send(embed=embed)

        elif arg1 == "2":
            embed: discord.Embed = discord.Embed(
                title="Dice Roll Results",
                description=f"You chose **2**\nThe Bot chose **{bot_side}**",
                color=discord.Color.green()
            )

            await ctx.send(embed=embed)

        elif arg1 == "3":
            embed: discord.Embed = discord.Embed(
                title="Dice Roll Results",
                description=f"You chose **3**\nThe Bot chose **{bot_side}**",
                color=discord.Color.green()
            )

            await ctx.send(embed=embed)

        elif arg1 == "4":
            embed: discord.Embed = discord.Embed(
                title="Dice Roll Results",
                description=f"You chose **4**\nThe Bot chose **{bot_side}**",
                color=discord.Color.green()
            )

            await ctx.send(embed=embed)

        elif arg1 == "5":
            embed: discord.Embed = discord.Embed(
                title="Dice Roll Results",
                description=f"You chose **5**\nThe Bot chose **{bot_side}**",
                color=discord.Color.green()
            )

            await ctx.send(embed=embed)

        elif arg1 == "6":
            embed: discord.Embed = discord.Embed(
                title="Dice Roll Results",
                description=f"You chose **6**\nThe Bot chose **{bot_side}**",
                color=discord.Color.green()
            )

            await ctx.send(embed=embed)

        elif arg1 == None:
            await ctx.send("Please do **d/dice [1, 2, 3, 4, 5, or 6]**")

        else:
            await ctx.send("Please do **d/dice [1, 2, 3, 4, 5, or 6]**")

    @commands.command(aliases=['8ball'])
    async def ball(self, ctx, *, message=None):
        responses=[
            "It is Certain.",
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

        if message == None:
            await ctx.send("Please do **d/8ball [message]** for the bot to predict!")

        else:
            msg = await ctx.send("https://tenor.com/view/8ball-bart-simpson-shaking-shake-magic-ball-gif-17725278")

            await asyncio.sleep(8)

            embed: discord.Emebed = discord.Embed(
                title="8ball Results",
                description=f"Your message - **{message}**\n8ball message - **{bot_responses}**",
                color=discord.Color.green()
            )

            await msg.edit(embed=embed)
            
    @slash_commands.command(
        name="8ball",
        description="Its a simple 8ball comamnds",
        options=[
            Option("message", "type what you would want to say.", Type.STRING, required=True)
        ]
    )
    async def slash_ball(self, ctx, message=None):
        print("hi")
        
        responses=[
            "It is Certain.",
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
        
        if message == None:
            await ctx.reply("Make sure you have a message for the 8ball")
            
        else:
            embed: discord.Emebed = discord.Embed(
                title="8ball Results",
                description=f"Your message - **{message}**\n8ball message - **{bot_responses}**",
                color=discord.Color.green()
            )

            await ctx.reply(embed=embed)
            

def setup(client):
	client.add_cog(Games(client))  