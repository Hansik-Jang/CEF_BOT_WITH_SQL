import sqlite3


def connectDB() :
    conn = sqlite3.connect("CEF.db")
    return conn


def checkUseJoinCommand(ctx) :
    conn = sqlite3.connect("CEF.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM USER_INFORMATION WHERE ID=?", (ctx.author.id,))
    result = cur.fetchone()
    conn.close()
    if result is not None :
        return True
    else :
        return False



def checkUseJoinCommandWithID(id) :
    conn = sqlite3.connect("CEF.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM USER_INFORMATION WHERE ID=?", (id,))
    result = cur.fetchone()
    conn.close()
    if result is not None :
        return True
    else :
        return False


def getUserInformation(ctx) :
    conn = sqlite3.connect("CEF.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM USER_INFORMATION WHERE ID=?", (ctx.author.id,))
    result = cur.fetchone()
    conn.close()
    return result


def getUserInformationWithID(id) :
    conn = sqlite3.connect("CEF.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM USER_INFORMATION WHERE ID=?", (id,))
    result = cur.fetchone()
    conn.close()
    return result


# ------------- USER_INFORMATION -------------

def getNicknameFromUserInfo(ctx) :
    try:
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM USER_INFORMATION WHERE ID=?", (ctx.author.id,))
        result = cur.fetchone()
        nickname = result[1]
        conn.close()
    except:
        nickname = ''
    return nickname


def getNicknameFromUserInfoWithID(id) :
    try:
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM USER_INFORMATION WHERE ID=?", (id,))
        result = cur.fetchone()
        nickname = result[1]
        conn.close()
    except :
        nickname = ""
    return nickname


def getMainPositionFromUserInfo(ctx) :
    try:
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM USER_INFORMATION WHERE ID=?", (ctx.author.id,))
        result = cur.fetchone()
        mainPosition = result[2]
        conn.close()
    except:
        mainPosition = ''
    return mainPosition


def getMainPositionFromUserInfoWithID(id) :
    try:
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM USER_INFORMATION WHERE ID=?", (id,))
        result = cur.fetchone()
        mainPosition = result[2]
        conn.close()
    except:
        mainPosition = ''
    return mainPosition


def getSubPositionFromUserInfo(ctx) :
    try:
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM USER_INFORMATION WHERE ID=?", (ctx.author.id,))
        result = cur.fetchone()
        subPosition = result[3]
        conn.close()
    except:
        subPosition = ''
    return subPosition


def getSubPositionFromUserInfoWithID(id) :
    try:
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM USER_INFORMATION WHERE ID=?", (id,))
        result = cur.fetchone()
        subPosition = result[3]
        conn.close()
    except:
        subPosition = ''
    return subPosition


def getTeamNameFromUserInfo(ctx) :
    try:
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM USER_INFORMATION WHERE ID=?", (ctx.author.id,))
        result = cur.fetchone()
        teaaName = result[4]
        conn.close()
    except:
        teaaName = ''
    return teaaName


def getTeamNameFromUserInfoWithID(id) :
    try:
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM USER_INFORMATION WHERE ID=?", (id,))
        result = cur.fetchone()
        teaaName = result[4]
        conn.close()
    except:
        teaaName = ''
    return teaaName


def getRankFromUserInfo(ctx) :
    try:
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM USER_INFORMATION WHERE ID=?", (ctx.author.id,))
        result = cur.fetchone()
        rank = result[5]
        conn.close()
    except:
        rank = ''
    return rank


def getRankFromUserInfoWithID(id) :
    try:
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM USER_INFORMATION WHERE ID=?", (id,))
        result = cur.fetchone()
        rank = result[5]
        conn.close()
    except:
        rank = ''
    return rank


def getNickChangeCouponFromUserInfo(ctx) :
    try:
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM USER_INFORMATION WHERE ID=?", (ctx.author.id,))
        result = cur.fetchone()
        nickChangeCoupon = result[6]
        conn.close()
    except:
        nickChangeCoupon = 0
    return nickChangeCoupon


def getNickChangeCouponFromUserInfoWithID(id) :
    try:
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM USER_INFORMATION WHERE ID=?", (id,))
        result = cur.fetchone()
        nickChangeCoupon = result[6]
        conn.close()
    except:
        nickChangeCoupon = 0
    return nickChangeCoupon


# ------------- TEAM_INFORMATION -------------


def getTeamFullNameFromTeamInfor(abbTeamName) :
    try:
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM TEAM_INFORMATION WHERE Abbreviation=?", (abbTeamName,))
        result = cur.fetchone()
        fullName = result[1]
    except:
        fullName =''
    return fullName


def getColorCodeFromTeamInfor(abbTeamName) :
    try:
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM TEAM_INFORMATION WHERE Abbreviation=?", (abbTeamName,))
        result = cur.fetchone()
        colorCode = result[2]
    except:
        colorCode =''
    return colorCode


def getLastRankFromTeamInfor(abbTeamName) :
    try:
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM TEAM_INFORMATION WHERE Abbreviation=?", (abbTeamName,))
        result = cur.fetchone()
        lastRank = result[3]
    except:
        lastRank =''
    return lastRank


# ------------- TOTS -------------

def getInforFromTotsFW(ctx) :
    text = ''
    conn = sqlite3.connect("CEF.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM TOTS_FW WHERE ID=?", (ctx.author.id,))
    data_list = cur.fetchall()
    data_list.sort(key=lambda x : x[1])  # Season 순으로 정렬
    for data in data_list :
        if data[2] :
            text = text + data[1] + " FW TOTS **1st**\n"
        elif data[3] :
            text = text + data[1] + " FW TOTS 2nd\n"

    return text


# ------------- HISTORY -------------

def getInfoFromSeasonUserHistory(ctx) :
    text = ''
    text_li = []
    conn = sqlite3.connect("CEF.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM SEASON_USER_HISTORY WHERE ID=?", (ctx.author.id,))
    data_list = cur.fetchall()
    data_list.sort(key=lambda x : x[1])  # Season 순으로 정렬
    print(data_list)
    for data in data_list :
        text = ''
        # print("C - ", data)
        # data / 1 : 시즌, 2 : 팀약자, 3 : 직책, 4 : 포지션, 5 : 순위(int)
        # text = text + getHostFromSeasonTeamCount(data[1]) + " " + data[1] + " 시즌 " + data[2] + " " + data[3] + " "\
        #       + data[4] + " " + str(data[5]) + "위 (" + str(getTotalCountFromSeasonTeamCount(data[1])) + "팀)\n"
        # print(text)
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

def getHostFromSeasonTeamCount(season) :
    try:
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM SEASON_TEAM_COUNT_INFORMATION WHERE Season=?", (season,))
        data = cur.fetchone()
        host = data[1]
    except:
        host = ''
    return host


def getTotalCountFromSeasonTeamCount(season) :
    try:
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM SEASON_TEAM_COUNT_INFORMATION WHERE Season=?", (season,))
        data = cur.fetchone()
        totalCount = data[2]
    except:
        totalCount = 0
    return totalCount


# ------------- CONTRACT -------------
def checkInsertOverapFromContract(ctx):
    conn = sqlite3.connect("CEF.db")
    cur = conn.cursor()
    cur.execute("SELECT StartDate FROM CONTRACT WHERE ID=?", (ctx.author.id,))
    result = cur.fetchone()
    if result is None:
        result2 = True
    else:
        result2 = False
    return result2

def checkInsertOverapFromContractWithID(idnum):
    conn = sqlite3.connect("CEF.db")
    cur = conn.cursor()
    cur.execute("SELECT StartDate FROM CONTRACT WHERE ID=?", (idnum,))
    result = cur.fetchone()
    if result is None:
        result2 = True
    else:
        result2 = False
    return result2

def getStartDateFromContract(ctx) :
    conn = sqlite3.connect("CEF.db")
    cur = conn.cursor()
    cur.execute("SELECT StartDate FROM CONTRACT WHERE ID=?", (ctx.author.id,))
    startDate = cur.fetchone()
    return startDate[0]


def getStartDateFromContractwithID(idNum) :
    conn = sqlite3.connect("CEF.db")
    cur = conn.cursor()
    cur.execute("SELECT StartDate FROM CONTRACT WHERE ID=?", (idNum,))
    startDate = cur.fetchone()
    return startDate[0]


def getPeriodFromContract(ctx) :
    conn = sqlite3.connect("CEF.db")
    cur = conn.cursor()
    cur.execute("SELECT Period FROM CONTRACT WHERE ID=?", (ctx.author.id,))
    period = cur.fetchone()
    return period[0]


def getPeriodFromContractwithID(idNum) :
    conn = sqlite3.connect("CEF.db")
    cur = conn.cursor()
    cur.execute("SELECT Period FROM CONTRACT WHERE ID=?", (idNum,))
    period = cur.fetchone()
    return period[0]


def getEndDateFromContract(ctx) :
    try :
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT EndDate FROM CONTRACT WHERE ID=?", (ctx.author.id,))
        endDate = cur.fetchone()
        result = endDate[0]
    except :
        result = ""
    return result


def getEndDateFromContractwithID(idNum) :
    try :
        conn = sqlite3.connect("CEF.db")
        cur = conn.cursor()
        cur.execute("SELECT EndDate FROM CONTRACT WHERE ID=?", (idNum,))
        endDate = cur.fetchone()
        result = endDate[0]
    except :
        result = ""
    return result
