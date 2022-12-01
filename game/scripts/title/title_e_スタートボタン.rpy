label title_e:
    scene bg room with fade
    $ move_room('title')
    show screen title_e_screen(read_room())


label title_e_pause:
    $ renpy.pause()
    show screen title_e_screen(read_room())
    jump title_e_pause

label title_e_start_clicked:
    hide screen title_e_screen
    return 