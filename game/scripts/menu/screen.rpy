screen menu_screen(enable):
    grid 4 2:
        xcenter 0.5
        ycenter 0.5
        spacing 30
        imagebutton:
            auto "256x192_%s.png"
            sensitive enable
            action Jump("f1r1") # ロードファイル1
        imagebutton:
            auto "256x192_%s.png"
            sensitive enable
            action NullAction() # ロードファイル2
        imagebutton:
            auto "256x192_%s.png"
            sensitive enable
            action NullAction() # ロードファイル3
        for i in range(0, 5):
            add "256x192_idle"