default jumped_menu_ev_l1_clicked = False

label menu_ev_l1_clicked:
    # このラベルの訪問が初めてで、かつf1にジャンプ可能な時
    if not jumped_menu_ev_l1_clicked and menu_evflg_canjump_f1:
        $ jumped_menu_ev_l1_clicked = True  # このラベルを訪問済みに

        show girl smile at right onlayer screens with dissolve
        
        g "脱出ゲームステージ1の、はじまりはじまり"

        $ menu_jumplabel = "f1r1"

        hide girl

        return
    
    # f1へ2回目以降のジャンプ
    if menu_evflg_canjump_f1:

        $ menu_jumplabel = "f1r1"

        return

    return