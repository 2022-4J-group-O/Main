screen backbutton_screen:
    if enable_event and room_prefix in previous_room:
        imagebutton:
            idle "backbutton_idle"
            hover "backbutton_hover"
            # auto "backbutton %s"
            action Event("room_back")
            xcenter 0.5
            yanchor 1.0
            ypos 1.0
            yoffset -20

label room_back:

    $ event_end(previous_room[room_prefix])