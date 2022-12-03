label f1r1_show_screen:
    scene bg f1r1 with fade
    $ move_room('loadfile1/room1')
    show screen f1r1_screen(read_room())


label f1r1_scloop:
    $ renpy.pause()
    show screen f1r1_screen(read_room())
    jump f1r1_scloop

