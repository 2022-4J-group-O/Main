# この部屋のプロパティ
define f1r2_obj_prop = {
    "Door": {"anchor": (0.0, 0.0), "pos": (1404, 179)},
}

screen f1r2_screen(current, rob=True):
    layer "master"

    drag:
        drag_name "DoorFrameType2"
        if renpy.can_show("door frame type2"):
            add "door frame type2"
        else:
            add SampleImage("DoorFrameType2", 150, 150, "#FF0000")
        draggable False
        droppable False
        anchor (0.0, 0.0)
        pos (1380, 150)

    use obj_screen(current, f1r2_obj_prop)

    if rob:
        draggroup:
            drag:
                drag_name "Robot"
                if renpy.can_show("robot"):
                    add "robot"
                else:
                    add SampleImage("robot", 150, 150, "#FF0000")
                draggable False
                droppable False
                clicked Event("f1r2_ev_robot_clicked")
                pos (671, 601)
    else:
        draggroup:
            drag:
                drag_name "Robot Angry"
                if renpy.can_show("robot angry"):
                    add "robot angry"
                else:
                    add SampleImage("robot angry", 150, 150, "#FF0000")
                draggable False
                droppable False
                pos (673, 597)
