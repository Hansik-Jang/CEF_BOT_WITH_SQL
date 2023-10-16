import sqlite3


def getInforAboutTeamInfo():
    pass


def getUserInformation(ctx):
    conn = sqlite3.connect("CEF.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM USER_INFORMATION WHERE ID=?", (ctx.author.id,))
    result = cur.fetchone()
    conn.close()

    print(result)
    return result
