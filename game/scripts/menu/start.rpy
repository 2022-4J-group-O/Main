default menu2_evflg_opening = True  # menu2初回起動のイベントフラグ
default menu2_evflg_canjump_f1 = True  # 現在はf1にジャンプ可能
default menu2_evflg_canjump_f2 = False  # 現在はf2にジャンプ可能
default menu2_evflg_canjump_f3 = False  # 現在はf3にジャンプ可能
default menu2_jumplabel = None  # ジャンプするラベル

label menu2:
    $ move_room('menu2')
    scene bg loadfile with fade


label .scloop:
    hide window
    show screen menu2_screen(True)
    with dissolve

    if menu2_evflg_opening:
        $ menu2_evflg_opening = False
        call say_about(calllabel_0="menu2_ev_opening", jumplabel_0="menu2.scloop")
    
    if menu2_jumplabel == "f1r1":
        $ menu2_jumpflg_f1 = None
        hide screen menu2_screen with dissolve
        jump f1r1

    if menu2_jumplabel == "f2r1":
        $ menu2_jumpflg_f2 = None
        hide screen menu2_screen with dissolve
        jump f2r1

    if menu2_jumplabel == "f3r1":
        $ menu2_jumpflg_f3 = None
        hide screen menu2_screen with dissolve
        jump f3r1

    pause

    jump .scloop
