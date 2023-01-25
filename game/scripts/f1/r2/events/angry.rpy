# 隠しファイルでないオブジェクトが見つかったとき
default f1r2_jumped_ev_angry = False  # このラベルに訪問済みか

label f1r2_ev_angry:
    hide screen f1r2_screen
    show screen f1r2_screen(read_room(), rob=False) with dissolve

    show robot1 angry at left with dissolve

    ro1 "この部屋に、"

    ro1 "無駄ながらくたを、"

    ro1 "持ち込むなー！！！！"

    $ move_obj(nhidden)
    show screen f1r2_screen(read_room(), rob=False)
    with dissolve

    # このラベルを初めて訪れた時
    if not f1r2_jumped_ev_angry:
        $ f1r2_jumped_ev_angry = True

        show girl surprise at right with dissolve

        g "ちょっと？なにやってるの！？"

        ro1 "さっきも言っただろう。この部屋に不純物はいらないのだ"

        show girl at right with dissolve

        g "少しくらいいいじゃない......"

        ro1 "がらくたはひとつ前の部屋へ放っておいたからな"

        ro1 "二度と私の手を煩わせるなよ、このポンコツめ！"
    
    else:
        show girl look away at right with dissolve
        
        g "そんなにかっかしないでよ。何とかロボット君"

        ro1 "がらくたはひとつ前の部屋へ放っておいたからな"
    
    hide girl with dissolve

    hide robot1 angry with dissolve

    hide screen f1r2_screen

    $ event_end("f1r2.scloop")