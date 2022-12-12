define ldissolve = Dissolve(1.0)
default f1r1_evflg_opening = True  # 初回起動時フラグ

label f1r1:
    $ move_room('loadfile1/room1')
    scene bg f1r1 with dissolve

label .scloop:
    hide window
    show screen f1r1_screen(read_room())

    # 最初の一回だけ会話が流れる
    if f1r1_evflg_opening:
        $ f1r1_evflg_opening = False
        call say_about("f1r1_ev_opening", "f1r1.scloop")

    pause

    jump .scloop
