"""
スタートボタンがクリックされたときの処理
"""

label title_start_clicked:
    call title_ev_start_clicked
    return

label title_ev_start_clicked:
    hide screen title_screen

    show girl

    g "さて、今度こそゲームスタートだね。"

    hide girl
    
    return 
