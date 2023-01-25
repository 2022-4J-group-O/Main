define ldissolve = Dissolve(1.0)
default f1r1_evflg_opening = True  # f1r1初回起動時のイベントのフラグ

label f1r1:
    if f1r1_evflg_opening:  # f1r1初回起動時
        $ init_room("loadfile1/room1")
    $ move_room("loadfile1/room1")
    scene bg f1r1

label .scloop:
    window hide
    show screen f1r1_screen(read_room()) with dissolve

    if f1r1_evflg_opening:  # f1r1初回起動時
        $ f1r1_evflg_opening = False
        # $ Event("f1r1_ev_opening")()
    
    pause
    
    jump .scloop
