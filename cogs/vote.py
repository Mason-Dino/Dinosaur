#----------------------------------------------------------------------#
#
#       Vote: -vote
#       vlbowner: -vlb
#
#----------------------------------------------------------------------#

import discord
import os
from discord.ext import commands
from discord.ext.commands import BucketType
import asyncio
import random
import math
import sqlite3
import datetime

class Vote(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Vote Command -vote
    @commands.command()
    async def vote(self, ctx, lead=None):
        if lead == None:
            embed: discord.Embed = discord.Embed(
                title="Vote for Dinosaur on top.gg",
                description="Use the link bellow to vote for Dinosaur\n\nhttps://top.gg/bot/840025172861386762/vote",
                color=discord.Color.green()
            )

            await ctx.send(embed=embed)

        elif lead == "leaderboard":
            conn = sqlite3.connect("vote.db")
            c = conn.cursor()

            c.execute("SELECT * FROM vote ORDER BY votes DESC LIMIT 1 OFFSET 0")

            items_1 = c.fetchall()
            none_1 = str(items_1)

            c.execute("SELECT * FROM vote ORDER BY votes DESC LIMIT 1 OFFSET 1")

            items_2 = c.fetchall()
            none_2 = str(items_2)

            c.execute("SELECT * FROM vote ORDER BY votes DESC LIMIT 1 OFFSET 2")

            items_3 = c.fetchall()
            none_3 = str(items_3)

            c.execute("SELECT * FROM vote ORDER BY votes DESC LIMIT 1 OFFSET 3")

            items_4 = c.fetchall()
            none_4 = str(items_4)

            c.execute("SELECT * FROM vote ORDER BY votes DESC LIMIT 1 OFFSET 4")

            items_5 = c.fetchall()
            none_5 = str(items_5)

            c.execute("SELECT * FROM vote ORDER BY votes DESC LIMIT 1 OFFSET 5")

            items_6 = c.fetchall()
            none_6 = str(items_6)

            c.execute("SELECT * FROM vote ORDER BY votes DESC LIMIT 1 OFFSET 6")

            items_7 = c.fetchall()
            none_7 = str(items_7)

            c.execute("SELECT * FROM vote ORDER BY votes DESC LIMIT 1 OFFSET 7")

            items_8 = c.fetchall()
            none_8 = str(items_8)

            c.execute("SELECT * FROM vote ORDER BY votes DESC LIMIT 1 OFFSET 8")

            items_9 = c.fetchall()
            none_9 = str(items_9)

            c.execute("SELECT * FROM vote ORDER BY votes DESC LIMIT 1 OFFSET 9")

            items_10 = c.fetchall()
            none_10 = str(items_10)

            if none_1 == "[]":
                user_1 = "Unavailable"
                votes_1 = 0

            else:
                for item_1 in items_1:
                    user_1_id = int(item_1[0])
                    vote_1 = int(item_1[1])

                user_1 = self.client.get_user(user_1_id)

                if user_1 == None:
                    user_1 = user_1_id

                else:
                    user_1 = user_1.name

            if none_2 == "[]":
                user_2 = "Unavailable"
                vote_2 = 0

            else:
                for item in items_2:
                    user_2_id = int(item[0])
                    vote_2 = int(item[1])

                user_2 = self.client.get_user(user_2_id)

                if user_2 == None:
                    user_2 = user_2_id

                else:
                    user_2 = user_2.name

            if none_3 == "[]":
                user_3 = "Unavailable"
                vote_3 = 0

            else:
                for item in items_3:
                    user_3_id = int(item[0])
                    vote_3 = int(item[1])

                user_3 = self.client.get_user(user_3_id)

                if user_3 == None:
                    user_3 = user_3_id

                else:
                    user_3 = user_3.name

            if none_4 == "[]":
                user_4 = "Unavailable"
                vote_4 = 0

            else:
                for item in items_4:
                    user_4_id = int(item[0])
                    vote_4 = int(item[1])

                user_4 = self.client.get_user(user_4_id)

                if user_4 == None:
                    user_4 = user_4_id

                else:
                    user_4 = user_4.name

            if none_5 == "[]":
                user_5 = "Unavailable"
                vote_5 = 0

            else:
                for item in items_5:
                    user_5_id = int(item[0])
                    vote_5 = int(item[1])

                user_5 = self.client.get_user(user_5_id)

                if user_5 == None:
                    user_5 = user_5_id

                else:
                    user_5 = user_5.name

            if none_6 == "[]":
                user_6 = "Unavailable"
                vote_6 = 0

            else:
                for item in items_6:
                    user_6_id = int(item[0])
                    vote_6 = int(item[1])

                user_6 = self.client.get_user(user_6_id)

                if user_6 == None:
                    user_6 = user_6_id

                else:
                    user_6 = user_6.name

            if none_7 == "[]":
                user_7 = "Unavailable"
                vote_7 = 0

            else:
                for item in items_7:
                    user_7_id = int(item[0])
                    vote_7 = int(item[1])

                user_7 = self.client.get_user(user_7_id)

                if user_7 == None:
                    user_7 = user_7_id

                else:
                    user_7 = user_7.name

            if none_8 == "[]":
                user_8 = "Unavailable"
                vote_8 = 0

            else:
                for item in items_8:
                    user_8_id = int(item[0])
                    vote_8 = int(item[1])

                user_8 = self.client.get_user(user_8_id)

                if user_8 == None:
                    user_8 = user_8_id

                else:
                    user_8 = user_8.name

            if none_9 == "[]":
                user_9 = "Unavailable"
                vote_9 = 0

            else:
                for item in items_9:
                    user_9_id = int(item[0])
                    vote_9 = int(item[1])

                user_9 = self.client.get_user(user_9_id)

                if user_9 == None:
                    user_9 = user_9_id

                else:
                    user_9 = user_9.name

            if none_10 == "[]":
                user_10 = "Unavailable"
                vote_10 = 0

            else:
                for item in items_10:
                    user_10_id = int(item[0])
                    vote_10 = int(item[1])

                user_10 = self.client.get_user(user_10_id)

                if user_10 == None:
                    user_10 = user_10_id

                else:
                    user_10 = user_10.name

            embed: discord.Embed = discord.Embed(
                title="Vote Leaderboard",
                description=f"Bellow are the top 10 people\n\n:first_place: {user_1} - {vote_1}\n:second_place: {user_2} - {vote_2}\n:third_place: {user_3} - {vote_3}\n:medal: {user_4} - {vote_4}\n:medal: {user_5} - {vote_5}\n:medal: {user_6} - {vote_6}\n:medal: {user_7} - {vote_7}\n:medal: {user_8} - {vote_8}\n:medal: {user_9} - {vote_9}\n:medal: {user_10} - {vote_10}\n",
                color=discord.Color.green()
            ) 

            await ctx.send(embed=embed)

        else:
            embed: discord.Embed = discord.Embed(
                title="Vote for Dinosaur on top.gg",
                description="Use the link bellow to vote for Dinosaur\n\nhttps://top.gg/bot/840025172861386762/vote",
                color=discord.Color.green()
            )

            await ctx.send(embed=embed)

            

    """    
    @slash_commands.command(
        name="vote",
        description="Gives you a vote link for top.gg"
    )
    async def slash_vote(self, ctx):
        embed: discord.Embed = discord.Embed(
            title="Vote for Dinosaur on top.gg",
            description="Use the link bellow to vote for Dinosaur\n\nhttps://top.gg/bot/840025172861386762/vote",
            color=discord.Color.green()
        )
        
        await ctx.reply(embed=embed)
    """

    #Vlbowner Command -vlb
    @commands.command()
    async def vlbowner(self, ctx):
        if 638092957756555291 == ctx.message.author.id:
            x = datetime.datetime.now()
            m_d_y = x.strftime("%x")

            date = m_d_y.split("/")

            m = date[0]
            d = date[1]
            y = date[2]

            if d == "01":
                votechannel = self.client.get_channel(861773377742831656)

                conn = sqlite3.connect("vote.db")
                c = conn.cursor()

                c.execute("SELECT * FROM vote ORDER BY votes DESC LIMIT 1 OFFSET 0")

                items_1 = c.fetchall()
                none_1 = str(items_1)

                c.execute("SELECT * FROM vote ORDER BY votes DESC LIMIT 1 OFFSET 1")

                items_2 = c.fetchall()
                none_2 = str(items_2)

                c.execute("SELECT * FROM vote ORDER BY votes DESC LIMIT 1 OFFSET 2")

                items_3 = c.fetchall()
                none_3 = str(items_3)

                c.execute("SELECT * FROM vote ORDER BY votes DESC LIMIT 1 OFFSET 3")

                items_4 = c.fetchall()
                none_4 = str(items_4)

                c.execute("SELECT * FROM vote ORDER BY votes DESC LIMIT 1 OFFSET 4")

                items_5 = c.fetchall()
                none_5 = str(items_5)

                c.execute("SELECT * FROM vote ORDER BY votes DESC LIMIT 1 OFFSET 5")

                items_6 = c.fetchall()
                none_6 = str(items_6)

                c.execute("SELECT * FROM vote ORDER BY votes DESC LIMIT 1 OFFSET 6")

                items_7 = c.fetchall()
                none_7 = str(items_7)

                c.execute("SELECT * FROM vote ORDER BY votes DESC LIMIT 1 OFFSET 7")

                items_8 = c.fetchall()
                none_8 = str(items_8)

                c.execute("SELECT * FROM vote ORDER BY votes DESC LIMIT 1 OFFSET 8")

                items_9 = c.fetchall()
                none_9 = str(items_9)

                c.execute("SELECT * FROM vote ORDER BY votes DESC LIMIT 1 OFFSET 9")

                items_10 = c.fetchall()
                none_10 = str(items_10)

                if none_1 == "[]":
                    user_1 = "Unavailable"
                    votes_1 = 0

                else:
                    for item_1 in items_1:
                        user_1_id = int(item_1[0])
                        vote_1 = int(item_1[1])

                    user_1 = self.client.get_user(user_1_id)

                    if user_1 == None:
                        user_1 = user_1_id

                    else:
                        user_1 = user_1.name

                if none_2 == "[]":
                    user_2 = "Unavailable"
                    vote_2 = 0

                else:
                    for item in items_2:
                        user_2_id = int(item[0])
                        vote_2 = int(item[1])

                    user_2 = self.client.get_user(user_2_id)

                    if user_2 == None:
                        user_2 = user_2_id

                    else:
                        user_2 = user_2.name

                if none_3 == "[]":
                    user_3 = "Unavailable"
                    vote_3 = 0

                else:
                    for item in items_3:
                        user_3_id = int(item[0])
                        vote_3 = int(item[1])

                    user_3 = self.client.get_user(user_3_id)

                    if user_3 == None:
                        user_3 = user_3_id

                    else:
                        user_3 = user_3.name

                if none_4 == "[]":
                    user_4 = "Unavailable"
                    vote_4 = 0

                else:
                    for item in items_4:
                        user_4_id = int(item[0])
                        vote_4 = int(item[1])

                    user_4 = self.client.get_user(user_4_id)

                    if user_4 == None:
                        user_4 = user_4_id

                    else:
                        user_4 = user_4.name

                if none_5 == "[]":
                    user_5 = "Unavailable"
                    vote_5 = 0

                else:
                    for item in items_5:
                        user_5_id = int(item[0])
                        vote_5 = int(item[1])

                    user_5 = self.client.get_user(user_5_id)

                    if user_5 == None:
                        user_5 = user_5_id

                    else:
                        user_5 = user_5.name

                if none_6 == "[]":
                    user_6 = "Unavailable"
                    vote_6 = 0

                else:
                    for item in items_6:
                        user_6_id = int(item[0])
                        vote_6 = int(item[1])

                    user_6 = self.client.get_user(user_6_id)

                    if user_6 == None:
                        user_6 = user_6_id

                    else:
                        user_6 = user_6.name

                if none_7 == "[]":
                    user_7 = "Unavailable"
                    vote_7 = 0

                else:
                    for item in items_7:
                        user_7_id = int(item[0])
                        vote_7 = int(item[1])

                    user_7 = self.client.get_user(user_7_id)

                    if user_7 == None:
                        user_7 = user_7_id

                    else:
                        user_7 = user_7.name

                if none_8 == "[]":
                    user_8 = "Unavailable"
                    vote_8 = 0

                else:
                    for item in items_8:
                        user_8_id = int(item[0])
                        vote_8 = int(item[1])

                    user_8 = self.client.get_user(user_8_id)

                    if user_8 == None:
                        user_8 = user_8_id

                    else:
                        user_8 = user_8.name

                if none_9 == "[]":
                    user_9 = "Unavailable"
                    vote_9 = 0

                else:
                    for item in items_9:
                        user_9_id = int(item[0])
                        vote_9 = int(item[1])

                    user_9 = self.client.get_user(user_9_id)

                    if user_9 == None:
                        user_9 = user_9_id

                    else:
                        user_9 = user_9.name

                if none_10 == "[]":
                    user_10 = "Unavailable"
                    vote_10 = 0

                else:
                    for item in items_10:
                        user_10_id = int(item[0])
                        vote_10 = int(item[1])

                    user_10 = self.client.get_user(user_10_id)

                    if user_10 == None:
                        user_10 = user_10_id

                    else:
                        user_10 = user_10.name

                embed: discord.Embed = discord.Embed(
                    title="Vote Leaderboard",
                    description=f"Bellow are the top 10 people\n\n:first_place: {user_1} - {vote_1}\n:second_place: {user_2} - {vote_2}\n:third_place: {user_3} - {vote_3}\n:medal: {user_4} - {vote_4}\n:medal: {user_5} - {vote_5}\n:medal: {user_6} - {vote_6}\n:medal: {user_7} - {vote_7}\n:medal: {user_8} - {vote_8}\n:medal: {user_9} - {vote_9}\n:medal: {user_10} - {vote_10}\n",
                    color=discord.Color.green()
                )

                conn = sqlite3.connect("vote.db")
                c = conn.cursor()

                c.execute("SELECT * FROM vote")

                items = c.fetchall()
                none = str(items)

                if none == "[]":
                    pass
            
                else:
                    for item in items:
                        user_id = int(item[0])
                        votes = int(item[1])

                        c.execute(f"""UPDATE vote SET votes=0
                                    WHERE user_ID={user_id}
                        """)

                        conn.commit()

                    conn.close()

                await votechannel.send(embed=embed)

            else    :
                await ctx.send(f"Did not do leaderboard because its only {m_d_y}")

        else:
            await ctx.send("You can't do this command because you are not the owner")

def setup(client):
	client.add_cog(Vote(client)) 