screen menu2_screen(enable):
    layer "master"
    grid 4 2:
        xcenter 0.5
        ycenter 0.5
        spacing 30
        imagebutton:
            auto "256x192_%s.png"
            sensitive enable
            action FromSc("menu2_ev_l1_clicked", "menu2.scloop") # ロードファイル1
        imagebutton:
            auto "256x192_%s.png"
            sensitive enable
            action FromSc("menu2_ev_l2_clicked", "menu2.scloop") # ロードファイル2
        imagebutton:
            auto "256x192_%s.png"
            sensitive enable
            action FromSc("menu2_ev_l3_clicked", "menu2.scloop") # ロードファイル3
        for i in range(0, 5):
            add "256x192_idle"