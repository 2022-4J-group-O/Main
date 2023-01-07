"""
隠しファイルを初めてクリックしたときに呼び出される会話
"""

label f1r2_ev_hidden_clicked:

    show girl with dissolve

    g "あの何とかロボット君、この家具は見えていないようだったけど......どうしてだろう"

    hide girl

    show girl at right with dissolve
    show robot1 at left with dissolve

    g "ねえ、何とかロボット君"

    ro1 "私の名前はcG9ua290c3U=だ。このポンコツめ"

    g "君、ここにある花瓶とチェスト、本当に見えてないの？"

    ro1 "この部屋に家具などあるわけがないだろう"

    g "よく見て。ここに家具が置いてあるじゃない"

    ro1 "さっきから何なんだね君は、家具などこの部屋にはない！私をからかうのもいいかげんにしなさい"

    show girl look away at right with dissolve

    g "わかったよ。ごめん"

    hide robot1
    hide girl

    show girl with dissolve

    g "やっぱり、この花瓶とチェスト......あの何とかロボット君には見えてないみたい"

    g "ほかのドアや、家具は見えていたみたいだし......どうしてなんだろう"

    hide girl
    
    return