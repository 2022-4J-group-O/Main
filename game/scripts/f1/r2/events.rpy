init python:
    import shutil
    # オブジェクトを移動する関数
    def move_obj(objlist, path=None):
        if path == None:
            os.chdir(os.path.join(user_dir_path, "loadfile1/room2"));
            path = "../room1"
        for o in objlist:
            shutil.move(o, path)
    # 隠しファイルでないファイルを取得
    def not_hidden():
        os.chdir(os.path.join(user_dir_path, "loadfile1/room2"))
        l = read_room("loadfile1/room2")
        return [p for p in l if not is_hidden_file(p)]

label f1r2:

# 隠しファイルのチェック
# 隠しファイルでないファイルが見つからなかったらjlblに飛ぶ(jlblはreturnするべき)
label .check(jlbl):
    $ nhidden = not_hidden()
    if len(nhidden) > 0:
        jump .robot_angry
    jump expression jlbl

# ロボットをクリックしたとき
label .robot_clicked:
    show screen f1r2_screen(read_room(), False)
    show robot1 onlayer screens
    with dissolve
    if not renpy.seen_label("f1r2.robot_clicked"):
        ro1 "これは一回目の会話です"
        ro1 "ロボットが喋る"
        ro1 "<自己紹介的なこと> <少女との会話もあってもいい>"
        hide robot1 onlayer screens
        show girl onlayer screens with dissolve
        g "呼んだ？"
        hide girl onlayer screens with dissolve
    else:
        ro1 "これは2回目以降の会話です"
        hide robot1 onlayer screens with dissolve
    window hide
    return

# 隠しファイルでないオブジェクトが見つかったとき
label .robot_angry:
    show screen f1r2_screen(read_room(), False)
    show robot1 angry onlayer screens
    with dissolve
    ro1 "激おこ"
    $ move_obj(nhidden)
    show screen f1r2_screen(read_room())
    with dissolve
    hide robot1 angry onlayer screens with dissolve
    return