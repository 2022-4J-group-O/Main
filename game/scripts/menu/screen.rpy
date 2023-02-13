screen menu2_screen(enable):
    layer "master"
    grid 3 1:
        spacing 100
        xcenter 0.5
        ycenter 0.5
        frame:
            vbox:
                text "File1" size 30
                imagebutton:
                    auto "file1_%s"
                    sensitive enable
                    action Event("menu2_ev_l1_clicked") # ロードファイル1
        frame:
            vbox:
                text "File2" size 30
                imagebutton:
                    auto "file2_%s"
                    sensitive enable
                    action Event("menu2_ev_l2_clicked") # ロードファイル2
        frame:
            vbox:
                text "File3" size 30
                imagebutton:
                    auto "file3_%s"
                    sensitive enable
                    action Event("menu2_ev_l3_clicked") # ロードファイル3