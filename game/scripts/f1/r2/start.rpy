default f1r2_evflg_opening = True
default f1r2_evflg_angry = False
default nhidden = []
default f1r2_hidden_clicked = False  # VaseまたはChestがクリックされたか

label f1r2:
    if f1r2_evflg_opening:
        $ init_room("loadfile1/room2")
    $ move_room("loadfile1/room2")
    scene bg f1r2

label .scloop:
    window hide
    show screen f1r2_screen(read_room()) with dissolve

    python:
        if jump_label != None:
            tmp = jump_label
            jump_label = None
            Event(tmp)()

    $ nhidden = not_hidden()
    $ f1r2_evflg_angry = len(nhidden) > 0
    

    if f1r2_evflg_opening:
        $ f1r2_evflg_opening = False
        $ Event("f1r2_ev_opening")()

    if f1r2_evflg_angry:
        $ Event("f1r2_ev_angry")()
    
    pause

    jump .scloop
