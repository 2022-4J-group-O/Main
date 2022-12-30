# !TODO
label f2r2_ev_picture_clicked(picture):
    show girl with dissolve

    $ g("題名は" + picture + "らしいよ")

    hide girl with dissolve
    
    $ event_end(loop_label())
