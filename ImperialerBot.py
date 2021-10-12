import discord
from discord import activity
from discord.ext import commands, tasks
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
from discord.ext.commands import Bot
import time
import asyncio

class MyClient(discord.Client):
    async def on_ready(self):
        print("Der Imperialer Bot ist nun bereit! Lang lebe das Imperium!")
        while True:
            await client.change_presence(activity=discord.Game('https://discord.gg/7PMrd8cdFy'), status=discord.Status.online)
            await asyncio.sleep(5)
            await client.change_presence(activity=discord.Game('https://www.youtube.com/channel/UCOKurTE8Frp_A76NgthkRyg'), status=discord.Status.online)
            await asyncio.sleep(5)
            await client.change_presence(activity=discord.Game('Der imperiale Bot!'), status=discord.Status.online)
            await asyncio.sleep(5)
            await client.change_presence(activity=discord.Game('Lang lebe das Imperium!'), status=discord.Status.online)
            await asyncio.sleep(5)
            await client.change_presence(activity=discord.Game('Besuche meine Webseite:'), status=discord.Status.online)
            await asyncio.sleep(2)
            await client.change_presence(activity=discord.Game('lernenmitherrshojai.de'), status=discord.Status.online)
            await asyncio.sleep(3)
            await client.change_presence(activity=discord.Game('Schreibe Hi Bot!'), status=discord.Status.online)
            await asyncio.sleep(5)
            await client.change_presence(activity=discord.Game('Am 18.10.2021 fängt die Schule wieder an!'), status=discord.Status.online)
            await asyncio.sleep(5)
            await client.change_presence(activity=discord.Game('Folge mir auf Instagram!'), status=discord.Status.online)
            await asyncio.sleep(2)
            await client.change_presence(activity=discord.Game('@arasp_sh_'), status=discord.Status.online)
            await asyncio.sleep(3)
            await client.change_presence(activity=discord.Game('?help'), status=discord.Status.online)
            await asyncio.sleep(5)
  
    async def on_message(self, message):
        print("Nachricht von " + str(message.author) + " enthält " + str(message.content))
        if message.author == client.user:
            return
        
        if message.author.bot:
            return

        if message.content.startswith("?help"):
            await message.channel.send('**Folgende Commands kannst du verwenden:** \r\n'
                                 '- ?help \r\n'
                                 '- ?userinfo \r\n'
                                 '- ?homeworks \r\n'
                                 '- ?meetings \r\n'
                                 '- ?games \r\n'
                                 '- ?website \r\n'
                                 '- ?youtube \r\n'
                                 '- ?instagram \r\n'
                                 '- ?clear \r\n')

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
                                       '- Wahrsager: ?8ball + Deine Frage eingeben und abwarten!\r\n'
                                       '\r\n'
                                       '- \r\n')
        
        if message.content.startswith("?website"):
            await message.channel.send('Besuche meine Webseite! \r\n'
                                       'https://www.lernenmitherrshojai.de/')

        if message.content.startswith("?youtube"):
            await message.channel.send('Besuche mein Youtube-Kanal! \r\n'
                                       'https://www.youtube.com/channel/UCOKurTE8Frp_A76NgthkRyg')

        if message.content.startswith("?instagram"):
             await message.channel.send('Folge mir auf Instagram! \r\n'
                                        'https://www.instagram.com/arasp_sh_')

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

client = MyClient()
client.run("YourBotToken")
