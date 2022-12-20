label f2r1_success:
    show girl 
    g "画像とおんなじ写真のオブジェとおけばよかったんだね"
    g "なんか、箱がでてきたね"
    g "箱の中身は何がはいっているのかな"
    g "それより、次のへやにいこ―"
    hide girl with dissolve
    $ f2r1_jumplabel = True
    $ event_end("f2r1.scloop")