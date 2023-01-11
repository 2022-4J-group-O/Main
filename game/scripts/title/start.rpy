default title_evflg_opening = True  # タイトル画面初回起動時のイベントフラグ

label title:
    $ move_room('title')
    scene bg title with dissolve

label .scloop:
    window hide
    show screen title_screen(read_room()) with dissolve

    if title_evflg_opening:  # タイトル画面初回起動時
        python:
            init_room("title")

            title_evflg_opening = False  # タイトル画面初回起動時のフラグ無効化

            Event("title_ev_opening")()

    pause

    jump .scloop
