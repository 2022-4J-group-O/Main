label menu_d_opening:
    scene bg loadfile with fade
    show screen menu_e_screen(False)
    show girl onlayer screens # screensレイヤーに表示しないとloadfileの後ろに行ってしまう
    g "ここのセリフはまだできてないよ"
    hide girl onlayer screens
    with fade
    jump menu_e 