default f3r1_evflg_opening = True

label f3r1:
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