default f3r2_evflg_opening = True

label f3r2:
    $ move_room("loadfile3/room2")
    scene bg f3r2

label .scloop:
    window hide
    show screen f3r2_screen(read_room())
    with dissolve

    if f3r2_evflg_opening:
        $ f3r2_evflg_opening = False
        $ Event("f3r2_ev_opening")()
    
    pause
    
    jump .scloop
