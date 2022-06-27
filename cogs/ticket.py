from typing import TYPE_CHECKING, Tuple, List

import nextcord
from nextcord import Embed, Interaction
from nextcord.ext import commands
from nextcord.ext.commands import Context
from nextcord.ui import View, Button
from nextcord.components import SelectOption

if TYPE_CHECKING:
    from main import Main


async def create_select_options() -> List[SelectOption]:
    options = []
    needed = ['Bewerbung', 'Giveaway-Gewinner', 'Booster-tickets']
    for i in needed:
        options.append(SelectOption(label=i, value=i))

    return options


class TicketView(View):
    @nextcord.ui.select(custom_id='ticket_select', options=await create_select_options())
    async def create_ticket(self, button: Button, inter: Interaction):
        print('create ticket')


async def create_ticket(ctx: Context) -> Tuple[View, Embed]:
    view = TicketView(timeout=None)
    # view.add_item(Button(label='Ticket erstellen'))
    embed = Embed(title='Ticket erstellen', description='Ticket erstellen', color=0x00ff00)
    return view, embed


class Ticket(commands.Cog):
    def __init__(self, bot: 'Main'):
        self.bot = bot

    @commands.Command
    async def ticket(self, ctx: Context):
        ticket_view, ticket_embed = await create_ticket(ctx)
        await ctx.send(embed=ticket_embed, view=ticket_view)


def setup(bot) -> int:
    bot.add_cog(Ticket(bot))
    print('Ticket loaded.')
    return 0
