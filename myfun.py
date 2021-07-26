def convertNick(ctx):
    temp = ctx.author.display_name.split('[')
    nickname = temp[0].strip()
    return nickname

def convertJupo(ctx):
    a = ctx.author.display_name.split('[')
    temp = a[1]
    if '/' in ctx.author.display_name:
        b = temp.split('/')
        jupo = b[0]
        return jupo
    else:
        b = temp.split(']')
        jupo = b[0]
        return jupo

def convertBupo(ctx):
    a = ctx.author.display_name.split('/')
    temp = a[1]
    b = temp.split(']')
    bupo = b[0]
    return bupo

def assembleExcludeBupo(ctx):
    nickname = convertNick(ctx)
    jupo = convertJupo(ctx)
    result = nickname + "[" + jupo + "]"
    return result

def assembleIncludeBupo(ctx):
    nickname = convertNick(ctx)
    jupo = convertJupo(ctx)
    bupo = convertBupo(ctx)
    result = nickname + "[" + jupo + "/" + bupo + "]"
    return result