define ldissolve = Dissolve(1.0)
default f2r1_evflg_opening = True# f2r1初回起動時のイベントのフラグ
default f2r1_jumplabel = None  # この変数にラベル名を入れるとそこへジャンプする
default f2r1_exsist_flag = False #
default f2r1_first = True

label f2r1:
    $ move_room("loadfile2/room1")
    scene bg room

label .scloop:
    window hide
    show screen f2r1_screen(read_room()) with dissolve

    if f2r1_evflg_opening:  # f2r1初回起動時
        $ f2r1_evflg_opening = False
        $ Event("f2r1_ev_opening")()
    
    if f1r1_jumplabel == "f2r2":
        $ f2r1_jumplabel = None
        hide screen f2r1_screen with dissolve
        jump f2r2

    pause
    #正解のオブジェクトがあるかどうか
    python:
        import os
        import shutil

        f2r1_exsist_flag = os.path.exists(os.path.join(config.basedir,"game_data/loadfile2/room1/object3/Apple"))
        
        if f2r1_exsist_flag and f2r1_first:
            f2r1_first = False

            from_path = os.path.join(config.basedir,"game/images")
            to_path = os.path.join(config.basedir,"game_data/loadfile2/room1/box")
            if not os.path.exists(to_path):
                os.mkdir(to_path)
                shutil.copy(os.path.join(from_path,'box.png'),os.path.join(to_path,'box.png'))
            Event("f2r1_success")()

    
    jump .scloop
