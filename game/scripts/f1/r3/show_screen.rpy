label f1r3_show_screen:
    scene bg room with fade
    $ move_room('loadfile1/room3')
    show screen f1r3_screen(read_room())


label f1r3_scloop:
    $ renpy.pause()
    show screen f1r3_screen(read_room())
    jump f1r3_scloop

