import string
import forAccessDB


# display_name으로부터 닉네임 정보 얻기
def getNickFromDisplayname2(name):
    temp = name.split('[')
    nickname = temp[0].strip()
    return nickname

# display_name으로부터 닉네임 정보 얻기
def getNickFromDisplayname(ctx):
    if '[' in ctx.author.display_name:
        temp = ctx.author.display_name.split('[')
        nickname = temp[0].strip()
        return nickname
    else:
        return ctx.author.display_name

# display_name으로부터 주포지션 정보 얻기
def getJupoFromDisplayname(ctx):
    a = ctx.author.display_name.split('[')
    temp = a[1]
    if '/' in ctx.author.display_name:
        b = temp.split('/')
        jupo = b[0].upper()
        return jupo
    else:
        b = temp.split(']')
        jupo = b[0].upper()
        return jupo

# display_name으로부터 주포지션 정보 얻기
def getJupoFromDisplayname2(name):
    a = name.split('[')
    temp = a[1]
    if '/' in name:
        b = temp.split('/')
        jupo = b[0].upper()
        return jupo
    else:
        b = temp.split(']')
        jupo = b[0].upper()
        return jupo

# display_name으로부터 부포지션 정보 얻기
def getBupoFromDisplayname(ctx):
    if '/' in ctx.author.display_name:
        a = ctx.author.display_name.split('/')
        temp = a[1]
        b = temp.split(']')
        bupo = b[0].upper()
        return bupo
    else:
        return '없음'


# display_name으로부터 이모지 정보 얻기
def getImojiFromDisplayname(ctx):
    temp = ctx.author.display_name.split(']')
    imoji = temp[1]
    return imoji


def getImoji(ctx):
    imoji = ""
    role_names = [role.name for role in ctx.author.roles]
    print(role_names)
    if "TOTS🥇" in role_names:
        imoji = imoji + "🥇"
    if "TOTS Nomi🥈" in role_names:
        imoji = imoji + "🥈"
    if "Valondor👑" in role_names:
        imoji = imoji + "👑"
    if "Server Booster⭐" in role_names:
        imoji = imoji + "⭐"
    if "Golden Rookey🐔" in role_names:
        imoji = imoji + "🐔"
    if "신규🐤" in role_names:
        imoji = imoji + "🐤"
    if "내전리그 1위🌺" in role_names:
        imoji = imoji + "🌺"
    if "내전리그 2위🍀" in role_names:
        imoji = imoji + "🍀"
    if "내전리그 3위☘" in role_names:
        imoji = imoji + "☘"

    return imoji


def recombinationNickname(nickname, mainPos, subPos, imoji):

    if subPos == "":
        result = nickname + "[" + mainPos + "]" + imoji
    else:
        result = nickname + "[" + mainPos + "/" + subPos + "]" + imoji
    return result


def printDump(conn):
    # Dump 출력
    # 데이터베이스 백업
    with conn:
        with open('./resource/dump.sql', 'w') as f:
            for line in conn.iterdump():
                f.write('%s\n' % line)
            print('DumpPrint Complete')

    # f.close(), conn.close()

def teamNameConvert(name):
    if name == "A" or name == 'a' or name == 'TEAM_A':
        return 'TEAM_A'
    elif name == "B" or name == 'b' or name == 'TEAM_B':
        return 'TEAM_B'
    elif name == "C" or name == 'c' or name == 'TEAM_C':
        return 'TEAM_C'
    elif name == "D" or name == 'd' or name == 'TEAM_D':
        return 'TEAM_D'
    elif name == "E" or name == 'e' or name == 'TEAM_E':
        return 'TEAM_E'
    else:
        return 'error'

def getRoleCount(ctx, roleName):
    from discord.utils import get
    discordRole = get(ctx.guild.roles, name=roleName)
    return str(len(discordRole.members))