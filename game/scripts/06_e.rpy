label e06:
    scene bg room with fade
    $ move_room('title')
    show screen e06(read_room())


label e06_pause:
    $ renpy.pause()
    show screen e06(read_room())
    jump e06_pause

label e06_clicked_start:
    hide screen e06
    return 