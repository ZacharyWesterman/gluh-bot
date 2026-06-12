#!/usr/bin/env python3

import json
from pathlib import Path
import random

import discord
from discord import Forbidden, HTTPException, NotFound
from discord.ext import tasks

with open(str(Path(__file__).parent) + '/secrets.json', 'r', encoding='utf8') as fp:
    data = json.load(fp)
    DISCORD_TOKEN = data['token']
    GUILD_ID = data['guild']

DEFAULT_REPLIES = (
    (10, "gluh"),
    (10, "Gluh."),
    (8, "...gluh?"),
    (5, "g l u h"),
    (5, "gluh..."),
    (4, "gluh!"),
    (4, "gluh?"),
    (3, "GLUH!!"),
    (3, "gluh gluh"),
    (3, "\\*gluh noises\\*"),
    (3, "g-gluh...?"),
    (2, "gluh moment 🤯"),
    (2, "gluh 👍"),
    (2, "gluh 👎"),
    (1, '> Guhhhh, gluh.\n\\- gluh'),
    (1, "ERROR: gluh overflow"),
    (1, "1. gluh\n2. gluh\n3. ???\n4. gluh"),
    (0.5, "gluh detected. activating neurotoxin."),
    (0.5, "I am in incredible pain. Uh, I mean... gluh"),
    (0.1, "One day you will answer for your crimes. And God will not be as merciful as I am."),
    (0.1, "srry busy overthrowing lithuania. be bac l8r."),
)

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

        replies = DEFAULT_REPLIES
        reply = random.choices([i[1] for i in replies], weights=[i[0] for i in replies])

        await message.channel.send(reply[0])

INTENTS = discord.Intents.all()
CLIENT = DiscordClient(intents=INTENTS)
CLIENT.run(DISCORD_TOKEN)
