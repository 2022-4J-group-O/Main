screen obj_screen(current, jlabeldict={}):
    layer "master"
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
                if item in jlabeldict:
                    clicked FromSc("obj_clicked", jlabeldict[item], objname=item)
                else:
                    clicked FromSc("obj_clicked", room_prefix + ".scloop", objname=item)
                properties default_obj_prop[item]