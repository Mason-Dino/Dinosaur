#----------------------------------------------------------------------#
#
#       help: -help
#
#----------------------------------------------------------------------#

import discord
from discord.ext import commands
from discord import app_commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Help Command
    @commands.command()
    async def help(self, ctx, arg1=None, arg2=None):
        if arg1 == None:
            embed: discord.Embed = discord.Embed(
                title="**Help**",
                description="Below are all the help commands that you can do to see all the different commands that we have.",
                color=discord.Color.green()
            )
            embed.add_field(name="**Game Help**", value="**d/help game** - info about the game commands.", inline=False)
            embed.add_field(name="**Utility Help**", value="**d/help utility** - info about utility commands.", inline=False)
            embed.add_field(name="**Economy Help**", value="**d/help economy** - info about economy commands", inline=False)
            #embed.add_field(name="**Moderation Help**", value="**d/help moderation** or **d/help mod** - shows 3 sub-categories of moderation commands", inline=False)
            embed.add_field(name="**Support Links**", value="[Support Server](https://discord.gg/KxPuFvazuF)\n[Invite The Bot](https://discord.com/api/oauth2/authorize?client_id=840025172861386762&permissions=2683662023&scope=bot)\n[top.gg Profile](https://top.gg/bot/840025172861386762)")

            await ctx.send(embed=embed, suppress_embeds=False)
        
        elif arg1 == "game":
            embed: discord.Embed = discord.Embed(
                title="**Game Help**",
                description="Below are all the Game commands that we have at the moment.",
                color=discord.Color.green()
            )
            embed.add_field(name="**Rock Paper Scissors**", value="**d/rps [Rock, Paper, or Scissors]** - initiates rock paper scisors with the bot.", inline=False)
            embed.add_field(name="**Coinflip**", value="**d/coinflip (optional) [heads or tails]** - virtual coinflip.", inline=False)
            embed.add_field(name="**Dice Roll**", value="**d/dice [1, 2, 3, 4, 5, or 6]**. If you do that you can perdict a dice roll.", inline=False)
            embed.add_field(name="**8ball**", value="**d/8ball [message]** then the bot will just be like a 8ball.", inline=False)
            embed.add_field(name="**Wordle**", value ="**d/wordle (optional) [easy or hard]** - initiates a game of wordle", inline=False)

            await ctx.send(embed=embed)

        elif arg1 == "utility":
                embed: discord.Embed = discord.Embed(
                    title="**Utility Help**",
                    description="Below are all the Utility commands that we have at the moment.",
                    color=discord.Color.green()
                )
                embed.add_field(name="**Support**", value="If you do **d/support** you will be able to join our support server.", inline=False)
                embed.add_field(name="**Ping**", value="If you do **d/ping** you can find the ping of the bot right now.", inline=False)
                embed.add_field(name="**Invite**", value="If you do **d/invite** it will send the invite link for the bot.", inline=False)
                embed.add_field(name="**Bot Infomation**", value="If you do **d/bot** you can find out some of the infomation about Dinosaur Bot.", inline=False)
                embed.add_field(name="**Servers**", value="If you do **d/servers** it will show the number of servers the bot is in.", inline=False)
                embed.add_field(name="**Feedback**", value="If you do **d/feedback [message]** you can give us feedback about the bot.", inline=False)
                embed.add_field(name="**Bug Report**", value="If you do **d/bug [report]**. I will see that there is a bug and I will be working on it as soon as I can.", inline=False)
                embed.add_field(name="Uptime", value="If you do **d/uptime** you can see the uptime for the bot.", inline=False)
                #embed.add_field(name="**Change Log**", value="If you do **d/change** you can see the most recent change log of the bot.")

                await ctx.send(embed=embed)

        elif arg1 == "economy":
            embed: discord.Embed = discord.Embed(
                title="**Economy Help**",
                description="Below are all the Economy commands that you can use with Dinosaur Points.",
                color=discord.Color.green()

            )
            embed.add_field(name="**Balance**", value="If you do **d/bal** it will give you the amount of Dinosaur Points you have currently.", inline=False)
            embed.add_field(name="**Work**", value="If you do **d/work** it will give you between 5 and 25 Dinosaur Points.", inline=False)
            embed.add_field(name="**Deposit**", value="If you do **d/dep all** or **d/dep [amount]** it will deposit all or the ammount you want into your Dinosaur Points bank.", inline=False)
            embed.add_field(name="**Withdraw**", value="If you do **d/with all** or **d/with [amount]** it will withdraw all or the ammount you want from your Dinosaur Points bank.", inline=False)
            embed.add_field(name="**Leaderboard**", value="If you do **d/leaderboard**, **d/lb**, and **d/top** you will get the top 10 people of the Dinosaur Economy", inline=False)
            embed.add_field(name="**Shop**", value="If you do **d/shop** it will show you all the items that we have in our shop at that time.", inline=False)
            embed.add_field(name="**Inventory**", value="If you do **d/inv** it will show all the items you have in your inventory.", inline=False)
            embed.add_field(name="**Buy**", value="If you do **d/buy [shop ID] [(optional) amount]** you will buy that item from the shop", inline=False)
            embed.add_field(name="**Use**", value="If you do **d/use [shop ID] [(optional) amount]** it will use the item. But you have to have it in your inventory", inline=False)
            #embed.add_field(name="**Gamble Help**", value="If you do **d/gamble help** it will give you the gamble commands that we have at the moment.")

            await ctx.send(embed=embed)

        elif arg1 == "mod" or arg1 == "moderation":
            await ctx.send(":construction: Coming Soon! :construction:")


        @app_commands.commands(name="ping", description="you can see what the ping is of the bot")
        @app_commands.guilds(discord.Object(840354954074128405))
        async def slash_ping(self, ctx: discord.Interaction):
            bot_latency = round(self.client.latency * 1000)
            await ctx.response.send_message(f"Pong! {bot_latency} ms.")


async def setup(client):
    await client.add_cog(Help(client))
