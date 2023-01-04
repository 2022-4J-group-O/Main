default f1r2_jumped_door_clicked = False  # このラベルに訪問済みか

label f1r2_door_clicked:
    # このラベルを初めて訪れた時
    if not f1r2_jumped_door_clicked:
        $ f1r2_jumped_door_clicked = True

        show girl smile at right with dissolve

        girl "やった！これで次の部屋に行けるね"

        girl "ばれないようにドアを設置するなんて。まさに完全犯罪だ"

        show girl at right with dissolve

        show robot1 at left with dissolve
        
        robot1 "何を隠れて話しているのだね、君たち"

        robot1 "見ての通り、この部屋はには何もない。君たちの望むものは絶対に見つからないぞ"

        robot1 "それがわかったらそろそろ出て行ってくれないかね"

        girl "わかってるよ。今に出ていくから。安心して"

        girl "部屋を荒らして悪かったね"

        robot1 "やけに素直だな......まあわかればいいのだよ"

        robot1 "......しかし出口はそちらではないぞ"

        girl "いや、あってるよ。私たちはこっちに用があるから"

        robot1 "その、何もない壁に用があるというのかね。また私をからかっているのか？"

        girl "からかってなんかないよ。いつも本気。それじゃあね"

        hide girl

        robot1 "消えた！？"

        robot1 "いったい何が起こっているんだ？理解不能だ！"

        hide robot1

        $ event_end("f1r3")

    else:
        $ event_end("f1r3")