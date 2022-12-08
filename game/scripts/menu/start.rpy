default menu_evflg_opening = True  # menu初回起動のイベントフラグ
default menu_evflg_canjump_f1 = True  # 現在はf1にジャンプ可能
default menu_evflg_canjump_f2 = False  # 現在はf2にジャンプ可能
default menu_evflg_canjump_f3 = False  # 現在はf3にジャンプ可能
default menu_jumplabel = None  # ジャンプするラベル

label menu_start:
    $ move_room('menu')
    scene bg loadfile with fade


label .scloop:
    show screen menu_screen(True)
    with dissolve

    if menu_evflg_opening:
        $ menu_evflg_opening = False
        call say_about(calllabel_0="menu_ev_opening", jumplabel_0="menu_start.scloop")
    
    if menu_jumplabel == "f1r1":
        $ menu_jumpflg_f1 = None
        hide screen menu_screen with dissolve
        jump f1r1_start

    if menu_jumplabel == "f2r1":
        $ menu_jumpflg_f2 = None
        hide screen menu_screen with dissolve
        jump f2r1_start

    if menu_jumplabel == "f3r1":
        $ menu_jumpflg_f3 = None
        hide screen menu_screen with dissolve
        jump f3r1_start

    pause

    jump .scloop
