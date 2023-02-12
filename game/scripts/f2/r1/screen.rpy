# exist_box: boolean
# boxを表示するか
# exist_picture: (boolean, boolean, boolean)
# 3つの絵画をそれぞれ表示するか
screen f2r1_screen(current, exist_box, exist_picture):
    layer "master"
    #固定表示のやつ

    add "bg f2r1" xpos 1.0

    imagebutton:
        anchor (0.0, 0.0)
        pos (1.0, 0.0)
        offset (82, 194)
        if exist_picture[0]:
            # リンゴの絵画を表示
            idle "pic_a"
            hover "pic_a"
        else:
            # エラー画像
            idle "error"
            hover "error"
    
    imagebutton:
        anchor (0.0, 0.0)
        pos (1.0, 0.0)
        offset (747, 194)
        if exist_picture[1]:
            # 犬の絵画を表示
            idle "pic_b"
            hover "pic_b"
        else:
            # エラー画像
            idle "error"
            hover "error"

    imagebutton:
        anchor (0.0, 0.0)
        pos (1.0, 0.0)
        offset (1412, 195)
        if exist_picture[2]:
            # コップの絵画を表示
            idle "pic_c"
            hover "pic_c"
        else:
            # エラー画像
            idle "error"
            hover "error"

    imagebutton:
        anchor (0.0, 0.0)
        pos (1.0, 0.0)
        offset (68, 178)
        idle "frame 1"
        hover "frame 1"

    imagebutton:
        anchor (0.0, 0.0)
        pos (1.0, 0.0)
        offset (735, 178)
        idle "frame 1"
        hover "frame 1"

    imagebutton:
        anchor (0.0, 0.0)
        pos (1.0, 0.0)
        offset (1399, 178)
        idle "frame 1"
        hover "frame 1"

    imagebutton:
        anchor (0.0, 0.0)
        pos (1.0, 0.0)
        offset (127, 700)
        idle "stand"
        hover "stand"

    imagebutton:
        anchor (0.0, 0.0)
        pos (1.0, 0.0)
        offset (793, 700)
        idle "stand"
        hover "stand"

    imagebutton:
        anchor (0.0, 0.0)
        pos (1.0, 0.0)
        offset (1460, 700)
        idle "stand"
        hover "stand"

    imagebutton:
        idle "door frame"
        hover "door frame"
        anchor (0.5, 1.0)
        pos (0.2, 915)
        clicked Event("f2r1_door_frame_clicked")

    use obj_screen(current, {"Door A": {"index": 0, "anchor": (0.5, 1.0), "pos": (0.2,  915), "yoffset": -2, "xoffset": -1},})
    #各objectを部屋として読み込む
    use obj_screen_pos_obj(read_room("loadfile2/room1/object A"), pos=(1.0, 0.0), offset=(222, 700))
    use obj_screen_pos_obj(read_room("loadfile2/room1/object B"), pos=(1.0, 0.0), offset=(884, 700))
    use obj_screen_pos_obj(read_room("loadfile2/room1/object C"), pos=(1.0, 0.0), offset=(1560, 700))

    if exist_box:
        imagebutton:
            anchor (0.5, 1.0)
            pos (1.5, 1.0)
            idle "box"
            hover "box"
