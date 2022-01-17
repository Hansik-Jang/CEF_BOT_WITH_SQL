from myfun import *

def checkNicknameForm(ctx):
    if '[' in ctx.author.display_name and ']' in ctx.author.display_name:
        return True
    else:
        return False


def checkNicknameOverlap(ctx):
    import sqlite3
    result = False
    try:
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM User_Info")
        for row in cur.fetchall():
#           print(row)
            print(getNickFromDisplayname(ctx), row[2])
            if getNickFromDisplayname(ctx) == row[2]:
                result = True           # 중복이면 True
                break
                #print('a')
            else:
                #print('b')
                result = False          # 중복 아니면 False
        #print("----\n")
        #print(result)

        return result
    finally:
        conn.close()


def checkRejoin(ctx):
    import sqlite3
    result = False
    try:
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM User_Info")
        for row in cur.fetchall():
            print(ctx.author.id, row[0])
            if ctx.author.id == row[0]:
                result = True           # 중복이면 True
                break
                #print('a')
            else:
                #print('b')
                result = False          # 중복 아니면 False
        #print("----\n")
        #print(result)

        return result
    finally:
        conn.close()