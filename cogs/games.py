import discord
import os
from discord.ext import commands
from discord.ext.commands import BucketType
import asyncio
import random
import math
from dislash.slash_commands import slash_command
from dislash import *
import json

class Games(commands.Cog):
    def __init__(self, client):
        self.client = client

    #wordle
    @commands.command()
    async def wordle(self, ctx, difficulty = None):
            def load_json(file):
                with open(file, "r") as f:
                    data = json.load(f)
                return data
            def logic(guess, ans):
              varr = list(ans)
              var = [0,0,0,0,0]
              guess = list(guess)
              for i in range(0,5):
                if guess[i] == varr[i]:
                  var[i] = 2
                  varr[i] = "-"
              for x in range(0,5):
                for y in range(0,5):
                  if guess[x] == varr[y]:
                    var[x] = 1
                    varr[y] = "-"
                    
              return(var)

            loop = True

            if difficulty == None:
                difficulty = 'easy'

            ans = 0
            if difficulty.lower() == 'easy':
                answer = load_json('cogs/words.json')
                answer = answer[0]
                answer = random.choice(answer)
                ans = 1
            if difficulty.lower() == 'hard':
                answer = load_json('cogs/words.json')
                answer = answer[1]
                answer = random.choice(answer)
                ans = 1
            if ans == 0:
                await ctx.send('Unknown difficulty, please retry with `easy`, `hard` or nothing')
            else:
                goal = 0
                guesses = []
                results = []
              
                await ctx.send("please guess the word: ")
                while loop == True:
                    if len(guesses) == 6:
                        await ctx.send(f"Sorry but you've ran out of guesses!\n The answer was {answer}")
                        break
                        return
                    else:
                        wlist = load_json("cogs/words.json")
                        wlist = wlist[1]
                  
                        def check(msg):
                          return msg.author == ctx.author and msg.channel.id == ctx.channel.id
                        
                        msg = await self.client.wait_for("message",check = check)
                        guess = msg.content.lower()
                        guessl = list(guess)
                        
                        if guess == "break":
                          await ctx.send('wordle deactivated')
                          break
                        if len(guessl) != 5:
                          await ctx.send("that guess is invalid because it is not 5 letters")
                        elif guess not in wlist:
                          await ctx.send("that isn't a real word")
                        else:
                  
                          
                          result = logic(guess, answer)
                          guess = "".join(guess)
                          guess = "`"+guess+"`"
                          guesses.append(guess)
                          
                          if result == [2,2,2,2,2]:
                            goal = 1
                          
                  
                  
                          for i in range(0, 5):
                            if result[i] == 1:
                              result[i] = ":orange_square:"
                            if result[i] == 0:
                              result[i] = ":red_square:"
                            if result[i] == 2:
                              result[i] = ":green_square:"
                  
                          result = "".join(result)
                          results.append(result)
                          
                          
                          embedstuff = []
                          for i in range(0,len(results)):
                            embedstuff.append(guesses[i])
                            embedstuff.append(results[i])
                            
                          embedstuff = "\n".join(embedstuff)
                        
                          if result != ':green_square::green_square::green_square::green_square::green_square:':
                              embed = discord.Embed(title = "Result:", description = embedstuff + "\n Please enter your next guess:", color=discord.Color.green())
                              await ctx.send(embed = embed)
                          else:
                            embed = discord.Embed(title = f"Correct, you got the word in {len(guesses)}!", description = embedstuff, color=discord.Color.green())
                            await ctx.send(embed = embed)
                            break


    #rps
    @commands.command()
    async def rps(self, ctx, arg1=None):

        responses = [
            "Scissors", 
            "Paper", 
            "Rock"
            ]

        if arg1 == None:
            await ctx.send("Please chose one of the following: **Rock, Paper, or Scissors**")

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
            await ctx.reply("An error occured, please try again.")
            
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
            embed.set_footer(text="You can also do d/coinflip [heads or tails] to predict the results of the coinflip")

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
            Option("choice", "pick the item you want to play.", Type.STRING,
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

        if arg1 == None:
            embed: discord.Embed = discord.Embed(
                title="Dice Roll Results",
                description=f"The Bot chose **{bot_side}**",
                color=discord.Color.green()
            )
            await ctx.send(embed = embed)
        else:
            if arg1 in sides:
                embed: discord.Embed = discord.Embed(
                title="Dice Roll Results",
                description=f"You chose **{arg1}**\nThe Bot chose **{bot_side}**",
                color=discord.Color.green()
                )
                await ctx.send(embed = embed)
            else:
                await ctx.send("Invalid prediction, try **d/dice [(optional) 1-6]**")

    @commands.command(aliases=['8ball'])
    async def ball(self, ctx, *, message=None):
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