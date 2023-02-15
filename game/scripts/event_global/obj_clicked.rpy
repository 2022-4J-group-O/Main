label obj_clicked(objname):
    if check_obj(objname):
        $ renpy.dynamic(lb=objname.lower().replace(" ", "_").replace(".", "_") + "_clicked")
        $ renpy.dynamic(pref_lb=room_prefix + "_" + lb)
        if renpy.has_label(pref_lb):
            jump expression pref_lb
        elif renpy.has_label(lb):
            jump expression lb
        $ event_end()
    # ごり押し
    if objname in ["Apple", "Dog", "Cup"]:
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
    g "これ、冷蔵庫から出てきたのかな"
    show girl look away at right with dissolve
    g "冷蔵庫に封筒って......ますますよくわからくなってきたね"
    show girl at right with dissolve
    g "開封してみようよ"
    g "何が入っているのかな"
    hide girl with dissolve
    $ event_end(loop_label())

label document_docx_clicked:
    show girl look away at right with dissolve
    g "今度は、封筒から封筒が出てきたね"
    show girl at right with dissolve
    g "この封筒、冷蔵庫で冷やされていたわけだからきっと凍り付いてるよね"
    show girl smile at right with dissolve
    g "......ってことは、「解凍」が必要なんじゃないかな"
    show girl at right with dissolve
    g "......なんてね"
    hide girl with dissolve
    $ event_end(loop_label())

label document_zip_clicked:
    show girl at right with dissolve
    jump document_docx_clicked

label config_clicked:
    python:

        ShowMenu("preferences")() # 設定画面を呼び出す

        event_end()
