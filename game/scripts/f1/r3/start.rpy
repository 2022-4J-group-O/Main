default f1r3_evflg_opening = True

label f1r3:
    $ move_room("loadfile1/room3")
    scene bg f1r3

label .scloop:
    window hide
    show screen f1r3_screen(read_room()) with dissolve

    if f1r3_evflg_opening:
        $ f1r3_evflg_opening = False
        $ Event("f1r3_ev_opening")()

    pause
    
    jump .scloop