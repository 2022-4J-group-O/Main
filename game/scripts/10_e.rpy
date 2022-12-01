label e10:
    scene bg room with fade
    $ move_room('loadfile1/room1')
    show screen e10_screen(read_room())


label e10_pause:
    $ renpy.pause()
    show screen e10_screen(read_room())
    jump e10_pause


label door_is_clickable:
    hide screen e10_screen
    return 