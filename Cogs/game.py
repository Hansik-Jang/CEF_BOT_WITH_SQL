import discord
from discord.ext import commands
from discord.utils import get
import asyncio

class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='투표', pass_context=True)
    async def _topyo(self, ctx):
        msg = await ctx.send("투표")

        await msg.add_reaction('1️⃣')
        await msg.add_reaction('2️⃣')
        await msg.add_reaction('3️⃣')

    @commands.command(name='랜덤모집', pass_context=True)
    async def _naejeongongji(self, ctx, *, text=None):
        voice_state = ctx.author.voice
        channelA_ID = 935523897493835826
        channelB_ID = 1156183464295542815
        channelC_ID = 1156183466539499550
        channelD_ID = 1159148162422935564
        sleep_time = 720
        voice_channel_id_list = [channelA_ID, channelB_ID, channelC_ID, channelD_ID ]
        #voice_channel_id_list = [1165171280597758022]
        recruit_channel = get(ctx.guild.text_channels, id=1165537473317843015)
        #recruit_channel = get(ctx.guild.text_channels, id=1165547381643817050)
        channel = ctx.message.author.voice.channel

        if voice_state is not None:
            if channel.id in voice_channel_id_list:
                if text is None:
                    await ctx.send("모집 포지션을 같이 작성해주세요.\n"
                                    "작성방법 : $랜덤모집 '모집포지션'\n"
                                    "예시) $랜덤모집 RW CM RB")
                else:
                    await ctx.reply(f"{recruit_channel.mention}에 업데이트 되었습니다.", delete_after=10)
                    await recruit_channel.send(f"```모집 채널 : {channel.name}\n"
                                               f"모집 포지션 : {text}```", delete_after=720)
                    invitelink = await channel.create_invite(max_age=720, max_uses=10)
                    msg = await recruit_channel.send(invitelink)
            else:
                await ctx.reply("랜덤매칭 채널에 없습니다.")
        else:
            await ctx.reply("입장한 음성 대화방이 업습니다.")


async def setup(bot):
    await bot.add_cog(Game(bot))
