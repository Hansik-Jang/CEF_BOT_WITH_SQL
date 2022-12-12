from myfun import *

def checkNicknameForm(ctx):
    if '[' in ctx.author.display_name and ']' in ctx.author.display_name:
        return True
    else:
        return False

def checkEnglish(ctx):
    if 'a' <= getNickFromDisplayname(ctx)[0].lower() <= 'z':
        return True
    else:                             # 대소문자가 다르면 영어
        return False

def checkEnglishFromText(text):
    if 'a' <= text.lower() <= 'z':
        return True
    else:                             # 대소문자가 다르면 영어
        return False

def checkNicknameOverlap(ctx):
    import sqlite3
    result = True
    temp = ''
    try:
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM User_Info")
        for row in cur.fetchall():
            #print(row)
            if getNickFromDisplayname(ctx).lower() == row[2].lower():
                temp = '중복 O'
                result = False           # 중복이면 True
                print(getNickFromDisplayname(ctx), row[2], temp)
                break
                #print('a')
            else:
                #print('b')
                temp = '중복 X'
                result = True          # 중복 아니면 False
                print(getNickFromDisplayname(ctx), row[2], temp)
        #print("----\n")
        #print(result)
        return result
    finally:
        conn.close()

def checkNicknameOverlapFromText(text):
    import sqlite3
    result = True
    temp = ''
    try:
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM User_Info")
        for row in cur.fetchall():
            #print(row)
            if text == row[2].lower():
                temp = '중복 O'
                result = False           # 중복이면 True
                break
                #print('a')
            else:
                #print('b')
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
        cur.execute("SELECT * FROM User_Info")
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