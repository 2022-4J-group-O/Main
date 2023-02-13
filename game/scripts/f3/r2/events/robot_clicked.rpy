label f3r2_robot2_clicked:
    show screen f3r2_screen(read_room(), False)  # ロボットを不可視に
    show robot2 at left with dissolve
    show girl at right with dissolve

    menu:
        ro2 "クイズは解けましたか？"
        "はい":
            ro2 "では、回答を確認しましょう"
            ro2 "......"
            $ path = os.path.join(config.basedir, user_directory, current_room, "answer.txt")
            if os.path.isfile(path):
                $ ans = open(path, "r").read()
                ro2 "あなたの回答は......"
                ro2 "[ans]"
                ro2 "これは......"
                if ans in ["@MizukiTerasaki", "MizukiTerasaki"]:
                    jump f3r2_success
                else:
                    ro2 "残念。不正解です"
                    ro2 "どんどん間違えてください。間違えるたびに、正解に近づきます"
                    show robot2 smile at left with dissolve
                    ro2 "挑戦が成功を作るのですから"
            else:
                ro2 "おや、回答用のテキストファイルが存在しないようです"
                ro2 "新たにファイルを作っておきますね"
                $ open(os.path.join(config.basedir, user_directory, current_room, "answer.txt"), "w").close()
                ro2 "答えがわかったら、このファイルに入力してくださいね"
        "いいえ":
            g "このゲームの製作者のtwitterアカウントのidを答えればいいんだよね"
            ro2 "ええ、その通りです"
            ro2 "答えはこの部屋のテキストファイルに入力してくださいね"
            ro2 "ゆっくりお考え下さい。いつでも声をかけてくださいね"
        
    hide girl with dissolve
    hide robot2 with dissolve

    $ event_end()
    