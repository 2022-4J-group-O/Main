label f1r2_vase_clicked:

    if not f1r2_hidden_clicked:  # 初めてVase or Chestに触れた
        $ f1r2_hidden_clicked = True

        call f1r2_ev_hidden_clicked
        
    else:
        show girl with dissolve

        g "この家具、あのロボットには見えていないみたい"

        g "何か理由があるのかな"

        hide girl with dissolve
    
    $ event_end("f1r2.scloop")