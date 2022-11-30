label d07:
    scene bg loadfile with fade
    show screen e08_loadfile(False)
    show girl onlayer screens # screensレイヤーに表示しないとloadfileの後ろに行ってしまう
    g "ここのセリフはまだできてないよ"
    hide girl onlayer screens
    with fade
    jump e08