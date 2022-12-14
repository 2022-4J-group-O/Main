default jumped_menu_ev_l3_clicked = False

label menu_ev_l3_clicked:
    # このラベルへの訪問が初めてで、f3にジャンプ可能な時
    if not jumped_menu_ev_l3_clicked and menu_evflg_canjump_f2:
        $ menu_jumplabel = "f3r1"
        
        show girl at right onlayer screens with dissolve

        g "f3を初めて訪れるときのセリフ"

        hide girl with dissolve

        return
    
    # f3へ2回目以降のジャンプ
    if menu_evflg_canjump_f3:

        $ menu_jumplabel = "f3r1"
        
        return
    
    # f3どころかf2にすらジャンプできないとき
    if not menu_evflg_canjump_f2:
        show girl smile at right onlayer screens with dissolve

        g "まずはセーブデータ1に行ってみよう"

        hide girl with dissolve

        return
    
    
    show girl smile at right onlayer screens with dissolve

    g "次はセーブデータ2に行ってみよう"

    hide girl with dissolve
    
    return
