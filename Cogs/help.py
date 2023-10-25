import discord
from discord.ext import commands
import config


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='도움말', aliases=[], pass_context=True)
    async def _help(self, ctx, args=None):
        help_embed = discord.Embed(title="도움말")
        command_names_list = [x.name for x in self.bot.commands]
        if not args :
            print(config.COG_LIST)
            for cogName in config.COG_LIST:
                print(cogName)
                i = 1
                cog = self.bot.get_cog(cogName)
                commands = cog.get_commands()
                text = ""
                for c in commands:
                    text = text + str(i) + ". " + c.name + "\n"
                    i += 1
                print(cogName)
                print(text)
                help_embed.add_field(name=cogName, value=text, inline=True)
            help_embed.add_field(name="사용법", value="$도움말 '검색할 명령어를 입력하세요.", inline=False)
        elif args in command_names_list :
            help_embed.add_field(
                name=args,
                value=self.bot.get_command(args).help
            )

        else :
            help_embed.add_field(
                name="잘못 입력하였습니다.",
                value="$도움말 '명령어' 를 정확히 입력해주세요."
            )
        await ctx.send(embed=help_embed, delete_after=30)


async def setup(bot):
    await bot.add_cog(Help(bot))