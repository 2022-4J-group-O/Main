label title_show_screen:
    scene bg room with fade
    $ move_room('title')
    show screen title_screen(read_room())


label title_scloop:
    $ renpy.pause()
    show screen title_screen(read_room())
    jump title_scloop
