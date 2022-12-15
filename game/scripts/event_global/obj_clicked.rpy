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
