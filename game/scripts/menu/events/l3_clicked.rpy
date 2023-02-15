default jumped_menu2_ev_l3_clicked = False

label menu2_ev_l3_clicked:

    show screen menu2_screen(False)

    # このラベルへの訪問が初めてで、f3にジャンプ可能な時
    if not jumped_menu2_ev_l3_clicked and menu2_evflg_canjump_f3:
        $ menu2_jumplabel = "f3r1"
        
        show girl at right with dissolve

        g "いよいよ最後のセーブデータだね"

        hide girl with dissolve

    # f3へ2回目以降のジャンプ
    elif menu2_evflg_canjump_f3:

        $ menu2_jumplabel = "f3r1"

    # f3どころかf2にすらジャンプできないとき
    elif not menu2_evflg_canjump_f2:
        show girl smile at right with dissolve

        g "まずはセーブデータ1に行ってみよう"

        hide girl with dissolve

    # f2にはジャンプできるとき
    else:
        show girl smile at right with dissolve

        g "次はセーブデータ2に行ってみよう"

        hide girl with dissolve

    $ event_end("menu2.scloop")
