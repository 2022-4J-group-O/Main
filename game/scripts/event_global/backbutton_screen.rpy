init python:
    def can_show_backbutton():
        return room_prefix in previous_room and get_current_map() == 0

screen backbutton_screen:
    if enable_event and can_show_backbutton():
        imagebutton:
            auto "backbutton_%s"
            action Event("room_back")
            xcenter 0.5
            yanchor 1.0
            ypos 1.0
            yoffset -20

label room_back:

    if previous_room[room_prefix] != "menu2":
        play sound se_door_open

    $ event_end(previous_room[room_prefix])