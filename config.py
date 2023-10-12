import discord
from discord.ext import commands
from discord.utils import get

# 베이스
baseRoleName = "테스트용"
totalCommunityRoleNameList = ["테스트용", "RFA", "KPA", "EVT", "SNI"] # 나중에 테스트용은 CEF로 변경 필수

# 상태
DEVELOPER_SWITCH = True     # True이면 개발자만 사용 가능, DB에선 1
global NICKNAME_FORMAT_CHECK_SWITCH
NICKNAME_FORMAT_CHECK_SWITCH = True

# 채널명
JOIN_CHANNEL = 'cef-가입신청❕'

NAEJEON_TEAM_A = '내전-a-파랑💙'
NAEJEON_TEAM_B = '내전-b-빨강💖'
NAEJEON_TEAM_C = '내전-c-노랑💛'
NAEJEON_TEAM_D = '내전-d-하양🤍'


# 개발자 리스트
DEVELOPER_LIST = [146549960312225792,   # 타임제이
                  790243958071492648]   # 테스트계정

def devlopCheck(ctx):
    if ctx.author.id in DEVELOPER_LIST:
        return True
    else:
        return False