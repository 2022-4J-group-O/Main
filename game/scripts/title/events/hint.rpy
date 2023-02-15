label title_ev_hint:
    show girl at right with dissolve

    $ path = os.path.join(config.basedir, current_room)
    
    g "ところでこの場所は\"[path]\"だよ"

    g "さっき、似たような画面を見たと思うんだけど......"

    g "そこには、スタートボタンが表示されてたと思う"

    g "それを押したから、君は私と出会った"

    g "あのボタン、この画面にも表示できないかな"

    hide girl with dissolve
    
    $ event_end()