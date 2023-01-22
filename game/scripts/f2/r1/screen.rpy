screen f2r1_screen(current):
    layer "master"
    #固定表示のやつ

    fixed:
        add "bg f2r1"
        xpos 1.0

    imagebutton:
        anchor (0.0, 0.0)
        pos (1.0, 0.0)
        offset (68, 178)
        idle "frame_a"
        hover "frame_a"

    imagebutton:
        anchor (0.0, 0.0)
        pos (1.0, 0.0)
        offset (735, 178)
        idle "frame_b"
        hover "frame_b"

    imagebutton:
        anchor (0.0, 0.0)
        pos (1.0, 0.0)
        offset (1399, 178)
        idle "frame_c"
        hover "frame_c"

    imagebutton:
        anchor (0.0, 0.0)
        pos (1.0, 0.0)
        offset (82, 194)
        idle "pic_a"
        hover "pic_a"

    imagebutton:
        anchor (0.0, 0.0)
        pos (1.0, 0.0)
        offset (747, 194)
        idle "pic_b"
        hover "pic_b"

    imagebutton:
        anchor (0.0, 0.0)
        pos (1.0, 0.0)
        offset (1412, 195)
        idle "error"
        hover "error"

    imagebutton:
        anchor (0.0, 0.0)
        pos (1.0, 0.0)
        offset (127, 700)
        idle "stand_c"
        hover "stand_c"

    imagebutton:
        anchor (0.0, 0.0)
        pos (1.0, 0.0)
        offset (793, 700)
        idle "stand_b"
        hover "stand_b"

    imagebutton:
        anchor (0.0, 0.0)
        pos (1.0, 0.0)
        offset (1460, 700)
        idle "stand_a"
        hover "stand_a"




    use obj_screen(current)
    #各objectを部屋として読み込む
    use obj_screen_pos_obj(read_room("loadfile2/room1/objectA"), pos=(1.0, 0.0), offset=(222,700))
    use obj_screen_pos_obj(read_room("loadfile2/room1/objectB"), pos=(1.0, 0.0), offset=(884,700))
    use obj_screen_pos_obj(read_room("loadfile2/room1/objectC"), pos=(1.0, 0.0), offset=(1560,700))

    if f2r1_exist_flag:
        imagebutton:
            anchor (0.5, 1.0)
            pos (1.5, 1.0)
            idle "box"
            hover "box"
