import discord
from discord.ext import commands
from discord.utils import get
import random
import myfun


class Others(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='임시용', pass_context=True)
    async def _copypermission(self, ctx, name):
        pass

    @commands.command(name='포지션현황', aliases=["현황"], pass_context=True)
    async def _postionStatus(self, ctx, *, role_name):
        st_count = 0
        lw_count = 0
        rw_count = 0
        cam_count = 0
        cm_count = 0
        cdm_count = 0
        lb_count = 0
        cb_count = 0
        rb_count = 0
        gk_count = 0
        num = 0
        total = 0
        newbie_count = 0
        role = get(ctx.guild.roles, name=role_name)

        if role_name == "FA (무소속)" :
            fa_role = get(ctx.guild.roles, name="FA (무소속)")
            for member in fa_role.members :
                role_names = [role.name for role in member.roles]
                if "신규" in role_names :
                    newbie_count += 1

        for member in role.members :
            total += 1
            if "[" in member.display_name :
                print(member.display_name, myfun.getJupoFromDisplayname2(member.display_name))
                if myfun.getJupoFromDisplayname2(member.display_name) == 'ST' :
                    st_count = st_count + 1
                    num = num + 1
                elif myfun.getJupoFromDisplayname2(member.display_name) == 'LW' :
                    lw_count = st_count + 1
                    num = num + 1
                elif myfun.getJupoFromDisplayname2(member.display_name) == 'RW' :
                    rw_count = rw_count + 1
                    num = num + 1
                elif myfun.getJupoFromDisplayname2(member.display_name) == 'CAM' :
                    cam_count = cam_count + 1
                    num = num + 1
                elif myfun.getJupoFromDisplayname2(member.display_name) == 'CM' :
                    cm_count = cm_count + 1
                    num = num + 1
                elif myfun.getJupoFromDisplayname2(member.display_name) == 'CDM' :
                    cdm_count = cdm_count + 1
                    num = num + 1
                elif myfun.getJupoFromDisplayname2(member.display_name) == 'LB' :
                    lb_count = lb_count + 1
                    num = num + 1
                elif myfun.getJupoFromDisplayname2(member.display_name) == 'CB' :
                    cb_count = cb_count + 1
                    num = num + 1
                elif myfun.getJupoFromDisplayname2(member.display_name) == 'RB' :
                    rb_count = rb_count + 1
                    num = num + 1
                elif myfun.getJupoFromDisplayname2(member.display_name) == 'GK' :
                    gk_count = gk_count + 1
                    num = num + 1

        embed = discord.Embed(title=f"{role_name} 역할 주포지션 현황", description=f"총원 : {total} 명", color=0xFF007F)
        embed.add_field(name="ST", value=str(st_count) + " 명", inline=True)
        embed.add_field(name="LW", value=str(lw_count) + " 명", inline=True)
        embed.add_field(name="RW", value=str(rw_count) + " 명", inline=True)
        embed.add_field(name="CAM", value=str(cam_count) + " 명", inline=True)
        embed.add_field(name="CM", value=str(cm_count) + " 명", inline=True)
        embed.add_field(name="CDM", value=str(cdm_count) + " 명", inline=True)
        embed.add_field(name="LB", value=str(lb_count) + " 명", inline=True)
        embed.add_field(name="CB", value=str(cb_count) + " 명", inline=True)
        embed.add_field(name="RB", value=str(rb_count) + " 명", inline=True)
        embed.add_field(name="GK", value=str(gk_count) + " 명", inline=True)
        if role_name == "FA (무소속)" :
            embed.add_field(name="신규", value=str(newbie_count) + " 명", inline=True)
            embed.add_field(name="기존", value=str(total - newbie_count) + " 명", inline=True)
        embed.set_footer(text="Copyright ⓒ 2020-2023 타임제이(TimeJ) in C.E.F All Right Reserved.")
        await ctx.message.delete()
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Others(bot))