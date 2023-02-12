label f3r2_ev_opening:
    show girl surprise at right with dissolve

    g "......あれ？"

    g "ここは、まだ見たことがない場所だね"

    g "あのどこでもd......瞬間移動するやつで、新しい場所に進めたんだね"

    g "君があのドアの行先をうまく調整してくれたのかな？"

    show girl smile at right with dissolve

    g "とにかく、これで先に進めるね"

    show girl look away at right with dissolve
    
    g "......と、ここにもロボットがいるのね"

    g "今度は拒まれないといいけど......"

    g "こんにちは"

    show screen f3r2_screen(read_room(), visible=False)

    show girl at right with dissolve
    show robot2 at left with dissolve

    ro2_unknown "こんにちは"

    ro2_unknown "久しぶりの客人ですね、うれしいです"

    ro2 "私の名前はcXVpeg==です"

    ro2 "名前は覚えにくいでしょうし、スーパークレバークイズロボット君とお呼びください"

    show girl look away at right with dissolve

    g "スーパークレバーって......cXなんとかよりはましだけど......"

    show girl at right with dissolve

    ro2 "私の製作者が、私をそう呼んでいたものですから......"

    ro2 "呼びやすい名前で、好きによんでいただいて構いませんよ"

    ro2 "ところで、名前の通り私は聡明なクイズロボットです"

    g "\"聡明な\"、ね"

    ro2 "よければ、私のクイズに付き合っていただけませんか？"

    g "クイズね......わかったよ"

    g "画面の向こうの君も、いいでしょ？"

    show girl smile at right with dissolve

    g "ここまで華麗に謎を解いてきた、君の聡明なところ、ロボットさんにみせてやりなよ"

    show robot2 smile at left with dissolve
    
    ro2 "その息です。では、クイズを出題しますね"

    show girl at right with dissolve

    g "かかってきなさい、解くのは私じゃないけど"

    show robot2 at left with dissolve

    ro2 "このゲームの製作者は、twitterのアカウントを持っています"

    ro2 "このアカウントのidを特定してください"

    show girl look away at right with dissolve

    g "twitterアカウント......誠実そうな言葉遣いで、なかなか趣味が悪いね"

    ro2 "ご安心ください。私を作ったのは、このゲームの製作者です"

    ro2 "もちろん、問題の製作も彼が行いました"

    ro2 "彼はアカウントが特定されることを前提としているのです"

    g "まあ確かに......"

    g "あの人も、思い切った問題を作るなぁ......"

    ro2 "回答は、この部屋に置かれたテキストファイルに入力してくださいね"

    ro2 "答えを入力したら、私に話しかけてください"

    ro2 "正誤を判定しますから"

    show robot2 smile at left with dissolve

    ro2 "それでは、ごゆっくり"

    hide robot2 with dissolve

    show screen f3r2_screen(read_room(), visible=True)
    
    hide girl with dissolve
    show girl with dissolve

    g "製作者のtwitterアカウント......"

    g "どうやったら特定できるのかさっぱりだけど......"

    show girl smile with dissolve

    g "君ならやってくれると信じてるよ"

    g "よろしくね"

    hide girl with dissolve

    $ event_end()
