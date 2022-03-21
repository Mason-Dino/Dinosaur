import discord
from discord.ext import commands
from dislash.slash_commands import slash_command
from dislash import *

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

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
            embed.add_field(name="**Moderation Help**", value="**d/help moderation** or **d/help mod** - shows 3 sub-categories of moderation commands", inline=False)
            embed.add_field(name="**Support Links**", value="[Support Server](https://discord.gg/KxPuFvazuF)\n[Invite The Bot](https://discord.com/api/oauth2/authorize?client_id=840025172861386762&permissions=2683662023&scope=bot)\n[top.gg Profile](https://top.gg/bot/840025172861386762)")

            await ctx.send(embed=embed)
        
        elif arg1 == "game":
            embed: discord.Embed = discord.Embed(
                title="**Game Help**",
                description="Below are all the Game commands that we have at the momment.",
                color=discord.Color.green()
            )
            embed.add_field(name="**Rock Paper Scissors**", value="**d/rps [Rock, Paper, or Scissors]** - initiates rock paper scisors with the bot.", inline=False)
            embed.add_field(name="**Coinflip**", value="**d/coinflip (optional) [heads or tails]** - virtual coinflip.", inline=False)
            embed.add_field(name="**Dice Roll**", value="**d/dice [1, 2, 3, 4, 5, or 6]**. If you do that you can perdict a dice roll.", inline=False)
            embed.add_field(name="**8ball**", value="**d/8ball [message]** then the bot will just be like a 8ball.", inline=False)
            embed.add_field(name="**Wordle**", value ="**d/wordle (optional) [easy or hard]** - initates a game of wordle", inline=False)

            await ctx.send(embed=embed)

        elif arg1 == "utility":
                embed: discord.Embed = discord.Embed(
                    title="**Utility Help**",
                    description="Below are all the Utility commands that we have at the momment.",
                    color=discord.Color.green()
                )
                embed.add_field(name="**Support**", value="If you do **d/support** you will be able to join our support server.", inline=False)
                embed.add_field(name="**Ping**", value="If you do **d/ping** you can find the ping of the bot right now.", inline=False)
                embed.add_field(name="**Invite**", value="If you do **d/invite** it will send the invite link for the bot.", inline=False)
                embed.add_field(name="**Bot Infomation**", value="If you do **d/bot** you can find out some of the infomation about Dinosaur Bot.", inline=False)
                embed.add_field(name="**Servers**", value="If you do **d/servers** it will show the number of servers the bot is in.", inline=False)
                embed.add_field(name="**Feedback**", value="If you do **d/feedback [message]** you can give us feedback about the bot.", inline=False)
                embed.add_field(name="**Bug Report**", value="If you do **d/bug [report]**. I will see that there is a bug and I will be working on it as soon as I can.", inline=False)
                #embed.add_field(name="**Change Log**", value="If you do **d/change** you can see the most recent change log of the bot.")

                await ctx.send(embed=embed)

        elif arg1 == "economy":
            embed: discord.Embed = discord.Embed(
                title="**Economy Help**",
                description="Below are all the Economy commands that you can use with Dinosaur Points.",
                color=discord.Color.green()

            )
            embed.add_field(name="**Balance**", value="If you do **d/bal** it will give you the ammount of Dinosaur Points you have currently.", inline=False)
            embed.add_field(name="**Work**", value="If you do **d/work** it will give you between 5 and 25 Dinosaur Points.", inline=False)
            embed.add_field(name="**Deposit**", value="If you do **d/dep all** or **d/dep set [ammount]** it will deposit all or the ammount you want into your Dinosaur Points bank.", inline=False)
            embed.add_field(name="**Withdraw**", value="If you do **d/with all** or **d/with set [ammount]** it will withdraw all or the ammount you want from your Dinosaur Points bank.", inline=False)
            embed.add_field(name="**Leaderboard**", value="If you do **d/leaderboard**, **d/lb**, and **d/top** you will get the top 10 people of the Dinosaur Economy", inline=False)
            embed.add_field(name="**Shop**", value="If you do **d/shop** it will show you all the items that we have in our shop at that time.", inline=False)
            embed.add_field(name="**Inventory**", value="If you do **d/inv** it will show all the items you have in your inventory.", inline=False)
            embed.add_field(name="**Buy**", value="If you do **d/buy [shop ID or name]** you will buy that item from the shop", inline=False)
            embed.add_field(name="**Use**", value="If you do **d/use [shop ID or name]** it will use the item. But you have to have it in your inventory", inline=False)
            #embed.add_field(name="**Gamble Help**", value="If you do **d/gamble help** it will give you the gamble commands that we have at the moment.")

            await ctx.send(embed=embed)

        elif arg1 == "moderation" or arg1 == "mod":
            if arg2 == None:
                embed: discord.Embed = discord.Embed(
                    title="**Moderation Help**",
                    description="Bellow are all the Moderation commands that we have.",
                    color=discord.Color.green()
                )
                embed.add_field(name="**Set Up**", value="If you do **d/help moderation set** it will show you all the moderation set up commands")
                embed.add_field(name="**Commands**", value="If you do **d/help moderation commands** it will show you all the moederation commands that we have at the momment")
                embed.add_field(name="**Mute**", value="If you do **d/help moderation search** it will show all the search moderation commands that we have.")


                await ctx.send(embed=embed)
            if arg2 == "set":
                embed: discord.Embed = discord.Embed(
                    title="**Moderation Help Setup**",
                    description="Bellow are all the Moderation Set Up comands that we have.",
                    color=discord.Color.green()
                )
                embed.add_field(name="**Moderation Set Up**", value="If you do **d/moderation start** it will allow you set up the diffrent moderation commands that we have. Look above for all the diffrent commands.\nPerms - Server Admin", inline=False)
                embed.add_field(name="**Moderation Info**", value="If you do **d/moderation info** this will allow you to see what roles have each perms.\nPerms - Server Admin", inline=False)
                embed.add_field(name="**Moderation Update**", value="If you do **d/moderation update [command]** it will allow you to update each of the moderation commands.\nPerms - Sever Admin", inline=False)

                await ctx.send(embed=embed)

            elif arg2 == "command" or arg2 == "commands":
                embed: discord.Embed = discord.Embed(
                    title="**Moderation Help Commands**",
                    description="Bellow are all the Moderation commands that we have.",
                    color=discord.Color.green()
                )
                embed.add_field(name="**Warn**", value="If you do **d/warn [user] [reason]** it will warn the user.\nPerms - Warn +", inline=False)
                embed.add_field(name="**Tempmute**", value="If you do **d/tempmute [user] [time] [reason]** it will tempmute the user for the time you said.\nPerms - Tempmute +", inline=False)
                embed.add_field(name="**Mute**", value="If you do **d/mute [user] [reason]** it will mute the user for ever if you don't unmute them.\nPerms - Mute +", inline=False)
                embed.add_field(name="**Unmute**", value="If you do **d/unmute [user]** it will unmute the user you said.\nPerms - Unmute +", inline=False)
                embed.add_field(name="**Kick**", value="If you do **d/kick [user] [reason]** it will kick the user from the server for that reason.\nPerms - Kick +", inline=False)
                embed.add_field(name="**Delete Infraction**", value="If you do **d/delete [case ID]** it will allow you to delete that infraction form the database. This is permanent.\nPerms - Delete Inf +")
                embed.add_field(name="**Ban**", value="If you do **d/ban [user] [reason]** it will ban the user from the server.\nPerms - Ban +", inline=False)
                embed.add_field(name="**Unban**", value="If you do **d/unban [user]** it will let you unban a user from the discord server. Note - only accepts tags, not IDs.\nPerms - Unban +")

                await ctx.send(embed=embed)

            elif arg2 == "search":
                embed: discord.Embed = discord.Embed(
                    title="**Moderation Help Search**",
                    description="Bellow are all the Moderation Search commands that we have",
                    color=discord.Color.green()
                )
                embed.add_field(name="**Mod Search**", value="If you do **d/mod [optional user]** it will search all for moderation commands that that use has done.\nPerms - Warn +", inline=False)
                embed.add_field(name="**User Search**", value="If you do **d/user [optional user]** it will search for infractions that the users has been givin.\nPerms - Warn +", inline=False)
                embed.add_field(name="**Case**", value="If you do **d/case [case ID]** it will give you the infomation of that case.\nPerms - Warn +", inline=False)
                embed.add_field(name="**Search All**", value="If you do **d/search all** it will show the 5 most recent infractions.\nPerms - Warn +", inline=False)
                embed.add_field(name="**Recent**", value="If you do **d/search recent** it will give you the infomation of the most recent infraction.\nPerms - Warn +", inline=False)
                embed.add_field(name="**Delete**", value="If you do **d/delete [case ID]** it will allow you to delete a case\nPerms - Delete inf +")

                await ctx.send(embed=embed)

    @slash_commands.command(
        name="help",
        description="this command allows you to get help with Dinosaur",
        guild_ids=[840354954074128405],
        options=[
            Option("sub", "this is where you can pick what subcategory you need help with.", Type.STRING,
                choices=[
                    OptionChoice("economy", "economy"),
                    OptionChoice("utility", "utility"),
                    OptionChoice("game", "game"),
                    OptionChoice("moderation set up", "moderation_set_up"),
                    OptionChoice("moderation commands", "moderation_commands"),
                    OptionChoice("moderation search", "moderation_search")
                ]
            )
        ]
    )
    async def slash_help(self, ctx, sub=None):
        if sub == None:
            embed: discord.Embed = discord.Embed(
                title="**Help**",
                description="Below are all the help commands that you can do to see all the diffrrent commands that we have.",
                color=discord.Color.green()
            )
            embed.add_field(name="**Game Help**", value="If you do **d/help game** you can find out all the games that we have.", inline=False)
            embed.add_field(name="**Utility Help**", value="If you do **d/help utility** it will give you all the utility commands that we have.", inline=False)
            embed.add_field(name="**Economy Help**", value="If you do **d/help economy** is will give all the economy commands that we have.", inline=False)
            embed.add_field(name="**Moderation Help**", value="If you do **d/help moderation** or **d/help mod** it will show you the 3 subcategories for all the moderation comamnds", inline=False)
            embed.add_field(name="**Support Links**", value="[Support Server](https://discord.gg/KxPuFvazuF)\n[Invite The Bot](https://discord.com/api/oauth2/authorize?client_id=840025172861386762&permissions=2683662023&scope=bot)\n[top.gg Profile](https://top.gg/bot/840025172861386762)")

            await ctx.reply(embed=embed)
            
        elif sub == "economy":
            embed: discord.Embed = discord.Embed(
                title="**Economy Help**",
                description="Below are all the Economy commands that you can use and all the command you can use with Dinosaur Points.",
                color=discord.Color.green()

            )
            embed.add_field(name="**Balance**", value="If you do **d/bal** it will give you the ammount of Dinosaur Points you have currently.", inline=False)
            embed.add_field(name="**Work**", value="If you do **d/work** it will give you anyway from 5 to 25 Dinosaur Points.", inline=False)
            embed.add_field(name="**Deposit**", value="If you do **d/dep all** or **d/dep set [ammount]** it will deposit all or the ammount you want into your Dinosaur Points bank.", inline=False)
            embed.add_field(name="**Withdraw**", value="If you do **d/with all** or **d/with set [ammount]** it will withdraw all or the ammount you want from your Dinosaur Points bank.", inline=False)
            embed.add_field(name="**Shop**", value="If you do **d/shop** it will show you all the items that we have in our shop at that time.", inline=False)
            embed.add_field(name="**Inventory**", value="If you do **d/inv** it will show all the items you have in your inventory.", inline=False)
            embed.add_field(name="**Buy**", value="If you do **d/buy [shop ID or name]** you will buy that item from the shop", inline=False)
            embed.add_field(name="**Use**", value="If you do **d/use [shop ID or name]** it will use the item. But you have to have it in your inventory", inline=False)
            #embed.add_field(name="**Gamble Help**", value="If you do **d/gamble help** it will give you the gamble commands that we have at the moment.")
            
            await ctx.reply(embed=embed)
            
        elif sub == "utility":
            embed: discord.Embed = discord.Embed(
                    title="**Utility Help**",
                    description="Below are all the Utility commands that we have at the momment.",
                    color=discord.Color.green()
                )
            
            embed.add_field(name="**Support**", value="If you do **d/support** you will be able to join our support server.", inline=False)
            embed.add_field(name="**Ping**", value="If you do **d/ping** you can find the ping of the bot right now.", inline=False)
            embed.add_field(name="**Invite**", value="If you do **d/invite** it will send the invite of the bot.", inline=False)
            embed.add_field(name="**Bot Infomation**", value="If you do **d/bot** you can figuar out some of the infomation about Dinosaur Bot.", inline=False)
            embed.add_field(name="**Servers**", value="If you do **d/servers** it will show the number of servers the bot is in.", inline=False)
            embed.add_field(name="**Feedback**", value="If you do **d/feedback [message]** you can give us feedback about the bot.", inline=False)
            embed.add_field(name="**Bug Report**", value="If you do **d/bug [report]**. I will see that there is a bug and I will be working on it as soon as I can.", inline=False)
            #embed.add_field(name="**Change Log**", value="If you do **d/change** you can see the most recent change log of the bot.")
            
            await ctx.reply(embed=embed)
            
        elif sub == "game":
            embed: discord.Embed = discord.Embed(
                title="**Game Help**",
                description="Below are all the Game commands that we have at the momment.",
                color=discord.Color.green()
            )
            embed.add_field(name="**Rock Paper Scissors**", value="If you do **d/rps [Rock, Paper, or Scissors]** you can play rock paper scissors with the bot.", inline=False)
            embed.add_field(name="**Coinflip**", value="You can do **d/coinflip [heads or tails]** and you can guess the coinflip or you can just do d/coinflip and that will do just a normal coinflip.", inline=False)
            embed.add_field(name="**Dice Roll**", value="If you do **d/dice [1, 2, 3, 4, 5, or 6]**. If you do that you can perdict a dice roll.", inline=False)
            embed.add_field(name="**8ball**", value="If you do **d/8ball [message]** then the bot will just be like a 8ball.", inline=False)
            
            await ctx.reply(embed=embed)
            
        elif sub == "moderation_set_up":
            embed: discord.Embed = discord.Embed(
                title="**Moderation Help Setup**",
                description="Bellow are all the Moderation Set Up comands that we have.",
                color=discord.Color.green()
            )
            embed.add_field(name="**Moderation Set Up**", value="If you do **d/moderation start** it will allow you set up the diffrent moderation commands that we have. Look above for all the diffrent commands.\nPerms - Server Admin", inline=False)
            embed.add_field(name="**Moderation Info**", value="If you do **d/moderation info** this will allow you to see what roles have each perms.\nPerms - Server Admin", inline=False)
            embed.add_field(name="**Moderation Update**", value="If you do **d/moderation update [command]** it will allow you to update each of the moderation commands.\nPerms - Sever Admin", inline=False)
            
            await ctx.reply(embed=embed)
            
        elif sub == "moderation_commands":
            embed: discord.Embed = discord.Embed(
                title="**Moderation Help Commands**",
                description="Bellow are all the Moderation commands that we have.",
                color=discord.Color.green()
            )
            embed.add_field(name="**Warn**", value="If you do **d/warn [user] [reason]** it will warn the user.\nPerms - Warn +", inline=False)
            embed.add_field(name="**Tempmute**", value="If you do **d/tempmute [user] [time] [reason]** it will tempmute the user for the time you said.\nPerms - Tempmute +", inline=False)
            embed.add_field(name="**Mute**", value="If you do **d/mute [user] [reason]** it will mute the user for ever if you don't unmute them.\nPerms - Mute +", inline=False)
            embed.add_field(name="**Unmute**", value="If you do **d/unmute [user]** it will unmute the user you said.\nPerms - Unmute +", inline=False)
            embed.add_field(name="**Kick**", value="If you do **d/kick [user] [reason]** it will kick the user from the server for that reason.\nPerms - Kick +", inline=False)
            embed.add_field(name="**Delete Infraction**", value="If you do **d/delete [case ID]** it will allow you to delete that infraction form the database. It will never come back.\nPerms - Delete Inf +")
            embed.add_field(name="**Ban**", value="If you do **d/ban [user] [reason]** it will ban the user from the server.\nPerms - Ban +", inline=False)
            embed.add_field(name="**Unban**", value="If you do **d/unban [user]** it will let you unban a user from the discord server. Note you have to do something like LegosAndStuff#0501 not a user ID.\nPerms - Unban +")
            
            await ctx.reply(embed=embed)
            
        elif sub == "moderation_search":
            embed: discord.Embed = discord.Embed(
                title="**Moderation Help Search**",
                description="Bellow are all the Moderation Search commands that we have",
                color=discord.Color.green()
            )
            embed.add_field(name="**Mod Search**", value="If you do **d/mod [optional user]** it will search all for moderation commands that that use has done.\nPerms - Warn +", inline=False)
            embed.add_field(name="**User Search**", value="If you do **d/user [optional user]** it will search for infractions that the users has been givin.\nPerms - Warn +", inline=False)
            embed.add_field(name="**Case**", value="If you do **d/case [case ID]** it will give you the infomation of that case.\nPerms - Warn +", inline=False)
            embed.add_field(name="**Search All**", value="If you do **d/search all** it will show the 5 most recent infractions.\nPerms - Warn +", inline=False)
            embed.add_field(name="**Recent**", value="If you do **d/search recent** it will give you the infomation of the most recent infraction.\nPerms - Warn +", inline=False)
            embed.add_field(name="**Delete**", value="If you do **d/delete [case ID]** it will allow you to delete a case\nPerms - Delete inf +")

            await ctx.reply(embed=embed)

        
    

def setup(client):
	client.add_cog(Help(client))   
