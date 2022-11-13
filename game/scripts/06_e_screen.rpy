screen e06(current):
    draggroup:
        for item in current:
            if item == 'Start':
                drag:
                    drag_name "Start"
                    idle_child "Start_idle.png"
                    hover_child "Start_hover.png"
                    xpos 0.2
                    ypos 0
                    draggable False
                    droppable False
                    clicked Call("say_about", calllabel="e06_clicked_start",jumplabel="d07")