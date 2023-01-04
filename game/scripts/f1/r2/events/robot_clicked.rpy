# ロボットをクリックしたとき
default f1r2_jumped_robot_clicked = False

label f1r2_ev_robot_clicked:
    show screen f1r2_screen(read_room(), False)  # ロボットを不可視に
    show robot1 at right with dissolve
    show girl at right with dissolve

    if not f1r2_jumped_robot_clicked:
        ro1 "む、まだいたのかね、君たち"

        girl "いいじゃない、私たちの勝手でしょ"

        ro1 "この部屋いるのは良いが、くれぐれも部屋を汚すなよ"

        girl "わかったよ"

        ro1 "しかし、今日は珍しいことばかり起こる"

        ro1 "久しぶりにゲームが起動されたと思ったら、知らぬ客人が来た"

        ro1 "画面の向こうの者も、どうも私の知っている人物ではないようだし......"

        ro1 "いったい何が起こっているんだ"

        ro1 "このゲームが日の目を見るなど、ありえないはずなのに......"

        hide robot1
        hide girl

        show girl look away with dissolve

        girl "このロボット、一人でごちゃごちゃしゃべるのが好きみたいだね......"

        girl "彼のことはほっといて、次の部屋へ進む方法を考えましょう"

    else:
        ro1 "む、まだいたのかね、君たち"

        girl "いいじゃない、私たちの勝手でしょ"

        ro1 "くれぐれも私の部屋を汚すでないぞ"

    window hide
    $ event_end("f1r2.scloop")
