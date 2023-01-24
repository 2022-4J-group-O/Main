screen f1r3_screen(current):
    layer "master"

    drag:
        drag_name "DoorFrameType2"
        if renpy.can_show("door frame type3"):
            add "door frame type3"
        else:
            add SampleImage("DoorFrameType3", 150, 150, "#FF0000")
        draggable False
        droppable False
        anchor (0.0, 0.0)
        pos (1527, 91)
        clicked Event("clicked_DoorFrameType3")

    use obj_screen(current)

label clicked_DoorFrameType3:
    show girl at right with dissolve
    
    g "このドア枠......さっきのロボットの部屋にもあったよね"

    g "ここにもきっと、ドアをはめることができるはずだよ"

    show girl smile at right with dissolve

    g "ドアを開けるっていうより、ドアを見つけて持ってこないといけないのは、ちょっと変だね"

    hide girl with dissolve

    $ event_end()
