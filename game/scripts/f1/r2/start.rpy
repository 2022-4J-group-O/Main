default f1r2_evflg_opening = True
default f1r2_evflg_angry = False
default nhidden = []

label f1r2:
    $ move_room("loadfile1/room2")
    scene bg f1r2

label .scloop:
    window hide
    show screen f1r2_screen(read_room()) with dissolve

    $ nhidden = not_hidden()
    $ f1r2_evflg_angry = len(nhidden) > 0
    

    if f1r2_evflg_opening:

        $ f1r2_evflg_opening = False

        $ Event("f1r2_ev_opening")()

    if f1r2_evflg_angry:
        $ Event("f1r2_ev_angry")()
    
    pause

    jump .scloop
