define ldissolve = Dissolve(1.0)
default f2r1_evflg_opening = True# f2r1初回起動時のイベントのフラグ
default f2r1_jumplabel = None  # この変数にラベル名を入れるとそこへジャンプする
default f2r1_exist_flag = False #
default f2r1_first = True

label f2r1:
    $ move_room("loadfile2/room1")
    scene bg f2r1 

label .scloop:
    window hide
    show screen f2r1_screen(read_room()) with dissolve

    if f2r1_evflg_opening:  # f2r1初回起動時
        $ f2r1_evflg_opening = False
        $ Event("f2r1_ev_opening")()
    
    if f2r1_jumplabel == "f2r2":
        $ f2r1_jumplabel = None
        hide screen f2r1_screen with dissolve
        jump f2r2

    pause
    #正解のオブジェクトがあるかどうか
    python:
        import os
        import shutil

        f2r1_exist_flag = os.path.exists(os.path.join(config.basedir,"game_data/loadfile2/room1/objectC/Cup"))
        
        if f2r1_exist_flag and f2r1_first:
            f2r1_first = False

            from_path = os.path.join(config.basedir,"game\images\door_noise_img")
            to_path = os.path.join(config.basedir,"game_data/loadfile2/room1/box") #出現する箱
            if not os.path.exists(to_path):
                os.mkdir(to_path)
                shutil.copy(os.path.join(from_path,'e.png'),os.path.join(to_path,'e.png'))
                shutil.copy(os.path.join(from_path,'f.png'),os.path.join(to_path,'f.png'))
            Event("f2r1_success")()

    
    jump .scloop
