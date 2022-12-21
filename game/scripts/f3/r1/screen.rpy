screen f3r1_screen(current):
    layer "master"
    for item in current:
        if item == 'Door':
            drag:
                drag_name "Door"
                child "door_idle.png"
                xpos 0.2
                ypos 0.8
                yoffset 15
                draggable False
                droppable False
                clicked FromSc("f3r1_jumproom", "f3r1.scloop")
