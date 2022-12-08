screen f1r1_screen(current):
    draggroup:
        if 'Door' in current:
            if 'Table' not in current and 'Drawer' not in current and 'Chair' not in current: 
                drag:
                    drag_name "Door"
                    idle_child "door_idle.png"
                    hover_child "door_hover.png"
                    xpos 0.2
                    ypos 0.8
                    yoffset 15
                    draggable False
                    droppable False
                    clicked FromSc("f1r1_door_clicked", "f1r1.scloop")
            else:
                drag:
                    drag_name "Door"
                    idle_child "door_idle.png"
                    hover_child "door_idle.png"
                    xpos 0.2
                    ypos 0.8
                    yoffset 15
                    draggable False
                    droppable False

        for item in current:
            if item == 'Chair':
                drag:
                    drag_name "Chair"
                    idle_child "chair_idle.png"
                    hover_child "chair_hover.png"
                    xpos 0.2
                    xoffset 10
                    ypos 0.8
                    draggable False
                    droppable False
            elif item=='Drawer':
                drag:
                    drag_name "Drawer"
                    idle_child "drawer_idle.png"
                    hover_child "drawer_hover.png"
                    xpos 0.2
                    ypos 0.8
                    yoffset 10
                    draggable False
                    droppable False
            elif item=='Table':  
                drag:
                    drag_name "Table"
                    idle_child "table_idle.png"
                    hover_child "table_hover.png"
                    xpos 0.1
                    xoffset 150
                    ypos 0.8
                    yoffset 10
                    draggable False
                    droppable False
