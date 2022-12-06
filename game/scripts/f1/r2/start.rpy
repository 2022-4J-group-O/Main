label f1r2_start:
    $ move_room("loadfile1/room2")
    scene bg f1r2
    show screen f1r2_screen(read_room())
    if renpy.seen_label("f1r2_start"):
        show girl onlayer screens with dissolve
        g "雑談を入れよう"
        g "ちなみにこうすると"
        show girl onlayer screens zorder 1 with dissolve
        g "メッセージウィンドウの前に来れることを発見したんだよね"
        hide girl onlayer screens with dissolve
        window hide
        jump f1r2_show_screen