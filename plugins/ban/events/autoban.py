"""
Ce programme est régi par la licence CeCILL soumise au droit français et
respectant les principes de diffusion des logiciels libres. Vous pouvez
utiliser, modifier et/ou redistribuer ce programme sous les conditions
de la licence CeCILL diffusée sur le site "http://www.cecill.info".
"""

import random

import discord
from discord.ext import commands


async def execute(
    ban_plugin,
    ctx: commands.Context,
    user: discord.User,
    reason: str,  # pylint: disable=unused-argument
) -> bool:
    """Execute the autoban event.
    If the event doest't succeed, the function returns False.
    """

    if ctx.author.id == user.id:
        if await ban_plugin.fake_ban(ctx, ctx.author):
            choice = random.randint(0, 2)
            msg = await ctx.bot._(ctx.channel, f"ban.gunivers.autoban.{choice}")
            await ctx.send(msg.format(ctx.author.mention, user.mention))
            await ctx.send(
                "https://tenor.com/view/seriously-facepalm-fml-crazy-head-bang-gif-16492152"
            )
        return True

    else:
        return False
