define ldissolve = Dissolve(1.0)

label f1r1_start:
    scene bg f1r1 with fade
    # 最初の一回だけ会話が流れる
    if not f1opening_flg:
        show girl with ldissolve
        g "ここのセリフはできてないよ"
        $ g("セリフを考えておいてね " + slow("お・ね・が・い"))
        hide girl with ldissolve
    jump f1r1_show_screen