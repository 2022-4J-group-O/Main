define ldissolve = Dissolve(1.0)
default f1r1_evflg_opening = True  # f1r1初回起動時のイベントのフラグ
default f1r1_jumplabel = None  # この変数にラベル名を入れるとそこへジャンプする

label f1r1:
    $ move_room("loadfile1/room1")
    scene bg f1r1

label .scloop:
    show screen f1r1_screen(read_room()) with dissolve

    if f1r1_evflg_opening:  # f1r1初回起動時
        $ f1r1_evflg_opening = False
        call say_about("f1r1_ev_opening", "f1r1.scloop")
    
    if f1r1_jumplabel == "f1r2":
        $ f1r1_jumplabel = None
        jump f1r2
    
    pause
    
    jump .scloop
