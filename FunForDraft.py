from myfun import *


def makeListFromList(li):
    text = ''
    for i in range(len(li)):
        if i == len(li) or i == 0:
            text = text + getNickFromDisplayname2(li[i])
        else:
            text = text + ', ' + getNickFromDisplayname2(li[i])

    text = text + ''
    return text


def ForEmbedFromList(li):
    temp = ''
    if len(li) == 0:
        temp = 'X'
    else:
        for i in range(len(li)):
            if i == len(li):
                temp = temp + str(i + 1) + "." + li[i]
            else:
                temp = temp + str(i + 1) + ". " + li[i] + "\n"

    return temp