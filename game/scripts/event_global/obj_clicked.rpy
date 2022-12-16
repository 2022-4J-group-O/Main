label obj_clicked(objname):
    $ renpy.dynamic(lb=objname.lower() + "_clicked")
    $ renpy.dynamic(pref_lb=room_prefix + "_" + lb)
    if renpy.has_label(pref_lb):
        call expression pref_lb
    elif renpy.has_label(lb):
        call expression lb
    return

label table_clicked:
    show girl with dissolve
    g "机がクリックされたよ"
    hide girl with dissolve
    return

label drawer_clicked:
    show girl with dissolve
    g "引き出しがクリックされたよ"
    hide girl with dissolve
    return

label chair_clicked:
    show girl with dissolve
    g "椅子がクリックされたよ"
    show girl with dissolve
    return

label chest_clicked:
    show girl with dissolve
    g "チェストがクリックされたよ"
    show girl with dissolve
    return

label vase_clicked:
    show girl with dissolve
    g "花瓶がクリックされたよ"
    show girl with dissolve
    return

label box_clicked:
    show girl with dissolve
    g "箱がクリックされたよ"
    show girl with dissolve
    return

