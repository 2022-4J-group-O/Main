screen title_screen(current):
    layer "master"
    draggroup:
        for item in current:
            if item == 'Start':
                drag:
                    drag_name "Start"
                    idle_child "Start_idle.png"
                    hover_child "Start_hover.png"
                    xpos 0.5
                    xanchor 0.5
                    ypos 0.5
                    yanchor 0.5
                    draggable False
                    droppable False
                    clicked FromSc("title_ev_start_clicked", "menu_start")
