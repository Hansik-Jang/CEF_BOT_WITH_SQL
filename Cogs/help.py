import discord
from discord.ext import commands
import config


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='도움말', aliases=[], pass_context=True,
                      help="명령어 목록 및 사용방법을 출력합니다.", brief="$도움말")
    async def _help(self, ctx, args=None):

        command_names_list = [x.name for x in self.bot.commands]
        if not args :
            help_embed = discord.Embed(title="도움말 목록")
            for cogName in config.COG_LIST:
                i = 1
                cog = self.bot.get_cog(cogName)
                commands = cog.get_commands()
                text = ""
                for command in commands:
                    print(command.help)
                    text = text + str(i) + ". " + command.name + "\n"
                    i += 1
                help_embed.add_field(name=cogName, value=text, inline=True)
            help_embed.add_field(name="사용법", value="$도움말 '검색할 명령어'를 입력하세요.", inline=False)
        elif args in command_names_list :
            help_embed = discord.Embed(title=f"도움말 - {args}")
            help_embed.add_field(
                name=self.bot.get_command(args).brief,
                value=self.bot.get_command(args).help
            )

        else :
            help_embed = discord.Embed(title="도움말 - 실패")
            help_embed.add_field(
                name="잘못 입력하였습니다.",
                value="$도움말 '명령어' 를 정확히 입력해주세요."
            )
        await ctx.send(embed=help_embed)


async def setup(bot):
    await bot.add_cog(Help(bot))