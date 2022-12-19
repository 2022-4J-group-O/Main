default jumped_menu2_ev_l1_clicked = False

label menu2_ev_l1_clicked:
    # このラベルの訪問が初めてで、かつf1にジャンプ可能な時
    if not jumped_menu2_ev_l1_clicked and menu2_evflg_canjump_f1:
        $ jumped_menu2_ev_l1_clicked = True  # このラベルを訪問済みに

        show girl smile at right
        
        g "脱出ゲームステージ1の、はじまりはじまり"

        $ menu2_jumplabel = "f1r1"

        hide girl

    # f1へ2回目以降のジャンプ
    elif menu2_evflg_canjump_f1:

        $ menu2_jumplabel = "f1r1"

    $ event_end("menu2.scloop")