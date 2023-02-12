default f1r4_evflg_opening = True

image bg f1r4:
    choice:
        "bg f1r4 1"
    choice:
        "bg f1r4 2"
    choice:
        "bg f1r4 3"
    choice:
        "bg f1r4 4"
    choice:
        "bg f1r4 5"
    choice:
        "bg f1r4 6"
    pause 0.1
    repeat

label f1r4:
    $ move_room("f1r4")

    scene bg f1r4

    if f1r4_evflg_opening:

        pause
        pause
        pause

        $ Event("f1r4_dialogue")()

        # menuで、f2直前イベントを起こす
        $ menu2_evflg_opening_f2 = True
        # menuで、f2を解放
        $ menu2_evflg_canjump_f2 = True
        jump menu2
    
    else:
        jump menu2

label f1r4_dialogue:
    show girl look away with dissolve
    
    g "......あー"

    g "これは......その......"

    g "バグってやつだね"

    g "これより先に進むのは難しそうだよ"

    g "少し待ってね"

    g "......"

    hide girl with dissolve

    $ event_end()
