# 隠しファイルでないオブジェクトが見つかったとき
label f1r2_ev_angry:
    show robot1 angry onlayer screens
    with dissolve

    ro1 "この部屋に、"

    ro1 "無駄ながらくたを、"

    ro1 "持ち込むなー！！！！"

    $ move_obj(nhidden)
    show screen f1r2_screen(read_room())
    with dissolve

    hide robot1 angry onlayer screens with dissolve
    return