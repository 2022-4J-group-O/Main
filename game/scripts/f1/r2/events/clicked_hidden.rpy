"""
隠しファイルを初めてクリックしたときに呼び出される会話
"""

label f1r2_ev_hidden_clicked:

    show girl with dissolve

    girl "あの何とかロボット君、この家具は見えていないようだったけど......どうしてだろう"

    hide girl

    show girl at right with dissolve
    show robot1 at left with dissolve

    girl "ねえ、何とかロボット君"

    robot1 "私の名前はcG9ua290c3U=だ。このポンコツめ"

    girl "君、ここにある花瓶とチェスト、本当に見えてないの？"

    robot1 "この部屋に家具などあるわけがないだろう"

    girl "よく見て。ここに家具が置いてあるじゃない"

    robot1 "さっきから何なんだね君は、家具などこの部屋にはない！私をからかうのもいいかげんにしなさい"

    show girl look away at right with dissolve

    girl "わかったよ。ごめんね何度も"

    hide robot1
    hide girl

    show girl with dissolve

    girl "やっぱり、この花瓶とチェスト......あの何とかロボット君には見えてないみたい"

    girl "ほかのドアや、家具は見えていたみたいだし......どうしてなんだろう"

    hide girl
    
    return