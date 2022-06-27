from typing import TYPE_CHECKING

from nextcord.ext import commands

if TYPE_CHECKING:
    from main import Main


class Ticket(commands.Cog):
    def __init__(self, bot: 'Main'):
        self.bot = bot


def setup(bot) -> int:
    bot.add_cog(Ticket(bot))
    print('Ticket loaded.')
    return 0
