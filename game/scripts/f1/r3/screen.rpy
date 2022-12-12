screen f1r3_screen(current):
    draggroup:
        for item in current:
            if item == 'Fridge 1':
                drag:
                    drag_name "Fridge 1"
                    child "Fridge.png"
                    xpos 0.2
                    xoffset 0
                    ypos 0.7
                    yoffset 50
                    draggable False
                    droppable False
            elif item == 'Fridge 2':
                drag:
                    drag_name "Fridge 2"
                    child "Fridge.png"
                    xpos 0.2
                    xoffset 50
                    ypos 0.7
                    yoffset 50
                    draggable False
                    droppable False
            elif item == 'Fridge 3':
                drag:
                    drag_name "Fridge 3"
                    child "Fridge.png"
                    xpos 0.2
                    xoffset 100
                    ypos 0.7
                    yoffset 50
                    draggable False
                    droppable False
            
            elif item == 'Fridge 4':
                drag:
                    drag_name "Fridge 4"
                    child "Fridge.png"
                    xpos 0.2
                    xoffset 150
                    ypos 0.7
                    yoffset 50
                    draggable False
                    droppable False
            elif item == 'DoorA':
                drag:
                    drag_name "DoorA"
                    child "door_idle.png"
                    xpos 0.2
                    ypos 0.8
                    yoffset 15
                    draggable False
                    droppable False
            elif item =='Box':
                drag:
                    drag_name "Box"
                    child "box.png"
                    xpos 0.5
                    ypos 0.7
                    draggable False
                    droppable False
