default f2r3_evflg_opening = True

label f2r3:
    $ move_room("f2r3")

    scene bg f1r4

    if f2r3_evflg_opening:

        pause
        pause
        pause

        $ f2r3_evflg_opening = False

        show girl look away with dissolve

        g "......あー"

        g "......まただ"

        g "何度もごめんね、すぐに戻すから"

        g "......"

        # menuで、f3直前イベントを起こす
        $ menu2_evflg_opening_f3 = True
        # menuで、f3を解放
        $ menu2_evflg_canjump_f3 = True
        jump menu2
    
    else:
        jump menu2
