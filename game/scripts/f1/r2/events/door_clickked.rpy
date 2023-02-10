default f1r2_jumped_door_clicked = False  # このラベルに訪問済みか

label f1r2_door_a_clicked:
    # このラベルを初めて訪れた時
    if not f1r2_jumped_door_clicked:
        $ f1r2_jumped_door_clicked = True

        show girl smile at right with dissolve

        g "やった！これで次の部屋に行けるね"

        g "ばれないようにドアを設置するなんて。まさに完全犯罪だ"

        show screen f1r2_screen(read_room(), visible=False) with dissolve

        show girl at right with dissolve
        show robot1 at left with dissolve
        
        ro1 "何を隠れて話しているのだね、君たち"

        ro1 "見ての通り、この部屋はには何もない。君たちの望むものは絶対に見つからないぞ"

        ro1 "それがわかったらそろそろ出て行ってくれないかね"

        g "わかってるよ。今に出ていくから。安心して"

        g "部屋を荒らして悪かったね"

        ro1 "やけに素直だな......まあわかればいいのだよ"

        ro1 "......しかし出口はそちらではないぞ"

        g "いや、あってるよ。私たちはこっちに用があるから"

        ro1 "その、何もない壁に用があるというのかね。また私をからかっているのか？"

        g "からかってなんかないよ。いつも本気。それじゃあね"

        hide girl with dissolve

        ro1 "消えた！？"

        ro1 "いったい何が起こっているんだ？理解不能だ！"

        hide robot1

        $ event_end("f1r3")

    else:
        $ event_end("f1r3")