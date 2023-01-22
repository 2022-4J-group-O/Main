screen f2r1_screen(current):
    layer "master"
    #固定表示のやつ

    imagebutton:
        xanchor 0.0
        yanchor 0.0
        xpos 68
        ypos 178
        idle "f2r1/frame_A.png"
        hover "f2r1/frame_A.png"

    imagebutton:
        xanchor 0.0
        yanchor 0.0
        xpos 735
        ypos 178
        idle "f2r1/frame_B.png"
        hover "f2r1/frame_B.png"

    imagebutton:
        xanchor 0.0
        yanchor 0.0
        xpos 1399
        ypos 178
        idle "f2r1/frame_C.png"
        hover "f2r1/frame_C.png"

    imagebutton:
        xanchor 0.0
        yanchor 0.0
        xpos 82
        ypos 194   
        idle "f2r1/pic_A.png"
        hover "f2r1/pic_A.png"

    imagebutton:
        xanchor 0.0
        yanchor 0.0
        xpos 747
        ypos 194    
        idle "f2r1/pic_B.png"
        hover "f2r1/pic_B.png"

    imagebutton:
        xanchor 0.0
        yanchor 0.0
        xpos 1412
        ypos 195    
        idle "f2r1/error.png"
        hover "f2r1/error.png"

    imagebutton:
        xanchor 0.0
        yanchor 0.0
        xpos 127
        ypos 700   
        idle "f2r1/stand_C.png"
        hover "f2r1/stand_C.png"

    imagebutton:
        xanchor 0.0
        yanchor 0.0
        xpos 793
        ypos 700  
        idle "f2r1/stand_B.png"
        hover "f2r1/stand_B.png"

    imagebutton:
        xanchor 0.0
        yanchor 0.0
        xpos 1460
        ypos 700 
        idle "f2r1/stand_A.png"
        hover "f2r1/stand_A.png"




    use obj_screen(current)
    #各objectを部屋として読み込む
    use obj_screen_pos_obj(read_room("loadfile2/room1/objectA"),222,700)
    use obj_screen_pos_obj(read_room("loadfile2/room1/objectB"),884,700)
    use obj_screen_pos_obj(read_room("loadfile2/room1/objectC"),1560,700)

    if f2r1_exist_flag:
        imagebutton:
            xanchor 0.5
            yanchor 1.0
            xpos 0.5
            ypos 1.0
            idle "f2r1/box.png"
            hover "f2r1/box.png"
