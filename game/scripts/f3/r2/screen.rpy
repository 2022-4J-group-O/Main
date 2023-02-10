# visible: Trueなら、ロボットを表示する
# smile: Trueなら、ロボットの表情を笑顔にする
screen f3r2_screen(current, visible=True, smile=False):
    layer "master"

    if visible:
        if smile:
            drag:
                drag_name "robot2 smile"
                if renpy.can_show("robot2 smile"):
                    add "robot2 smile"
                else:
                    add SampleImage("robot2 smile", 150, 150, "#FF0000")
                draggable False
                droppable False
                anchor (0.0, 0.0)
                pos (537, 79)
        else:
            drag:
                drag_name "robot2"
                if renpy.can_show("robot2"):
                    add "robot2"
                else:
                    add SampleImage("robot2", 150, 150, "#FF0000")
                draggable False
                droppable False
                anchor (0.0, 0.0)
                pos (553, 83)

    use obj_screen(current)