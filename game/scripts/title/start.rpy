default title_evflg_opening = True  # タイトル画面初回起動時のイベントフラグ

label title:
    if title_evflg_opening:  # タイトル画面初回起動時
        $ init_room("title")
    $ move_room('title')
    scene bg title with Fade(2.0, 1.0, 2.0)

    show screen title_screen(read_room()) with dissolve

    pause
    pause
    pause
    pause
    pause
    pause
    pause
    pause
    pause
    pause

label .scloop:
    window hide
    show screen title_screen(read_room()) with dissolve

    if title_evflg_opening:  # タイトル画面初回起動時
        $ title_evflg_opening = False  # タイトル画面初回起動時のフラグ無効化
        $ Event("title_ev_opening")()

    pause

    jump .scloop
