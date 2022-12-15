label f1r1_door_clicked:
    $ renpy.dynamic(current=read_room())
    if {"Chair", "Drawer", "Table"}.isdisjoint(set(current)):
        call f1r1_ev_door_clicked
    return

label f1r1_ev_door_clicked:
    show girl

    g "整理整頓お疲れ様"

    show girl smile
    
    g "家具ごと消し去っちゃうなんて、君の整理術もなかなかアクロバティックだね"

    g "この部屋を荒らした人も、君も、中庸ってやつを知らないのかな"

    show girl

    g "とにかく、これでまだ先へ進めるね"

    g "もしかしたらこの先で、この部屋を荒らした犯人と出会えるかも"

    g "整理整頓に関して極端な思想を持つ者同士、仲良くできるかもよ？"

    $ f1r1_jumplabel = "f1r2"  # 次のループでf1r2にループ

    hide girl
    
    return