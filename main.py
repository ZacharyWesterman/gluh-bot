#!/usr/bin/env python3

import json
from pathlib import Path
import random

import discord
from discord import Forbidden, HTTPException, NotFound
from discord.ext import tasks

from responses import messages, weights

with open(str(Path(__file__).parent) + '/secrets.json', 'r', encoding='utf8') as fp:
    data = json.load(fp)
    DISCORD_TOKEN = data['token']
    GUILD_ID = data['guild']


class DiscordClient(discord.Client):
    """
    A Discord client that listens for messages and reacts to them.
    It handles commands, updates player status, and manages point of interest markers.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the Discord client with the given arguments and keyword arguments.
        It sets up the database connection and prepares the client for use.
        """
        super().__init__(*args, **kwargs)
        self.activity = None

    async def on_ready(self):
        """
        Called when the client is ready and connected to Discord.
        It initializes the bot, sets the status message, and starts repeating tasks.
        """
        print('Logged in as ', self.user)

    async def on_message(self, message: discord.Message):
        """
        Called when a message is sent in a channel the bot can see.
        It processes the message to check if it was mentioned, and responds accordingly.

        Args:
            message (discord.Message): The message that was sent.
        """

        if not self.user:
            print('Discord client is not logged in. Exiting...')
            return

        # Don't respond to ourselves
        if message.author == self.user:
            return

        # Only respond to users that respond to us, mention us, or mention our role.
        if not self.user.mentioned_in(message) and '<@&1514854948066558035>' not in message.content:
            return

        reply = random.choices(messages(), weights=weights())

        await message.channel.send(reply[0])


INTENTS = discord.Intents.all()
CLIENT = DiscordClient(intents=INTENTS)
CLIENT.run(DISCORD_TOKEN)
