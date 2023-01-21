default current_map = 0

init python:
    def get_current_map():
        return current_map
    def can_move_left():
        return room_prefix == "f2r1" and current_map > 0
    
    def can_move_right():
        return room_prefix == "f2r1" and current_map < 1

screen move_map_ui:
    if enable_event and can_move_left():
        imagebutton:
            auto "button_left_%s"
            ycenter 0.5
            xanchor 0.0
            xpos 0.0
            xoffset 20
            action Event("move_map_left")
    if enable_event and can_move_right():
        imagebutton:
            auto "button_right_%s"
            ycenter 0.5
            xanchor 1.0
            xpos 1.0
            xoffset -20
            action Event("move_map_right")

label move_map_left:
    $ current_map -= 1
    camera:
        xpos -float(current_map)
    $ event_end()

label move_map_right:
    $ current_map += 1
    camera:
        xpos -float(current_map)
    $ event_end()