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

    use obj_screen(current)
