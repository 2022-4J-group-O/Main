label f1r1_door_a_clicked:
    $ renpy.dynamic(current=read_room())

    # クリア条件が満たされているとき
    if {"Table", "Sofa"}.isdisjoint(set(current)):
        show girl at right with dissolve

        g "整理整頓お疲れ様"

        show girl smile at right with dissolve
        
        g "家具ごと消し去っちゃうなんて、君の整理術もなかなかアクロバティックだね"

        g "この部屋を荒らした人も、君も、中庸ってやつを知らないのかな"

        show girl at right with dissolve

        g "とにかく、これでまだ先へ進めるね"

        g "もしかしたらこの先で、この部屋を荒らした犯人と出会えるかも"

        g "整理整頓に関して極端な思想を持つ者同士、仲良くできるかもよ？"

        hide girl with dissolve

        hide screen f1r1_screen

        $ event_end("f1r2")  # f1r2へ
    
    else:
        show girl at right with dissolve

        g "このドアの向こうに行きたいけど......"

        g "家具が邪魔だね"

        hide girl with dissolve
        
        $ event_end()
