default f1r2_evflg_opening = True
default f1r2_evflg_angry = False
default nhidden = []

label f1r2:
    $ move_room("loadfile1/room2")
    scene bg f1r2

label .scloop:
    show screen f1r2_screen(read_room()) with dissolve

    $ nhidden = not_hidden()
    $ f1r2_evflg_angry = len(nhidden) > 0
    

    if f1r2_evflg_opening:

        $ f1r2_evflg_opening = False

        call say_about("f1r2_ev_opening", "f1r2.scloop")

    if f1r2_evflg_angry:
        call say_about("f1r2_ev_angry", "f1r2.scloop")
    
    pause

    jump .scloop
