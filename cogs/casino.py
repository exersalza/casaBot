from random import randint
from typing import TYPE_CHECKING

from nextcord.ext import commands

if TYPE_CHECKING:
    from main import Main


class Casino(commands.Cog):
    def __init__(self, bot: 'Main'):
        self.bot: Main = bot

    @commands.command()
    async def gamble(self, ctx, bet: int = 100):
        user_id = ctx.author.id

        try:
            user_coins = self.bot.conn.get('SELECT points.coins FROM dcbots.points '
                                           'WHERE points.user = %s', (user_id,))[0][0]
        except IndexError as e:
            await ctx.send('Es ist ein Fehler aufgetreten, versuche es später erneut.')
            print(e)
            return
        print(user_coins)

        if bet > user_coins:
            await ctx.send('Du hast nicht genug Coins.')
            return

        if bet < 0:
            await ctx.send('Du kannst nicht negativ oder null werden.')
            return

        if randint(0, 1):
            await ctx.send('Du hast gewonnen!')
        else:
            await ctx.send('Du hast verloren!')


def setup(bot) -> int:
    bot.add_cog(Casino(bot))
    print('Casino loaded.')
    return 0
