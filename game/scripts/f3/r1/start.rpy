default f3r1_evflg_opening = True

label f3r1:
    if f1r3_evflg_opening:  # f3r1初回起動時
        $ init_room("loadfile3/room1")
        # room2も生成しておく(どこでもドアのヒント)
        $ init_room("loadfile3/room2")
    $ move_room("loadfile3/room1")
    scene bg f3r1

label .scloop:
    window hide
    show screen f3r1_screen(read_room())
    with dissolve

    if f3r1_evflg_opening:
        $ f3r1_evflg_opening = False
        $ Event("f3r1_ev_opening")()
    
    pause
    
    jump .scloop