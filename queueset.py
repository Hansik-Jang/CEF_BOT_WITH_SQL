import CEF_Test


def queueSet():
    st_queue = 0
    lw_queue = 0
    rw_queue = 0
    cam_queue = 0
    cm_queue = 0
    cdm_queue = 0
    lb_queue = 0
    cb_queue = 0
    rb_queue = 0
    gk_queue = 0
    a_team_form = ""
    b_team_form = ""
    if a_team_form == "4-3-3 홀딩":
        st_queue += 1
        lw_queue += 1
        rw_queue += 1
        cm_queue += 2
        cdm_queue += 1
        lb_queue += 1
        cb_queue += 2
        rb_queue += 1
        gk_queue += 1
    elif a_team_form == "3-5-2": #윙백은 풀백으로 처리
        st_queue += 2
        cam_queue += 1
        cdm_queue += 2
        lb_queue += 1
        rb_queue += 1
        cb_queue += 3
        gk_queue += 1
    elif a_team_form == "3-4-3 플랫": #윙백은 풀백으로 처리
        st_queue += 1
        lw_queue += 1
        rw_queue += 1
        cm_queue += 2
        lb_queue += 1
        rb_queue += 1
        cb_queue += 3
        gk_queue += 1
    elif a_team_form == "4-1-2-1-2 넓게":
        st_queue += 2
        cam_queue += 1
        lw_queue += 1
        rw_queue += 1
        cdm_queue += 1
        lb_queue += 1
        rb_queue += 1
        cb_queue += 2
        gk_queue += 1
    elif a_team_form == "4-4-2 플랫":
        st_queue += 2
        lw_queue += 1
        rw_queue += 1
        cm_queue += 2
        lb_queue += 1
        cb_queue += 2
        rb_queue += 1
        gk_queue += 1
    elif a_team_form == "4-2-3-1 넓게":
        st_queue += 1
        lw_queue += 1
        rw_queue += 1
        cam_queue += 1
        cdm_queue += 2
        lb_queue += 1
        cb_queue += 2
        rb_queue += 1
        gk_queue += 1
    elif a_team_form == "3-4-3 다이아몬드":
        st_queue += 1
        lw_queue += 1
        rw_queue += 1
        cm_queue += 2
        lb_queue += 1
        cb_queue += 3
        rb_queue += 1
        gk_queue += 1
    elif a_team_form == "5-3-2":
        st_queue += 2
        cm_queue += 3
        lb_queue += 1
        cb_queue += 3
        rb_queue += 1
        gk_queue += 1
    elif a_team_form == "4-1-2-1-2 좁게":
        st_queue += 2
        cam_queue += 1
        cm_queue += 2
        cdm_queue += 1
        lb_queue += 1
        rb_queue += 1
        cb_queue += 2
        gk_queue += 1
    elif a_team_form == "3-5-1-1": # CF는 CAM 처리
        st_queue += 1
        cam_queue += 1
        cm_queue += 2
        cdm_queue += 1
        lb_queue += 1
        rb_queue += 1
        cb_queue += 2
        gk_queue += 1
    elif a_team_form == "4-5-1 공격":
        st_queue += 1
        lw_queue += 1
        rw_queue += 1
        cam_queue += 2
        cm_queue += 1
        lb_queue += 1
        rb_queue += 1
        cb_queue += 2
        gk_queue += 1
    # B팀 큐 생성
    if b_team_form == "4-3-3 홀딩":
        st_queue += 1
        lw_queue += 1
        rw_queue += 1
        cm_queue += 2
        cdm_queue += 1
        lb_queue += 1
        cb_queue += 2
        rb_queue += 1
        gk_queue += 1
    elif b_team_form == "3-5-2": #윙백은 풀백으로 처리
        st_queue += 2
        cam_queue += 1
        cdm_queue += 2
        lb_queue += 1
        rb_queue += 1
        cb_queue += 3
        gk_queue += 1
    elif b_team_form == "3-4-3 플랫": #윙백은 풀백으로 처리
        st_queue += 1
        lw_queue += 1
        rw_queue += 1
        cm_queue += 2
        lb_queue += 1
        rb_queue += 1
        cb_queue += 3
        gk_queue += 1
    elif b_team_form == "4-1-2-1-2 넓게": # LM, RM은 LW, RW으로 처리
        st_queue += 2
        cam_queue += 1
        lw_queue += 1
        rw_queue += 1
        cdm_queue += 1
        lb_queue += 1
        rb_queue += 1
        cb_queue += 2
        gk_queue += 1
    elif b_team_form == "4-4-2 플랫": # LM, RM은 LW, RW으로 처리
        st_queue += 2
        lw_queue += 1
        rw_queue += 1
        cm_queue += 2
        lb_queue += 1
        cb_queue += 2
        rb_queue += 1
        gk_queue += 1
    elif b_team_form == "4-2-3-1 넓게":
        st_queue += 1
        lw_queue += 1
        rw_queue += 1
        cam_queue += 1
        cdm_queue += 2
        lb_queue += 1
        cb_queue += 2
        rb_queue += 1
        gk_queue += 1
    elif b_team_form == "3-4-3 다이아몬드":
        st_queue += 1
        lw_queue += 1
        rw_queue += 1
        cm_queue += 2
        lb_queue += 1
        cb_queue += 3
        rb_queue += 1
        gk_queue += 1
    elif b_team_form == "5-3-2": # 윙백은 풀백으로 처리
        st_queue += 2
        cm_queue += 3
        lb_queue += 1
        cb_queue += 3
        rb_queue += 1
        gk_queue += 1
    elif b_team_form == "4-1-2-1-2 좁게":
        st_queue += 2
        cam_queue += 1
        cm_queue += 2
        cdm_queue += 1
        lb_queue += 1
        rb_queue += 1
        cb_queue += 2
        gk_queue += 1
    elif b_team_form == "3-5-1-1": # CF는 CAM 처리
        st_queue += 1
        cam_queue += 1
        cm_queue += 2
        cdm_queue += 1
        lb_queue += 1
        rb_queue += 1
        cb_queue += 2
        gk_queue += 1
    elif b_team_form == "4-5-1 공격": # LM, RM은 LW, RW으로 처리
        st_queue += 1
        lw_queue += 1
        rw_queue += 1
        cam_queue += 2
        cm_queue += 1
        lb_queue += 1
        rb_queue += 1
        cb_queue += 2
        gk_queue += 1

    return st_queue, lw_queue, rw_queue,cam_queue,cm_queue,cdm_queue,lb_queue,cb_queue,rb_queue,gk_queue
