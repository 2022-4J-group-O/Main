default jumped_menu2_ev_l3_clicked = False

label menu2_ev_l3_clicked:
    # このラベルへの訪問が初めてで、f3にジャンプ可能な時
    if not jumped_menu2_ev_l3_clicked and menu2_evflg_canjump_f2:
        $ menu2_jumplabel = "f3r1"
        
        show girl at right

        g "f3を初めて訪れるときのセリフ"

        hide girl

        return
    
    # f3へ2回目以降のジャンプ
    if menu2_evflg_canjump_f3:

        $ menu2_jumplabel = "f3r1"
        
        return
    
    # f3どころかf2にすらジャンプできないとき
    if not menu2_evflg_canjump_f2:
        show girl smile at right

        g "まずはセーブデータ1に行ってみよう"

        hide girl

        return
    
    
    show girl smile at right

    g "次はセーブデータ2に行ってみよう"

    hide girl
    
    return
