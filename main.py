#!/usr/bin/python

# Imports
import os

import nextcord
from knxrcore.sql import mysql
from nextcord.ext.commands import Context, errors

import config

from nextcord.ext import commands


class Main(commands.Bot):
    def __init__(self, token: str, intents=''):
        self.token = token
        self.conn = mysql.Connection(host=config.db_host, user=config.db_user,
                                     password=config.db_pass, db=config.db_name)

        if not intents:
            intents = nextcord.Intents.default()
            intents.message_content = True

        super().__init__(command_prefix='!',
                         description='Casa Dc bot',
                         # help_command=None,
                         intents=intents)

        self.cog_loader()

    def cog_loader(self):
        """ Load cogs """
        for i in os.listdir('cogs'):
            if not i in ['__init__.py', '__pycache__']:
                print(f'cogs.{i[:-3]}')
                self.load_extension(f'cogs.{i[:-3]}')

    async def on_ready(self):
        print('\nLogged in as')
        print(self.user)
        print(self.user.id)
        print('------')

    @commands.Cog.listener()
    async def on_disconnect(self):
        await self.connect(reconnect=True)

    @commands.Cog.listener()
    async def on_connect(self) -> None:
        print('Connected!')

    @commands.Cog.listener()
    async def on_command_error(self, context: Context, exception: errors.CommandError) -> None:
        if isinstance(exception, errors.CommandNotFound):
            await context.send(f'Kommand `{context.prefix + context.invoked_with}` nicht gefunden.')
            return

        raise exception


if __name__ == '__main__':
    bot = Main(token=config.TOKEN)
    bot.run(bot.token)
