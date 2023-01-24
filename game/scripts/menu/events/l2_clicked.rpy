default jumped_menu2_ev_l2_clicked = False
#testのためf2に直接いけるようにしてある

label menu2_ev_l2_clicked:

    show screen menu2_screen(False)

    # このラベルへの訪問が初めてで、f2にジャンプ可能な時
    if not jumped_menu2_ev_l2_clicked and menu2_evflg_canjump_f2:
        $ jumped_menu2_ev_l2_clicked = True
        $ menu2_jumplabel = "f2r1"

        show girl look away at right with dissolve

        g "......気を取り直して、ステージ2だよ"

        $ menu2_jumplabel = "f2r1"

        hide girl with dissolve

    # f2へ2回目以降のジャンプ
    elif menu2_evflg_canjump_f2:

        $ menu2_jumplabel = "f2r1"


    # f2へジャンプできないとき->f1へ行くことを促す
    else :
        show girl at right with dissolve
        g "まずはセーブデータ1に行ってみよう"
        hide girl with dissolve

    $ event_end("menu2.scloop")