default menu2_evflg_opening = True  # menu2初回起動のイベントフラグ
default menu2_evflg_opening_f2 = False  # f2直前のイベントフラグ
default menu2_evflg_opening_f3 = False  # f3直前のイベントフラグ
default menu2_evflg_canjump_f1 = True  # 現在はf1にジャンプ可能
default menu2_evflg_canjump_f2 = False  # 現在はf2にジャンプ可能(f2のテスト用)
default menu2_evflg_canjump_f3 = False  # 現在はf3にジャンプ可能
default menu2_jumplabel = None  # ジャンプするラベル

label menu2:
    $ move_room('menu2')
    scene bg loadfile with fade


label .scloop:
    window hide
    show screen menu2_screen(True)
    with dissolve

    if menu2_evflg_opening:
        $ menu2_evflg_opening = False
        $ Event("menu2_ev_opening")()

    if menu2_evflg_opening_f2:
        $ menu2_evflg_opening_f2 = False
        $ Event("menu2_ev_opening_f2")()
    
    if menu2_jumplabel == "f1r1":
        $ menu2_jumplabel = None
        hide screen menu2_screen with dissolve
        jump f1r1

    if menu2_jumplabel == "f2r1":
        $ menu2_jumplabel = None
        hide screen menu2_screen with dissolve
        jump f2r1

    if menu2_jumplabel == "f3r1":
        $ menu2_jumplabel = None
        hide screen menu2_screen with dissolve
        jump f3r1

    pause

    jump .scloop
