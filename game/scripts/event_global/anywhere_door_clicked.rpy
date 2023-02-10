default jumped_anywhere_door_clicked = False  # このラベルへ訪問済みか

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
                    # このラベルを初めて訪れて、かつジャンプ先がf3r2でない時
                    if not jumped_anywhere_door_clicked and dest != "loadfile3/room2":
                        $ jumped_anywhere_door_clicked = True  # ラベルを訪問済みに
                        jump .first  # ジャンプ先でこのイベントは終了
                    if renpy.get_screen(prev_pref + "_screen") != None:
                        $ renpy.hide_screen(prev_pref + "_screen")
                    $ event_end(room_prefix)
                else:
                    $ move_room(cur_room)
    $ event_end(loop_label())

label .first:
    show girl at right with dissolve

    g "この......ドア？明らかに今までのものと雰囲気が違うよね"

    g "いったいどこにつながってるんだろう"

    g "百聞は一見にしかず。兵ははるか？......にして......なんとか......"

    show girl look away at right with dissolve

    g "だからね"

    show girl smile at right with dissolve

    g "それじゃ、行ってみよう"

    hide girl with dissolve

    if renpy.get_screen(prev_pref + "_screen") != None:
        $ renpy.hide_screen(prev_pref + "_screen")

    $ renpy.show_screen(room_prefix + "_screen", current=read_room())

    show girl surprise at right with dissolve

    g "......あれ？"

    g "ここは......前にも見たことがあるよね"

    show girl at right with dissolve

    g "ドアをくぐったと思ったら、いきなりここに出てきた......"

    g "まるでどこでもd......"

    show girl look away at right with dissolve

    g "えっと、まるで......瞬間移動してきたみたい......だね？"

    show girl at right with dissolve

    g "やっぱりあのドア、普通のドアじゃないみたいだね"

    g "今はここに移動してきたみたいだけど......"

    g "行先を変えることはできるのかな？"

    show girl smile at right with dissolve

    g "もし行先を変えることができたら、あの子の入浴シーンも見れるかも？"

    show girl at right with dissolve

    g "......なんてね"

    $ renpy.hide_screen(room_prefix + "_screen")

    $ event_end(room_prefix)
