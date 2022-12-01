screen title_screen(current):
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
                    clicked Call("say_about", calllabel="title_start_clicked",jumplabel="menu_start")

# スタートボタンがクリックされたときの処理
label title_start_clicked:
    hide screen title_screen
    return 