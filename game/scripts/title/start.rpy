"""
会話パート: プログラム起動直後のシーン
"""
define title_evflg_opening = True  # タイトル画面初回起動時のイベントフラグ

label title_start:
    $ move_room('title')
    scene bg title
    with fade


label .scloop:
    show screen title_screen(read_room())

    if title_evflg_opening:  # タイトル画面初回起動時
        $ title_evflg_opening = False  # タイトル画面初回起動時のフラグ無効化
        call say_about(calllabel_0="title_ev_opening", jumplabel_0="title_start.scloop")

    $ renpy.pause()

    jump .scloop
