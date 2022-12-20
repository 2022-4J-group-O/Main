screen f2r1_screen(current):
    layer "master"
    #固定表示のやつ
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.2
        ypos 0.2    
        idle "f2/JPG.jpg"
        hover "f2/JPG.jpg"

    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.2    
        idle "f2/PNG.png"
        hover "f2/PNG.png"
        
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.85
        ypos 0.2    
        idle "f2/error.png"
        hover "f2/error.png"
        
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.2
        ypos 0.75   
        idle "f2/obj1.png"
        hover "f2/obj1.png"

    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.75  
        idle "f2/obj1.png"
        hover "f2/obj1.png"

    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.85
        ypos 0.75 
        idle "f2/obj1.png"
        hover "f2/obj1.png"

    use obj_screen(current)
    #各objectを部屋として読み込む
    use obj_screen_pos_obj(read_room("loadfile2/room1/object1"),0.2,0.5)
    use obj_screen_pos_obj(read_room("loadfile2/room1/object2"),0.5,0.5)
    use obj_screen_pos_obj(read_room("loadfile2/room1/object3"),0.85,0.5)

    
    



