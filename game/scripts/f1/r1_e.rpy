label f1r1_e:
    scene bg room with fade
    $ move_room('loadfile1/room1')
    show screen f1r1_e_screen(read_room())


label f1r1_e_pause:
    $ renpy.pause()
    show screen f1r1_e_screen(read_room())
    jump f1r1_e_pause 


label f1r1_door_clicked:
    hide screen f1r1_e_screen
    return 