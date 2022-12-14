default jumped_menu_ev_l2_clicked = False

label menu_ev_l2_clicked:
    # このラベルへの訪問が初めてで、f2にジャンプ可能な時
    if not jumped_menu_ev_l2_clicked and menu_evflg_canjump_f2:
        $ menu_jumplabel = "f2r1"
        
        show girl at right onlayer screens with dissolve

        g "f2を初めて訪れるときのセリフ"

        hide girl with dissolve

        return
    
    # f2へ2回目以降のジャンプ
    if menu_evflg_canjump_f2:

        $ menu_jumplabel = "f2r1"
        
        return
    
    # f2へジャンプできないとき->f1へ行くことを促す
    show girl smile at right onlayer screens with dissolve

    g "まずはセーブデータ1に行ってみよう"

    hide girl with dissolve
    
    return