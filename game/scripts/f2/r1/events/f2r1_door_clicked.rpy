default f2r1_jumped_door_c_clicked = False

label f2r1_door_c_clicked:

    if not f2r1_jumped_door_c_clicked:
        $ f2r1_jumped_door_c_clicked = True

        show girl with dissolve

        g "あれ、開いてる"

        g "的なセリフ"

        hide girl with dissolve

    $ event_end("f2r2")