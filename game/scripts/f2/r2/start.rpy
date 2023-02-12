default f2r2_evflg_opening = True
default f2r2_jump_event = None
default f2r2_ev_add_button_clicked_seen = False

label f2r2:
    if f2r2_evflg_opening:
        $ init_room("loadfile2/room2")
    $ move_room("loadfile2/room2")
    scene bg f2r2

label .scloop:
    window hide
    show screen f2r2_screen(read_room())

    if f2r2_evflg_opening:
        python:
            f2r2_evflg_opening = False
            Event("f2r2_ev_opening")()
    
    if f2r2_jump_event != None:
        python:
            renpy.dynamic(je=f2r2_jump_event)
            f2r2_jump_event = None
            Event(je)()
        
    pause
    jump .scloop

