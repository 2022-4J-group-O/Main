default jumped_menu_ev_l1_clicked = False

label menu_ev_l1_clicked:
    show girl at right

    if menu_evflg_canjump_f1:

        g "l1にいくよ"

        $ menu_jumplabel = "f1r1"

        return

    
    g "l1がクリックされたよ"
    
    hide girl

    return