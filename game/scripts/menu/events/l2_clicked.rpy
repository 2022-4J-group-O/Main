default jumped_menu2_ev_l2_clicked = False
#testのためf2に直接いけるようにしてある

label menu2_ev_l2_clicked:
    # このラベルへの訪問が初めてで、f2にジャンプ可能な時
    if not jumped_menu2_ev_l2_clicked and menu2_evflg_canjump_f2:
        $ menu2_jumplabel = "f2r1"

        show girl at right

        g "f2を初めて訪れるときのセリフ"
        $ menu2_jumplabel = "f2r1"

        hide girl
      

    # f2へ2回目以降のジャンプ
    elif menu2_evflg_canjump_f2:

        $ menu2_jumplabel = "f2r1"


    # f2へジャンプできないとき->f1へ行くことを促す
    show girl smile at right

    g "まずはセーブデータ1に行ってみよう"

    hide girl

    $ event_end("menu2.scloop")