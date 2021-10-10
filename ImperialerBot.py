import discord
import random
import os
from discord.enums import ActivityType
from discord.ext import commands
import discord.utils
import datetime, re
import copy
import logging
import sys
import json, asyncio
import pytz
from datetime import datetime
from discord import Member
import asyncio

description = """
Moin! Ich wurde von Arasp Shojai, den heftigsten Typen der Welt, geschrieben!
"""

class MyClient(discord.Client):
    async def  on_ready(self):
        print("Der Imperialer Bot ist nun bereit! Lang lebe das Imperium!")

    async def on_message(self, message):
        print("Nachricht von " + str(message.author) + " enthält " + str(message.content))
        if message.author == client.user:
            return

        if message.content.startswith("?help"):
            await message.channel.send('**Folgende Commands kannst du verwenden:** \r\n'
                                 '- ?help \r\n'
                                 '- ?userinfo \r\n'
                                 '- ?homeworks \r\n'
                                 '- ?meetings \r\n'
                                 '- ?games \r\n'
                                 '- ?website \r\n'
                                 '- ?youtube \r\n')

        if message.content.startswith("Hi Bot!"):
            await message.channel.send('Hiiiiiiiiiiiiiiiiii!')
            await message.author.send("Du hast den legendären imperialen Bot kontaktiert, was gibt es, mein Freund?")

        if message.content.startswith("?homeworks"):
            await message.channel.send('**Das sind unsere aktuellen Hausaufgaben:** \r\n'
                                       '- Ein Erklärvideo zur Teilung der DNA --> Biologie \r\n'
                                       '- Das Bild sowie das Referat zu den ausgewählten Epochen beenden --> Kunst \r\n'
                                       '- Lernen für den Mathetest, der direkt nach den Ferien stattfinden wird --> Mathe \r\n'
                                       '- Lernen für die Gesellschaftsarbeit --> Gesellschaft \r\n')

        if message.content.startswith("?meetings"):
            await message.channel.send('**Das sind die aktuell wichtigsten Termine für Klassenarbeiten, etc:** \r\n'
                                       '- Gesellschaftsarbeit: 27.10.2021 \r\n'
                                       )

        if message.content.startswith("?games"):
            await message.channel.send('**Folgende Spiele könnt ihr mit dem Bot spielen:** \r\n'
                                       '- Roulette: ?roulette + BID eingeben und einfach Mal spielen! BID = \r\n'
                                       '   black \r\n'
                                       '   red \r\n'
                                       '   Eine Zahl zwischen 0 und 36 \r\n'
                                       '\r\n'
                                       '-  \r\n')
        
        if message.content.startswith("?website"):
            await message.channel.send('Besuche meine Webseite! \r\n'
                                       'https://www.lernenmitherrshojai.de/')

        if message.content.startswith("?youtube"):
            await message.channel.send('Besuche mein Youtube-Kanal! \r\n'
                                       'https://www.youtube.com/channel/UCOKurTE8Frp_A76NgthkRyg')


        if message.content.startswith("?roulette"):
            bid = message.content.split(' ')[1]
            bid_param = -3
            if bid.lower() == "black":
                bid_param = -1
            elif bid.lower() == "red":
                bid_param = -2
            else:
                try:
                    bid_param = int(bid)
                except:
                    bid_param = -3
            if bid_param == -3:
                await message.channel.send('Ungültige Eingabe')
                return
            result = random.randint(0,36)
            print(result)
            if bid_param == -1:
                won = result%2 == 0 and not result == 0
            elif bid_param == -2:
                won = result%2 == 1
            else:
                won = result == bid_param
            if won:
                await message.channel.send('Du hast gewonnen!!!!')
            else:
                await message.channel.send('Haha etchi patch, du hast verloren!')

        if message.content.startswith('?userinfo'):
            args = message.content.split(' ')
            if len(args) == 2:
                member = Member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    embed = discord.Embed(title='Userinfo für {}'.format(member.name),
                                          description='Dies ist eine Userinfo für den User {}'.format(member.mention),
                                          color=0x22a7f0)
                    embed.add_field(name='Server beigetreten', value=member.joined_at.strftime('%d/%m/%Y, %H:%M:%S'),
                                    inline=True)
                    embed.add_field(name='Discord beigetreten', value=member.created_at.strftime('%d/%m/%Y, %H:%M:%S'),
                                    inline=True)
                    rollen = ''
                    for role in member.roles:
                        if not role.is_default():
                            rollen += '{} \r\n'.format(role.mention)
                    if rollen:
                        embed.add_field(name='Rollen', value=rollen, inline=True)
                        embed.set_thumbnail(url=member.avatar_url)
                        embed.set_footer(text='EmbedFooter')
                        mess = await message.channel.send(embed=embed)
                        await mess.add_reaction('🚍')
                        await mess.add_reaction('a:tut_herz:662606955520458754')

client = MyClient()
client.run("YourBotToken")
