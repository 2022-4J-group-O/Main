define count_box_clicked = 0  # このラベルの訪問回数

label box_clicked:
    $ count_box_clicked += 1 

    if count_box_clicked == 1:  # このラベルを初めて訪れた時

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
    
        $ event_end()
        
    if count_box_clicked == 2:  # 訪問回数が2回のとき

        show girl at right with dissolve

        g "閉じた箱の画像が表示されてるってことは、開いた箱の画像もどこかに用意されてる......ってことだよね"

        g "どこかに画像ファイルはないかな"

        hide girl with dissolve

        $ event_end()
    
    if count_box_clicked == 3:  # 訪問回数が3回のとき

        show girl at right with dissolve

        g "この箱の中身が描かれた画像......"

        g "もしかしたら、それは巧妙に隠されているのかも"

        g "そして、それは案外君の近くに......"

        show girl smile at right with dissolve

        g "なんてね"

        hide girl with dissolve

        $ event_end()
    
    if count_box_clicked >= 4:  # 訪問回数が4回以上のとき

        show girl at right with dissolve

        g "君さ、ファイル拡張子ってどんなものか知ってる？"

        g "ファイル拡張子って、「.png」とか「.txt」みたいに、ファイルの末尾にくっついている文字列のことなんだけど......"
        
        g "これって、ファイルの種類をわかりやすくするためにくっつけてるだけなんだよね"

        g "だから、「.png」がくっついているファイルを画像だと思って実行したら、実はそれが実行ファイルでマルウェアに感染！"

        g "......なんてこともあるみたい"

        show girl smile at right with dissolve

        g "君がただの何でもないファイルだと思っているものも、実は画像ファイルだったりするかもしれないよ？"

        hide girl with dissolve

        $ event_end()
    
