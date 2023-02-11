default f2r1_jumped_door_c_clicked = False

label f2r1_door_a_clicked:

    if not f2r1_jumped_door_c_clicked:
        $ f2r1_jumped_door_c_clicked = True

        show girl at right with dissolve

        g "もう次の部屋に行くの？"

        g "的なセリフ"

        hide girl with dissolve

    $ event_end("f2r2")

label f2r1_door_frame_clicked:

    show girl at right with dissolve

    g "ここにドアをはめられそうだね"

    hide girl with dissolve

    $ event_end(loop_label())