from myfun import *
import myfun
import string
import discord
import asyncio

def checkDisplayNameChange(ctx):
    if ctx.author.display_name != ctx.author.name:
        return True
    else:
        return False

def checkNicknameForm(ctx):
    if '[' in ctx.author.display_name and ']' in ctx.author.display_name:
        return True
    else:
        return False


def checkEnglish(ctx):
    role_names = [role.name for role in ctx.author.roles]
    if "스태프" in role_names:
        return True
    else:
        nickname = myfun.getNickFromDisplayname(ctx)
        if nickname.upper() != nickname.lower():
            return True
        else:                             # 대소문자가 다르면 영어
            return False


def checkEnglishFromText(text):
    if 'a' <= text.lower() <= 'z':
        return True
    else:                             # 대소문자가 다르면 영어
        return False


def checkNicknameOverlapFromText(text):
    import sqlite3
    result = True
    temp = ''
    try:
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM USER_INFORMATION")
        for row in cur.fetchall():
            #print(row)
            if text == row[2].lower():
                temp = '중복 O'
                result = False           # 중복이면 True
                break
            else:
                temp = '중복 X'
                result = True          # 중복 아니면 False
        return result
    finally:
        conn.close()


def checkRejoin(ctx):
    import sqlite3
    result = True
    try:
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM USER_INFORMATION")
        for row in cur.fetchall():
            #print(ctx.author.id, row[0])
            if ctx.author.id == row[0]:
                result = False           # 중복이면 True
                break
                #print('a')
            else:
                #print('b')
                result = True          # 중복 아니면 False
        #print("----\n")
        #print(result)

        return result
    finally:
        conn.close()


def checkNicknameOverlap(ctx):
    import sqlite3
    temp = ''
    # 닉네임 내 공백 제거 및 소문자 변경
    ownNickname = getNickFromDisplayname(ctx).replace(" ", "")
    ownNickname = ownNickname.lower()
    nicknameDataInDB = ''
    nicknameDataInDB2 = ''
    # 스위치 ==============
    OVL_SWITCH = True          # True : USER_INFORMATION 내 데이터와 중복 X -> EXC_SWITCH 체크 필요
    EXC_SWITCH = False         # True : NICKNAME_EXCEPTION 내 데이터와 중복 -> 가입 가능
    JOIN_SWITCH = False         # True : 가입 가능
    text = ''
    # USER_INFORMATION DB 내 검사
    conn = sqlite3.connect("CEF.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM USER_INFORMATION")

    for row in cur.fetchall():  # A : 닉네임, B : DB 내 정보
        nicknameDataInDB = row[1].lower()
        nicknameDataInDB = nicknameDataInDB.replace(" ", "")
        # A in B 검사
        if ownNickname in nicknameDataInDB:
            print(ownNickname, nicknameDataInDB, "A in B")
            OVL_SWITCH = False
            text = text + "A in B / "
            break
        # B in A 검사
        elif nicknameDataInDB in ownNickname:
            print(ownNickname, nicknameDataInDB, "B in A")
            OVL_SWITCH = False
            text = text + "B in A / "
            break
        # 중복이 아닐 경우
        else:
            print(ownNickname, nicknameDataInDB, "중복 없음")
            OVL_SWITCH = True

    # NICKNAME_EXCEPTION DB 내 검사
    if not OVL_SWITCH:
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM NICKNAME_EXCEPTION")
        for row in cur.fetchall():
            nicknameDataInDB2 = row[0].lower()
            nicknameDataInDB2 = nicknameDataInDB2.replace(" ", "")
            if ownNickname == nicknameDataInDB2:       # 예외 목록에 있음
                EXC_SWITCH = True
                print("A")
                break
            else:
                print("B")
                EXC_SWITCH = False

    if OVL_SWITCH:
        JOIN_SWITCH = True
    else:
        if EXC_SWITCH:
            JOIN_SWITCH = True
        else:
            JOIN_SWITCH = False

    return JOIN_SWITCH

def checkNicknameOverlapText(text):
    import sqlite3
    temp = ''
    # 닉네임 내 공백 제거 및 소문자 변경
    ownNickname = text.replace(" ", "")
    ownNickname = ownNickname.lower()
    nicknameDataInDB = ''
    nicknameDataInDB2 = ''
    # 스위치 ==============
    OVL_SWITCH = True          # True : USER_INFORMATION 내 데이터와 중복 X -> EXC_SWITCH 체크 필요
    EXC_SWITCH = False         # True : NICKNAME_EXCEPTION 내 데이터와 중복 -> 가입 가능
    JOIN_SWITCH = False         # True : 가입 가능
    text = ''
    # USER_INFORMATION DB 내 검사
    conn = sqlite3.connect("CEF.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM USER_INFORMATION")

    for row in cur.fetchall():  # A : 닉네임, B : DB 내 정보
        nicknameDataInDB = row[1].lower()
        nicknameDataInDB = nicknameDataInDB.replace(" ", "")
        # A in B 검사
        if ownNickname in nicknameDataInDB:
            print(ownNickname, nicknameDataInDB, "A in B")
            OVL_SWITCH = False
            text = text + "A in B / "
            break
        # B in A 검사
        elif nicknameDataInDB in ownNickname:
            print(ownNickname, nicknameDataInDB, "B in A")
            OVL_SWITCH = False
            text = text + "B in A / "
            break
        # 중복이 아닐 경우
        else:
            print(ownNickname, nicknameDataInDB, "중복 없음")
            OVL_SWITCH = True

    # NICKNAME_EXCEPTION DB 내 검사
    if not OVL_SWITCH:
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM NICKNAME_EXCEPTION")
        for row in cur.fetchall():
            nicknameDataInDB2 = row[0].lower()
            nicknameDataInDB2 = nicknameDataInDB2.replace(" ", "")
            if ownNickname == nicknameDataInDB2:       # 예외 목록에 있음
                EXC_SWITCH = True
                print("A")
                break
            else:
                print("B")
                EXC_SWITCH = False

    if OVL_SWITCH:
        JOIN_SWITCH = True
    else:
        if EXC_SWITCH:
            JOIN_SWITCH = True
        else:
            JOIN_SWITCH = False

    return JOIN_SWITCH