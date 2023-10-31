import discord
from discord.ext import commands
from discord.utils import get

# 베이스
baseRoleName = "테스트용"
totalCommunityRoleNameList = ["테스트용", "RFA", "KPA", "EVT", "SNI"] # 나중에 테스트용은 CEF로 변경 필수
CEF_SERVER_ID = 706480732477849650
TEST_SERVER_ID = 1114943322201526272
positionList = ["ST", "LW", "RW", "CAM", "CM", "CDM", "LB", "CB", "RB", "GK"]

# 상태
DEVELOPER_SWITCH = True     # True이면 개발자만 사용 가능, DB에선 1
global NICKNAME_FORMAT_CHECK_SWITCH
NICKNAME_FORMAT_CHECK_SWITCH = True

# 채널명
JOIN_CHANNEL = 'cef-가입신청❕'
TRANSFER_CENTER = "리그-이적센터"
NAEJEON_TEAM_A = '내전-a-파랑💙'
NAEJEON_TEAM_B = '내전-b-빨강💖'
NAEJEON_TEAM_C = '내전-c-노랑💛'
NAEJEON_TEAM_D = '내전-d-하양🤍'

# 텍스트 문구
notJoinText = "등록된 인원만 사용 가능한 명령어입니다.\n" \
              "$가입 명령어를 사용하여 등록을 먼저 해주세요."

# 개발자 리스트
DEVELOPER_LIST = [146549960312225792,   # 타임제이
                  790243958071492648]   # 테스트계정

# Cog 리스트
COG_LIST = ["AboutDB", "Career", "Contract", "ControlSwitch", "Event", "Game", "Help", "League", "ManageTeam",
            "Mark", "Member", "OtherClub", "Team", "Test", "Transfer"] # Draft 재외
def devlopCheck(ctx):
    if ctx.author.id in DEVELOPER_LIST:
        return True
    else:
        return False


'''
        role_names = [role.name for role in ctx.author.roles]
        if "스태프" in role_names :
            if checkUseJoinCommandWithID(ctx.author.id):
                pass
            else :
                await ctx.reply("해당 인원은 등록되지 않는 인원입니다.")
        else:
            await ctx.reply("해당 명령어는 스태프만 사용 가능합니다.")
'''