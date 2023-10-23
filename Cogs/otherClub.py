import discord
from discord.utils import get
from discord.ext import commands
import checkFun
import myfun

class OtherClub(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.li = []

    @commands.command(aliases=["에버튼", "EVT", "evt"], pass_context=True)
    async def _everton(self, ctx):
        if str(ctx.message.channel) == "타커뮤-등록신청":
            add_message = "에버튼"
            join_out_text_channel = get(ctx.guild.channels, id=1157984264097382510)

            role_names = [role.name for role in ctx.author.roles]
            if "EVT" in role_names :  # RFA 역할을 이미 갖고 있는지 검사
                await ctx.reply(content=f"```이미 '{add_message}' 역할을 갖고 있습니다.```")
            else :  # RFA 역할이 없을 경우
                if "EVE_" in ctx.author.display_name :  # RFA_ 가 닉네임에 있는지 검사
                    EVE_ROLE = get(ctx.guild.roles, name="EVT")
                    SNI_ROLE = get(ctx.guild.roles, name="SNI")
                    RFA_ROLE = get(ctx.guild.roles, name="RFA")
                    KPA_ROLE = get(ctx.guild.roles, name="KPA")
                    CEF_ROLE = get(ctx.guild.roles, name="CEF")
                    NEW_ROLE = get(ctx.guild.roles, name="신규🐤")
                    DELETE_ROLE_LIST = [CEF_ROLE, EVE_ROLE, SNI_ROLE, RFA_ROLE, KPA_ROLE, CEF_ROLE, NEW_ROLE]
                    role_check_text_list = ["CEF", "EVE", "SNI", "KPA", "RFA", "신규🐤"]
                    user = ctx.author

                    delete_message = ''

                    for role in role_check_text_list :  # 본인 역할에 서버 역할들이 들어있는지 검사 시작
                        if role in role_names :  # 본인 역할에 서버 역할이 하나라도 있을 경우
                            if role == "CEF" :  # 삭제된 역할 목록 저장
                                delete_message = delete_message + "CEF"
                            elif role == "EVE" :
                                delete_message = delete_message + "EVE"
                            elif role == "SNI:" :
                                delete_message = delete_message + "SNI"
                            elif role == "RFA" :
                                delete_message = delete_message + "RFA"
                            elif role == "KPA" :
                                delete_message = delete_message + "KPA"

                            for ROLE in DELETE_ROLE_LIST :  # 모든 관련 역할 제거
                                await user.remove_roles(ROLE)

                    await user.add_roles(EVE_ROLE)  # 역할 추가
                    if delete_message == '' :
                        await ctx.reply(content=f"{add_message} 소속 등록 완료")
                        await join_out_text_channel.send(content=f"<최초등록> {ctx.author.mention} : {add_message} 소속 등록")
                    else :
                        await ctx.reply(content=f"{delete_message}  ->  {add_message} 소속 이전 완료")  # 삭제된 역할, 추가된 역할 텍스트 출력
                        await join_out_text_channel.send(content=f"<소속이전> {ctx.author.mention} : "
                                                                 f"{delete_message}  ->  {add_message}")    # 서버 이동 현황 채널에 업데이트
                else :
                    await ctx.reply(content=f"```닉네임을 소속에 맞게 수정 후 다시 시도해주세요.\n"
                                            f"ex) EVE_닉네임, SNI_닉네임, RFA_닉네임, KPA_닉네임```")
        else:
            join_other_community_channel = get(ctx.guild.channels, id=1159340259310587965)
            await ctx.message.delete()
            await ctx.send(content=f"{join_other_community_channel.mention} 채널에 작성해주세요.", delete_after=5)

    @commands.command(aliases=["저격", "SNI", "sni"], pass_context=True)
    async def _sniper(self, ctx):
        if str(ctx.message.channel) == "타커뮤-등록신청":
            add_message = "저격 UTD"
            join_out_text_channel = get(ctx.guild.channels, id=1157984264097382510)
            role_names = [role.name for role in ctx.author.roles]
            if "SNI" in role_names :  # RFA 역할을 이미 갖고 있는지 검사
                await ctx.reply(content=f"```이미 '{add_message}' 역할을 갖고 있습니다.```")
            else :  # RFA 역할이 없을 경우
                if "SNI_" in ctx.author.display_name :  # RFA_ 가 닉네임에 있는지 검사
                    EVE_ROLE = get(ctx.guild.roles, name="EVT")
                    SNI_ROLE = get(ctx.guild.roles, name="SNI")
                    RFA_ROLE = get(ctx.guild.roles, name="RFA")
                    KPA_ROLE = get(ctx.guild.roles, name="KPA")
                    CEF_ROLE = get(ctx.guild.roles, name="CEF")
                    NEW_ROLE = get(ctx.guild.roles, name="신규🐤")
                    DELETE_ROLE_LIST = []
                    role_check_text_list = ["CEF", "EVE", "SNI", "KPA", "RFA", "신규🐤"]
                    user = ctx.author

                    delete_message = ''

                    for role in role_check_text_list :  # 본인 역할에 서버 역할들이 들어있는지 검사 시작
                        if role in role_names :  # 본인 역할에 서버 역할이 하나라도 있을 경우
                            if role == "CEF" :  # 삭제된 역할 목록 저장
                                delete_message = delete_message + "CEF"
                                DELETE_ROLE_LIST.append(CEF_ROLE)
                            elif role == "EVE" :
                                delete_message = delete_message + "EVE"
                                DELETE_ROLE_LIST.append(EVE_ROLE)
                            elif role == "SNI:" :
                                delete_message = delete_message + "SNI"
                                DELETE_ROLE_LIST.append(SNI_ROLE)
                            elif role == "RFA" :
                                delete_message = delete_message + "RFA"
                                DELETE_ROLE_LIST.append(RFA_ROLE)
                            elif role == "KPA" :
                                delete_message = delete_message + "KPA"
                                DELETE_ROLE_LIST.append(KPA_ROLE)
                            elif role == "신고🐤":
                                DELETE_ROLE_LIST.append(NEW_ROLE)

                            for ROLE in DELETE_ROLE_LIST :  # 모든 관련 역할 제거
                                await user.remove_roles(ROLE)

                    await user.add_roles(SNI_ROLE)  # 역할 추가
                    if delete_message == '' :
                        await ctx.reply(content=f"{add_message} 소속 등록 완료")
                        await join_out_text_channel.send(content=f"<최초등록> {ctx.author.mention} : {add_message} 소속 등록")
                    else :
                        await ctx.reply(content=f"{delete_message}  ->  {add_message} 소속 이전 완료")  # 삭제된 역할, 추가된 역할 텍스트 출력
                        await join_out_text_channel.send(content=f"<소속이전> {ctx.author.mention} : "
                                                                 f"{delete_message}  ->  {add_message}")    # 서버 이동 현황 채널에 업데이트

                else :
                    await ctx.reply(content=f"```닉네임을 소속에 맞게 수정 후 다시 시도해주세요.\n"
                                            f"ex) EVE_닉네임, SNI_닉네임, RFA_닉네임, KPA_닉네임```")
        else:
            join_other_community_channel = get(ctx.guild.channels, id=1159340259310587965)
            await ctx.message.delete()
            await ctx.send(content=f"{join_other_community_channel.mention} 채널에 작성해주세요.", delete_after=5)

    @commands.command(aliases=["KPA", "kpa"], pass_context=True)
    async def _kpa(self, ctx) :
        if str(ctx.message.channel) == "타커뮤-등록신청":
            add_message = "KPA"
            join_out_text_channel = get(ctx.guild.channels, id=1157984264097382510)
            role_names = [role.name for role in ctx.author.roles]
            if "KPA" in role_names :  # RFA 역할을 이미 갖고 있는지 검사
                await ctx.reply(content=f"```이미 '{add_message}' 역할을 갖고 있습니다.```")
            else :  # RFA 역할이 없을 경우
                if "KPA_" in ctx.author.display_name :  # RFA_ 가 닉네임에 있는지 검사
                    EVE_ROLE = get(ctx.guild.roles, name="EVT")
                    SNI_ROLE = get(ctx.guild.roles, name="SNI")
                    RFA_ROLE = get(ctx.guild.roles, name="RFA")
                    KPA_ROLE = get(ctx.guild.roles, name="KPA")
                    CEF_ROLE = get(ctx.guild.roles, name="CEF")
                    NEW_ROLE = get(ctx.guild.roles, name="신규🐤")
                    DELETE_ROLE_LIST = []
                    role_check_text_list = ["CEF", "EVE", "SNI", "KPA", "RFA", "신규🐤"]
                    user = ctx.author

                    delete_message = ''

                    for role in role_check_text_list :  # 본인 역할에 서버 역할들이 들어있는지 검사 시작
                        print(role, "A")
                        if role in role_names :  # 본인 역할에 서버 역할이 하나라도 있을 경우
                            print(role)
                            if role == "CEF" :  # 삭제된 역할 목록 저장
                                delete_message = delete_message + "CEF"
                                DELETE_ROLE_LIST.append(CEF_ROLE)
                            elif role == "EVE" :
                                delete_message = delete_message + "EVE"
                                DELETE_ROLE_LIST.append(EVE_ROLE)
                            elif role == "SNI:" :
                                delete_message = delete_message + "SNI"
                                DELETE_ROLE_LIST.append(SNI_ROLE)
                            elif role == "RFA" :
                                delete_message = delete_message + "RFA"
                                DELETE_ROLE_LIST.append(RFA_ROLE)
                            elif role == "KPA" :
                                delete_message = delete_message + "KPA"
                                DELETE_ROLE_LIST.append(KPA_ROLE)
                            elif role == "신규🐤":
                                DELETE_ROLE_LIST.append(NEW_ROLE)

                            #for ROLE in DELETE_ROLE_LIST :  # 모든 관련 역할 제거
                            await user.edit(roles=[])
                            print("B")

                    await user.add_roles(KPA_ROLE)  # 역할 추가
                    if delete_message == '' :
                        await ctx.reply(content=f"{add_message} 소속 등록 완료")
                        await join_out_text_channel.send(content=f"<최초등록> {ctx.author.mention} : {add_message} 소속 등록")
                    else :
                        await ctx.reply(content=f"{delete_message}  ->  {add_message} 소속 이전 완료")  # 삭제된 역할, 추가된 역할 텍스트 출력
                        await join_out_text_channel.send(content=f"<소속이전> {ctx.author.mention} : "
                                                                 f"{delete_message}  ->  {add_message}")    # 서버 이동 현황 채널에 업데이트
                else :
                    await ctx.reply(content=f"```닉네임을 소속에 맞게 수정 후 다시 시도해주세요.\n"
                                            f"ex) EVE_닉네임, SNI_닉네임, RFA_닉네임, KPA_닉네임```")
        else :
            join_other_community_channel = get(ctx.guild.channels, id=1159340259310587965)
            await ctx.message.delete()
            await ctx.send(content=f"{join_other_community_channel.mention} 채널에 작성해주세요.", delete_after=5)

    @commands.command(aliases=["RFA", "rfa"], pass_context=True)
    async def _rfa(self, ctx):
        if str(ctx.message.channel) == "타커뮤-등록신청" :
            add_message = "RFA"
            join_out_text_channel = get(ctx.guild.channels, id=1157984264097382510)
            role_names = [role.name for role in ctx.author.roles]
            if "RFA" in role_names:                                                         # RFA 역할을 이미 갖고 있는지 검사
                await ctx.reply(content=f"```이미 '{add_message}' 역할을 갖고 있습니다.```")
            else:                                                                           # RFA 역할이 없을 경우
                if "RFA_" in ctx.author.display_name :                                          # RFA_ 가 닉네임에 있는지 검사
                    EVE_ROLE = get(ctx.guild.roles, name="EVT")
                    SNI_ROLE = get(ctx.guild.roles, name="SNI")
                    RFA_ROLE = get(ctx.guild.roles, name="RFA")
                    KPA_ROLE = get(ctx.guild.roles, name="KPA")
                    CEF_ROLE = get(ctx.guild.roles, name="CEF")
                    NEW_ROLE = get(ctx.guild.roles, name="신규🐤")
                    DELETE_ROLE_LIST = [CEF_ROLE, EVE_ROLE, SNI_ROLE, RFA_ROLE, KPA_ROLE, CEF_ROLE, NEW_ROLE]
                    role_check_text_list = ["CEF", "EVE", "SNI", "KPA", "RFA", "신규🐤"]
                    user = ctx.author

                    delete_message = ''

                    for role in role_check_text_list :                                      # 본인 역할에 서버 역할들이 들어있는지 검사 시작
                        if role in role_names :                                                 # 본인 역할에 서버 역할이 하나라도 있을 경우
                            if role == "CEF" :                                                      # 삭제된 역할 목록 저장
                                delete_message = delete_message + "CEF"
                            elif role == "EVE" :
                                delete_message = delete_message + "EVE"
                            elif role == "SNI:" :
                                delete_message = delete_message + "SNI"
                            elif role == "RFA" :
                                delete_message = delete_message + "RFA"
                            elif role == "KPA" :
                                delete_message = delete_message + "KPA"

                            for ROLE in DELETE_ROLE_LIST :                                                 # 모든 관련 역할 제거
                                await user.remove_roles(ROLE)

                    await user.add_roles(RFA_ROLE)                                                  # 역할 추가
                    if delete_message == '' :
                        await ctx.reply(content=f"{add_message} 소속 등록 완료")
                        await join_out_text_channel.send(content=f"<최초등록> {ctx.author.mention} : {add_message} 소속 등록")
                    else :
                        await ctx.reply(content=f"{delete_message}  ->  {add_message} 소속 이전 완료")  # 삭제된 역할, 추가된 역할 텍스트 출력
                        await join_out_text_channel.send(content=f"<소속이전> {ctx.author.mention} : "
                                                                 f"{delete_message}  ->  {add_message}")    # 서버 이동 현황 채널에 업데이트
                else :
                    await ctx.reply(content=f"```닉네임을 소속에 맞게 수정 후 다시 시도해주세요.\n"
                                            f"ex) EVE_닉네임, SNI_닉네임, RFA_닉네임, KPA_닉네임```")
        else :
            join_other_community_channel = get(ctx.guild.channels, id=1159340259310587965)
            await ctx.message.delete()
            await ctx.send(content=f"{join_other_community_channel.mention} 채널에 작성해주세요.", delete_after=5)



async def setup(bot):
    await bot.add_cog(OtherClub(bot))
