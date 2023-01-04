label f1r2_vase_clicked:

    if not f1r2_hidden_clicked:  # 初めてVase or Chestに触れた
        $ f1r2_hidden_clicked = True

        call f1r2_ev_hidden_clicked
        
    else:
        show girl with dissolve

        girl "この家具、あのロボットには見えていないみたい"

        girl "何か理由があるのかな"

        hide girl
    
    $ event_end("f1r2")