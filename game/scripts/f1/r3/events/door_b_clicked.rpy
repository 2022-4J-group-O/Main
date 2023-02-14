default f1r3_jumped_door_b_jpeg_clicked = False

label f1r3_door_b_jpeg_clicked:
    if not f1r3_jumped_door_b_jpeg_clicked:
        show girl smile at right with dissolve

        g "無事に、ドアを見つけられたね"

        show girl look away at right with dissolve

        g "謎解きはちょっと難しかったかな？"

        show girl at right with dissolve

        g "次の部屋はどうなっているだろう"

        show girl smile at right with dissolve

        g "今から楽しみね"

        hide girl with dissolve

    play sound se_door_open

    $ event_end("f1r4")