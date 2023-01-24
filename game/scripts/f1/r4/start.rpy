default f1r4_evflg_opening = True

label f1r4:
    scene bg f1r4

    if f1r4_evflg_opening:
        $ f1r4_evflg_opening = False

        pause
        pause
        pause

        g "......あー"

        g "これは......その......"

        g "バグってやつだね"

        g "これより先に進むのは難しそうだよ"

        g "少し待ってね"

        g "......"

        # menuで、f2直前イベントを起こす
        $ menu2_evflg_opening_f2 = True
        # menuで、f2を解放
        $ menu2_evflg_canjump_f2 = True
        jump menu2
    
    else:
        jump menu2
