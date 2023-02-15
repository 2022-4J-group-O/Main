label f2r2_door_png_clicked:

    play sound se_door_open

    show girl at right with dissolve

    g "やったね！これでまた次の部屋へ進める"

    g "なかなか面白いギミック満載の部屋だったね"

    g "次は、どんな部屋なのかな？"

    hide girl with dissolve

    $ event_end("f2r3")