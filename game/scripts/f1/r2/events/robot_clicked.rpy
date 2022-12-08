# ロボットをクリックしたとき
default f1r2_jumped_robot_clicked = False

label f1r2_ev_robot_clicked:
    show screen f1r2_screen(read_room(), False)  # ロボットを不可視に
    show robot1 onlayer screens
    with dissolve

    if not f1r2_jumped_robot_clicked:
        $ f1r2_jumped_robot_clicked = True

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
