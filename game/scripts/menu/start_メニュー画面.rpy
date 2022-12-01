label menu_start:
    scene bg loadfile with fade
    show screen menu_screen(False)
    show girl onlayer screens # screensレイヤーに表示しないとloadfileの後ろに行ってしまう
    g "ここのセリフはまだできてないよ"
    hide girl onlayer screens
    with fade
    jump menu_show_screen