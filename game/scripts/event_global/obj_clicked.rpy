label obj_clicked(objname):
    $ renpy.dynamic(lb=objname.lower().replace(" ", "_") + "_clicked")
    $ renpy.dynamic(pref_lb=room_prefix + "_" + lb)
    if renpy.has_label(pref_lb):
        jump expression pref_lb
    elif renpy.has_label(lb):
        jump expression lb
    $ event_end(loop_label())

label table_clicked:
    show girl at right with dissolve
    g "机がクリックされたよ"
    hide girl with dissolve
    $ event_end(loop_label())

label drawer_clicked:
    show girl at right with dissolve
    g "引き出しがクリックされたよ"
    hide girl with dissolve
    $ event_end(loop_label())

label chair_clicked:
    show girl at right with dissolve
    g "椅子がクリックされたよ"
    hide girl with dissolve
    $ event_end(loop_label())

label chest_clicked:
    show girl at right with dissolve
    g "チェストがクリックされたよ"
    hide girl with dissolve
    $ event_end(loop_label())

label vase_clicked:
    show girl at right with dissolve
    g "花瓶がクリックされたよ"
    hide girl with dissolve
    $ event_end(loop_label())

# label box_clicked: (box_clicked.rpyに定義)

label config_clicked:
    python:

        ShowMenu("preferences")() # 設定画面を呼び出す

        event_end(loop_label())
