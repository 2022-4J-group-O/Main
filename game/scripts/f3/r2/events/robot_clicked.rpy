label f3r2_robot2_clicked:
    show screen f3r2_screen(read_room(), False)  # ロボットを不可視に
    show robot2 at left with dissolve
    show girl at right with dissolve
    
    if f3r2_flg_q1:
        jump .q1
    else:
        jump .q2

label .q1:
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

label .q2:
    menu:
        ro2 "最後のクイズは解けましたか？"
        "はい":
            ro2 "では、確認しましょう"
            ro2 "......"
            ro2 "回答は......"
            $ path = os.path.join(config.basedir, "game_data", current_room, "ending.png")
            if check_hash_binary(path):
                ro2 "おめでとうございます！正解です！"
                g "やった！"
                g "これで、エンディングを迎えられるね"
                ro2 "ええ、それでは、このゲームのエンディングを、お見せします"
                jump ending
            else:
                ro2 "不正解です"
                ro2 "最後の謎ですから、なかなか手ごわいですよ"
                g "エンディング用の素材を見つければいいのよね"
                ro2 "はい。その通りです"
                ro2 "ファイルが見つかったらこの部屋のディレクトリ上に配置してくださいね"
                ro2 "仮ではありますが、このゲームのエンディングを、お見せしましょう"
        "いいえ":
            show robot2 smile at left with dissolve
            ro2 "最後の謎ですから、 楽しんでくださいね"
            show robot2 at left with dissolve
            g "エンディング用の素材を見つければいいのよね"
            ro2 "はい。その通りです"
            ro2 "ファイルが見つかったらこの部屋のディレクトリ上に配置してくださいね"
            ro2 "仮ではありますが、このゲームのエンディングを、お見せしましょう"

    hide girl with dissolve
    hide robot2 with dissolve
    $ event_end()
