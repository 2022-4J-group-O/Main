# ロボットをクリックしたとき
default f1r2_jumped_robot_clicked = False

label f1r2_ev_robot_clicked:
    show screen f1r2_screen(read_room(), visible=False)  # ロボットを不可視に
    show robot1 at left with dissolve
    show girl at right with dissolve

    if not f1r2_jumped_robot_clicked:
        $ f1r2_jumped_robot_clicked = True
        
        ro1 "む、まだいたのかね、君たち"

        g "いいじゃない、私たちの勝手でしょ"

        ro1 "この部屋いるのは良いが、くれぐれも部屋を汚すなよ"

        g "わかったよ"

        ro1 "しかし、今日は珍しいことばかり起こる"

        ro1 "久しぶりにゲームが起動されたと思ったら、知らぬ客人が来た"

        ro1 "画面の向こうの者も、どうも私の知っている人物ではないようだし......"

        ro1 "いったい何が起こっているんだ"

        ro1 "このゲームが日の目を見るなど、ありえないはずなのに......"

        hide robot1
        hide girl with dissolve

        show screen f1r2_screen(read_room(), visible=True)  # ロボットを不可視に

        show girl look away with dissolve

        g "このロボット、一人でごちゃごちゃしゃべるのが好きみたいだね......"

        g "彼のことはほっといて、次の部屋へ進む方法を考えましょう"

        hide girl with dissolve

    else:
        show girl at right with dissolve
        show robot1 at left with dissolve

        ro1 "む、まだいたのかね、君たち"

        g "いいじゃない、私たちの勝手でしょ"

        ro1 "くれぐれも私の部屋を汚すでないぞ"

        hide girl with dissolve
        hide robot1

    $ event_end("f1r2.scloop")
