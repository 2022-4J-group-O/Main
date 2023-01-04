default f1r2_evflg_opening = True
default f1r2_evflg_angry = False
default nhidden = []
default f1r2_hidden_clicked = False  # VaseまたはChestがクリックされたか

label f1r2:
    $ move_room("loadfile1/room2")
    # 応急処置的な処理。部屋のディレクトリ生成時に実行するべき
    $ give_hidden("loadfile1/room2", "Vase")
    $ give_hidden("loadfile1/room2", "Chest")
    scene bg f1r2

label .scloop:
    window hide
    show screen f1r2_screen(read_room()) with dissolve

    $ nhidden = not_hidden()
    $ f1r2_evflg_angry = len(nhidden) > 0
    

    if f1r2_evflg_opening:

        $ f1r2_evflg_opening = False

        $ Event("f1r2_ev_opening")()

    if f1r2_evflg_angry:
        $ Event("f1r2_ev_angry")()
    
    pause

    jump .scloop
