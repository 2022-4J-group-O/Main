define ldissolve = Dissolve(1.0)
define box_path = "box"
define f2r1_path = "loadfile2/room1"
define picture_paths = ("picture frame A/pic_A.png", "picture frame B/pic_B.png", "picture frame C/pic_C.png")

default f2r1_evflg_opening = True # f2r1初回起動時のイベントのフラグ
# default f2r1_jumplabel = None  # この変数にラベル名を入れるとそこへジャンプする
default f2r1_exist_flag = False #
default f2r1_first = True

init python:
    # boxを出現させる
    def f2r1_gen_box():
        p = os.path.join(user_directory, f2r1_path, box_path)
        check_folder_new(config.basedir, p)
        global_data.default_dir_data.make(os.path.join(config.basedir, p), os.path.join(f2r1_path, box_path))
    
    def f2r1_exist_box():
        return os.path.isdir(os.path.join(config.basedir, user_directory, f2r1_path, box_path))
    
    def f2r1_pictures_exist():
        base = os.path.join(config.basedir, user_directory, f2r1_path)
        return (
            check_hash_binary(os.path.join(base, picture_paths[0])),
            check_hash_binary(os.path.join(base, picture_paths[1])),
            os.path.isfile(os.path.join(base, picture_paths[2]))
        )
    
    def f2r1_check_objects():
        return check_obj("Cup", os.path.join(f2r1_path, "object C")) and check_obj("Apple", os.path.join(f2r1_path, "object A")) and check_obj("Dog", os.path.join(f2r1_path, "object B"))


label f2r1:
    if f2r1_evflg_opening:
        $ init_room("loadfile2/room1")
    $ move_room("loadfile2/room1")
    scene bg f2r1 

label .scloop:
    window hide
    show screen f2r1_screen(read_room(), f2r1_exist_box(), f2r1_pictures_exist()) with dissolve

    if f2r1_evflg_opening:  # f2r1初回起動時
        $ f2r1_evflg_opening = False
        $ Event("f2r1_ev_opening")()

    pause
    # 正解のオブジェクトがあるかどうか
    python:
        # import os
        # import shutil

        

        if f2r1_first and f2r1_check_objects():
            f2r1_first = False
            f2r1_gen_box()
            Event("f2r1_success")()


    jump .scloop
