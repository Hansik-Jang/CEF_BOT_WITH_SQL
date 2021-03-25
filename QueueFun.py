import CEF_Test
import discord
import asyncio


async def queueList(ctx, lst):
    alert = ""
    try :
        for i in range(1, len(lst)):
            alert = alert + f"{i} . " + lst[i] + "\n"

        if alert == "":
            await ctx.send("대기열이 존재하지 않습니다. 등록해주세요.")
        else:
            await ctx.send("대기목록 \n")
            await ctx.send("```" + alert + "```")
    except:
        await ctx.send("대기열에 아무도 없습니다.")