default title_evflg_opening = True  # タイトル画面初回起動時のイベントフラグ

label title:
    if title_evflg_opening:  # タイトル画面初回起動時
        $ init_room("title")
    $ move_room('title')
    scene bg title

    $ loop_count = 0
label .pause_loop:
    show screen title_screen(read_room()) with dissolve
    pause
    $ loop_count += 1
    if loop_count < 10:
        jump .pause_loop

label .scloop:
    window hide
    show screen title_screen(read_room()) with dissolve

    if title_evflg_opening:  # タイトル画面初回起動時
        $ title_evflg_opening = False  # タイトル画面初回起動時のフラグ無効化
        $ Event("title_ev_opening")()

    pause

    jump .scloop
