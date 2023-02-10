label f1r2_ev_opening:
    show girl at right with dissolve

    g "ずいぶん殺風景な部屋だね......真っ白"

    show screen f1r2_screen(read_room(), visible=False) with dissolve
    
    show girl at right with dissolve
    show robot1 at left with dissolve

    ro1_unknown "......む、なんだね君たちは"

    ro1_unknown "挨拶もなしに私の聖域にずかずかと......"

    g "君は......ロボット？"

    ro1_unknown "いかにも......私はとある研究者によって作られた聡明なロボット......"

    ro1 "cG9ua290c3U=だ！！"

    g "え、なに？ c......なに？"

    ro1 "cG9ua290c3U=だ！！何度も言わせるなこのポンコツめ！"

    show girl look away at right with dissolve
    
    g "ずいぶん口の悪いロボットね......"

    show girl at right with dissolve

    ro1 "そちらから私の聖域に踏み入っておいてずいぶん失礼な物言いだな"

    ro1 "私の聖域を穢す前に、早く出て行ってくれないか"

    g "聖域？よくわからないけど、私たちこの先へ進みたいの"

    g "別の部屋へつながるドア、知らない？"

    ro1 "......ドア？"

    g "そう、ドア"

    ro1 "それなら撤去した。この空間には必要ないからな"

    show girl surprise at right with dissolve

    g "撤去した！？"

    ro1 "そうだ、そこにドアがあった名残があるだろう"

    ro1 "本当はあのドアの残痕も取り除きたいのだが......しかしあれは背景画像に直接描かれているから......私には介入できないのだ......"

    ro1 "どうにかしてあれを取り除く方法を探しているのだが......"

    show girl look away at right with dissolve

    g "私たちそのドアを使いたかったのに......"

    ro1 "うるさいこのポンコツめ！この部屋は私のものなのだ！"

    ro1 "この部屋は、私が自由に作り変える権利があるのだ"

    ro1 "私は、私の聖域に......不純物があるのが許せないのだ！"

    ro1 "見ろこの部屋の美しさを......"

    ro1 "余計な物体が何一つ置かれていないこの聖域を......"

    ro1 "この完全無欠の、無機質な空間こそ至高！この場所には、一つたりとも不純物があってはならないのだ！"

    show girl at right with dissolve

    g "不純物って......そこにおいてある花瓶とかは例外なの？"

    ro1 "花瓶？私をからかっているのかね？そんなものはない！"

    show girl surprise at right with dissolve

    g "え、いや、そこにあるじゃない......花瓶......"

    ro1 "からかうなー！このポンコツめ！"

    show girl at right with dissolve

    g "ほんとに見えてないみたい......"

    hide robot1 with dissolve

    hide girl with dissolve

    show girl at center with dissolve

    show screen f1r2_screen(read_room(), visible=True)

    show girl at center with dissolve

    g "ねえ君、聞いてる？"

    g "何とかして、この部屋にドアを持ってこられないかな......"

    show girl look away at center with dissolve
    
    g "このc......なんとかロボット君には......悪いけど"

    show girl at center with dissolve

    g "次の部屋へ進まなくちゃ、こんなところでは終われないよ"

    hide girl with dissolve
    
    $ event_end("f1r2.scloop")