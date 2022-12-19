screen f1r2_screen(current, rob=True):
    layer "master"
    use obj_screen(current)
    if rob:
        draggroup:
            drag:
                drag_name "Robot"
                add SampleImage("Robot", 200, 500, "#000000", xcenter=0.5, ycenter=0.5)
                draggable False
                droppable False
                clicked Event("f1r2_ev_robot_clicked")

