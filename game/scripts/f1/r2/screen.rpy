screen f1r2_screen(current, rob=True):
    $ img_col = ["#FF0000", "#808000", "#00FF00", "#008080", "#0000FF", "#800080"]
    draggroup:
        for i, item in enumerate(current):
            drag:
                drag_name item
                if renpy.can_show(item.lower()):
                    add item.lower()
                else:
                    add SampleImage(item, 150, 150, img_col[i % 6])
                draggable False
                droppable False
                properties default_obj_prop[item]
        if rob:
            drag:
                drag_name "Robot"
                add SampleImage("Robot", 200, 500, "#000000", xcenter=0.5, ycenter=0.5)
                draggable False
                droppable False
                clicked FromSc("f1r2_ev_robot_clicked", "f1r2.scloop")

