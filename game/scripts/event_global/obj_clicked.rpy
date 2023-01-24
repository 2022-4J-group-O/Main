label obj_clicked(objname):
    if check_obj(objname):
        $ renpy.dynamic(lb=objname.lower().replace(" ", "_").replace(".", "_") + "_clicked")
        $ renpy.dynamic(pref_lb=room_prefix + "_" + lb)
        if renpy.has_label(pref_lb):
            jump expression pref_lb
        elif renpy.has_label(lb):
            jump expression lb
    $ event_end()

label table_clicked:
    show girl at right with dissolve
    g "机がクリックされたよ"
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

label archive_tar_gz_clicked:
    show girl at right with dissolve
    g "封筒だね"
    show girl look away at right with dissolve
    g "これ、冷蔵庫から出てきたのかな"
    hide girl with dissolve
    $ event_end(loop_label())

label document_docx_clicked:
    show girl at right with dissolve
    g "封筒だね"
    show girl look away at right with dissolve
    g "これ、冷蔵庫から出てきたのかな"
    g "これも中身を見れるかな"
    g "もしかしたら、いままでの冷蔵庫と同じ方法で中身を確認出来たり？"
    hide girl with dissolve
    $ event_end(loop_label())

label document_zip_clicked:
    show girl at right with dissolve
    g "封筒だね"
    show girl look away at right with dissolve
    g "これ、冷蔵庫から出てきたのかな"
    g "これも中身を見れるかな"
    g "もしかしたら、いままでの冷蔵庫と同じ方法で中身を確認出来たり？"
    hide girl with dissolve
    $ event_end(loop_label())

label config_clicked:
    python:

        ShowMenu("preferences")() # 設定画面を呼び出す

        event_end()
