label anywhere_door_clicked:
    $ renpy.dynamic(pathd=os.path.join(user_dir_path, current_room, "Anywhere Door Destination.txt"))
    if os.path.isfile(pathd):
        $ renpy.dynamic(inside=dumpfile(pathd))
        if inside != None:
            $ renpy.dynamic(dest=os.path.normpath(os.path.join(current_room, inside)))
            if os.path.isdir(os.path.join(user_dir_path, dest)):
                $ renpy.dynamic(cur_room=current_room, prev_pref=room_prefix)
                $ move_room(dest)
                if renpy.has_label(room_prefix):
                    if renpy.get_screen(prev_pref + "_screen") != None:
                        $ renpy.hide_screen(prev_pref + "_screen")
                    $ event_end(room_prefix)
                else:
                    $ move_room(cur_room)
    $ event_end(loop_label())