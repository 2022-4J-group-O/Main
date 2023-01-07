define f1r3_jumped_box_clicked = False  # このラベルを訪問済みか

label f1r3_box_clicked:

    if not f1r3_jumped_box_clicked:  # このラベルを初めて訪れた時

        $ f1r3_jumped_box_clicked = True
    
        show girl at right with dissolve

        g "この箱......気になるね"

        g "中には何が入っているのかな"

        "......"

        g "そんなの、私が今すぐこの箱を開けて、中を見てしまえばいい......"

        g "そう思った？"

        show girl smile at right with dissolve

        g "残念だけど、それは私にはできないよ"

        g "さっきも言った通り、私はゲーム内のオブジェクトに触れることができないんだ"

        show girl at right with dissolve

        g "それに......"

        g "君はさ、このゲームにおいて、「箱を開ける」ってどういうことだと思う？"

        g "君や私に見えているのはあくまで、「閉じられた箱」が描かれているだけの、ただの画像データなんだ"

        g "画像データに過ぎない箱を開いて、中身を調べるなんて、そんなことできるわけがない"

        g "描かれた箱の中から子羊を見いだすことができるのは、星の王子様ぐらいだよ"

        show girl smile at right with dissolve

        g "つまり、「中には何が入っているのか」とか、「箱を開けることができるか」とか、そんな問いはナンセンスなんだ"

        show girl at right with dissolve

        g "それでもきっと、「箱を開ける」ことはできるはず......"

        g "そうでないと、ここに閉じた箱がある意味がないからね"

        g "ではどうやって「箱をあける」か......"

        show girl look away at right with dissolve

        g "尊大に語っておいて、私にはさっぱりわからないけど......"

        show girl at right with dissolve
        
        g "それを解決するのは君の仕事だし、それがゲームの醍醐味だよね"

        show girl smile at right with dissolve

        g "というわけで、謎解きは頼んだよ"

        hide girl with dissolve
    
    else:
        
        g "この箱を開けるためには、どうすればいいかな"

        g "「そちら」から見て、この箱に違和感とかはない？"
    
    $ event_end()