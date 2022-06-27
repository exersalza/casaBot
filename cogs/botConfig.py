from functools import lru_cache
from typing import TYPE_CHECKING

from nextcord import Interaction
from nextcord.ext import commands
from nextcord.ext.commands import Context
from nextcord.ui import View, Button

if TYPE_CHECKING:
    from main import Main


class BotConfig(commands.Cog):
    def __init__(self, bot: 'Main'):
        self.bot = bot

    @commands.Command
    async def ping(self, ctx: Context):
        # add latency to ping
        view = View(timeout=None)
        view.add_item(Button(label='Pong', custom_id='pong'))
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms', view=view)

    @commands.Cog.listener()
    async def on_interaction(self, inter: Interaction):
        print('something')
        print(inter.expires_at)

    @commands.Command
    async def reload_module(self, ctx):
        self.bot.unload_extension('cogs.botConfig')
        self.bot.load_extension('cogs.botConfig')


def setup(bot) -> int:
    bot.add_cog(BotConfig(bot))
    print('BotConfig loaded.')
    return 0
