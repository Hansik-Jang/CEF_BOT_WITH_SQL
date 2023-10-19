import sqlite3

def connectDB():
    conn = sqlite3.connect("CEF.db")
    return conn

def checkUseJoinCommand(ctx):
    conn = sqlite3.connect("CEF.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM USER_INFORMATION WHERE ID=?", (ctx.author.id,))
    result = cur.fetchone()
    conn.close()
    if result is not None:
        return True
    else:
        return False

def checkUseJoinCommandWithID(id):
    conn = sqlite3.connect("CEF.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM USER_INFORMATION WHERE ID=?", (id,))
    result = cur.fetchone()
    conn.close()
    if result is not None:
        return True
    else:
        return False


def getUserInformation(ctx):
    conn = sqlite3.connect("CEF.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM USER_INFORMATION WHERE ID=?", (ctx.author.id,))
    result = cur.fetchone()
    conn.close()
    return result

def getUserInformationWithID(id):
    conn = sqlite3.connect("CEF.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM USER_INFORMATION WHERE ID=?", (id,))
    result = cur.fetchone()
    conn.close()
    return result

# ------------- USER_INFORMATION -------------

def getNicknameFromUserInfo(ctx):
    conn = sqlite3.connect("CEF.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM USER_INFORMATION WHERE ID=?", (ctx.author.id,))
    result = cur.fetchone()
    nickname = result[1]
    conn.close()
    return nickname

def getNicknameFromUserInfoWithID(id):
    conn = sqlite3.connect("CEF.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM USER_INFORMATION WHERE ID=?", id)
    result = cur.fetchone()
    nickname = result[1]
    conn.close()
    return nickname


def getMainPositionFromUserInfo(ctx):
    conn = sqlite3.connect("CEF.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM USER_INFORMATION WHERE ID=?", (ctx.author.id,))
    result = cur.fetchone()
    mainPosition = result[2]
    conn.close()
    return mainPosition


def getMainPositionFromUserInfoWithID(id):
    conn = sqlite3.connect("CEF.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM USER_INFORMATION WHERE ID=?", (id,))
    result = cur.fetchone()
    mainPosition = result[2]
    conn.close()
    return mainPosition


def getSubPositionFromUserInfo(ctx):
    conn = sqlite3.connect("CEF.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM USER_INFORMATION WHERE ID=?", (ctx.author.id,))
    result = cur.fetchone()
    subPosition = result[3]
    conn.close()
    return subPosition

def getSubPositionFromUserInfoWithID(id):
    conn = sqlite3.connect("CEF.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM USER_INFORMATION WHERE ID=?", (id,))
    result = cur.fetchone()
    subPosition = result[3]
    conn.close()
    return subPosition


def getTeamNameFromUserInfo(ctx):
    conn = sqlite3.connect("CEF.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM USER_INFORMATION WHERE ID=?", (ctx.author.id,))
    result = cur.fetchone()
    TeamNumber = result[4]
    conn.close()
    return TeamNumber


def getTeamNameFromUserInfoWithID(id):
    conn = sqlite3.connect("CEF.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM USER_INFORMATION WHERE ID=?", (id,))
    result = cur.fetchone()
    TeamNumber = result[4]
    conn.close()
    return TeamNumber


def getRankFromUserInfo(ctx):
    conn = sqlite3.connect("CEF.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM USER_INFORMATION WHERE ID=?", (ctx.author.id,))
    result = cur.fetchone()
    rank = result[5]
    conn.close()
    return rank

def getRankFromUserInfoWithID(id):
    conn = sqlite3.connect("CEF.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM USER_INFORMATION WHERE ID=?", (id,))
    result = cur.fetchone()
    rank = result[5]
    conn.close()
    return rank


def getNickChangeCouponFromUserInfo(ctx):
    conn = sqlite3.connect("CEF.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM USER_INFORMATION WHERE ID=?", (ctx.author.id,))
    result = cur.fetchone()
    nickChangeCoupon = result[6]
    conn.close()
    return nickChangeCoupon

def getNickChangeCouponFromUserInfoWithID(id):
    conn = sqlite3.connect("CEF.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM USER_INFORMATION WHERE ID=?", (id,))
    result = cur.fetchone()
    nickChangeCoupon = result[6]
    conn.close()
    return nickChangeCoupon

# ------------- TEAM_INFORMATION -------------


def getTeamFullNameFromTeamInfor(abbTeamName):
    conn = sqlite3.connect("CEF.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM TEAM_INFORMATION WHERE Abbreviation=?", (abbTeamName, ))
    result = cur.fetchone()
    fullName = result[1]
    return fullName

def getColorCodeFromTeamInfor(abbTeamName):
    conn = sqlite3.connect("CEF.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM TEAM_INFORMATION WHERE Abbreviation=?", (abbTeamName, ))
    result = cur.fetchone()
    colorCode = result[2]
    return colorCode

def getLastRankFromTeamInfor(abbTeamName):
    conn = sqlite3.connect("CEF.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM TEAM_INFORMATION WHERE Abbreviation=?", (abbTeamName, ))
    result = cur.fetchone()
    colorCode = result[3]
    return colorCode


# ------------- TOTS -------------

def getInforFromTotsFW(ctx):
    text = ''
    conn = sqlite3.connect("CEF.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM TOTS_FW WHERE ID=?", (ctx.author.id,))
    data_list = cur.fetchall()
    data_list.sort(key=lambda x: x[1])  # Season 순으로 정렬
    for data in data_list :
        if data[2]:
            text = text + data[1] + " FW TOTS **1st**\n"
        elif data[3]:
            text = text + data[1] + " FW TOTS 2nd\n"

    return text


# ------------- HISTORY -------------

def getInfoFromSeasonUserHistory(ctx):
    text = ''
    text_li = []
    conn = sqlite3.connect("CEF.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM SEASON_USER_HISTORY WHERE ID=?", (ctx.author.id,))
    data_list = cur.fetchall()
    data_list.sort(key=lambda x: x[1])   # Season 순으로 정렬
    print(data_list)
    for data in data_list:
        text = ''
        #print("C - ", data)
        # data / 1 : 시즌, 2 : 팀약자, 3 : 직책, 4 : 포지션, 5 : 순위(int)
        #text = text + getHostFromSeasonTeamCount(data[1]) + " " + data[1] + " 시즌 " + data[2] + " " + data[3] + " "\
        #       + data[4] + " " + str(data[5]) + "위 (" + str(getTotalCountFromSeasonTeamCount(data[1])) + "팀)\n"
        #print(text)
        text = text + getHostFromSeasonTeamCount(data[1]) + " " + data[1] + " 시즌 " + data[2] + " " + data[3] + " " \
               + data[4] + " " + str(data[5]) + "위 (" + str(getTotalCountFromSeasonTeamCount(data[1])) + "팀)\n"
        print(text)
        text_li.append(text)

    print(text_li)
    '''
            for data in data_list:
            text = ''
            print(data)
            host = str(getHostFromSeasonTeamCount(data[1]))
            season = str(data[1])
            abbName = str(data[2])
            job = str(data[3])
            pos = str(data[4])
            rank = str(data[5])
            totalCount = str(getHostFromSeasonTeamCount(season))
            text = text + host + " " + season + " 시즌 " + abbName + " " + job + " " \
                   + pos + " " + rank + "위 (" + totalCount + "팀)\n"
            print(text)
            li.append(text)
            print(li)
            '''
    return text

# ------------- SEASON_TEAM_COUNT_INFORMATION -------------

def getHostFromSeasonTeamCount(season):
    conn = sqlite3.connect("CEF.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM SEASON_TEAM_COUNT_INFORMATION WHERE Season=?", (season, ))
    data = cur.fetchone()
    host = data[1]
    return host


def getTotalCountFromSeasonTeamCount(season):
    conn = sqlite3.connect("CEF.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM SEASON_TEAM_COUNT_INFORMATION WHERE Season=?", (season, ))
    data = cur.fetchone()
    totalCount = data[2]
    return totalCount
