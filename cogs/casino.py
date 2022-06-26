from nextcord.ext import commands
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import Main


class Casino(commands.Cog):
    def __init__(self, bot: Main):
        self.bot = bot


def setup(bot):
    bot.add_cog(Casino(bot))
    print('Casino loaded.')
    return bot
