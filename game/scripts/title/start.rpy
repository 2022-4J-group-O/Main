default title_evflg_opening = True  # タイトル画面初回起動時のイベントフラグ

label title:
    if title_evflg_opening:  # タイトル画面初回起動時
        $ init_room("title")
    $ move_room('title')
    scene bg title with Fade(2.0, 1.0, 2.0)

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

    python:
        if jump_label != None:
            tmp = jump_label
            jump_label = None
            Event(tmp)()

    if title_evflg_opening:  # タイトル画面初回起動時
        $ title_evflg_opening = False  # タイトル画面初回起動時のフラグ無効化
        $ Event("title_ev_opening")()

    pause

    jump .scloop
