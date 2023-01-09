screen menu2_screen(enable):
    layer "master"
    grid 4 2:
        xcenter 0.5
        ycenter 0.5
        spacing 30
        imagebutton:
            auto "menu/256x192_%s.png"
            sensitive enable
            action Event("menu2_ev_l1_clicked") # ロードファイル1
        imagebutton:
            auto "menu/256x192_%s.png"
            sensitive enable
            action Event("menu2_ev_l2_clicked") # ロードファイル2
        imagebutton:
            auto "menu/256x192_%s.png"
            sensitive enable
            action Event("menu2_ev_l3_clicked") # ロードファイル3
        for i in range(0, 5):
            add "menu/256x192_idle"