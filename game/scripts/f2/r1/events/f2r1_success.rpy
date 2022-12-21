label f2r1_success:
    show girl 
    g "画像とおんなじ写真のオブジェとおけばよかったんだね"
    g "なんか、なんか箱で出てきたね"
    g "あとで、箱の中を確認してみよう"
    g "それより、次のへやにいこ―"
    hide girl with dissolve
    $ f2r1_jumplabel = True
    $ event_end("f2r1.scloop")