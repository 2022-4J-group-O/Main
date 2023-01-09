screen f1r1_screen(current):
    layer "master"

    drag:
        drag_name "DoorFrame"
        if renpy.can_show("door frame"):
            add "door frame"
        else:
            add SampleImage("DoorFrame", 150, 150, "#FF0000")
        draggable False
        droppable False
        anchor (0.0, 0.0)
        pos (1019, 120)

    use obj_screen(current)