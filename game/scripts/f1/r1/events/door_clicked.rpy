label f1r1_door_clicked:
    $ renpy.dynamic(current=read_room())

    # クリア条件が満たされているとき
    if {"Chair", "Drawer", "Table"}.isdisjoint(set(current)):
        show girl with dissolve

        g "整理整頓お疲れ様"

        show girl smile
        
        g "家具ごと消し去っちゃうなんて、君の整理術もなかなかアクロバティックだね"

        g "この部屋を荒らした人も、君も、中庸ってやつを知らないのかな"

        show girl

        g "とにかく、これでまだ先へ進めるね"

        g "もしかしたらこの先で、この部屋を荒らした犯人と出会えるかも"

        g "整理整頓に関して極端な思想を持つ者同士、仲良くできるかもよ？"

        hide girl

        $ event_end("f1r2")  # f1r2へ
    
    else:
        show girl with dissolve

        g "このドアの向こうに行きたいけど......"

        g "家具が邪魔だね"

        hide girl
        
        $ event_end()
