init python:
    # 実行後のジャンプ先を返す
    def f2r2_add_picture():
        l1 = f2r2_read(f2r2_picture_frame1)
        l2 = f2r2_read(f2r2_picture_frame2)
        if os.path.isdir(f2r2_picture_frame3):
            shutil.rmtree(f2r2_picture_frame3)
        os.makedirs(f2r2_picture_frame3)
        if len(l1) == 1 and len(l2) == 1:
            fn = f2r2_pictures[l1[0]] + "+" + f2r2_pictures[l2[0]]
            if fn == "a+b" or fn == "b+a":
                return "f2r2_add_denied"
            if fn != "c+d" and fn != "d+c" and "c" in fn and "d" in fn:
                fn = fn.replace("+c", "").replace("+d", "").replace("c+", "").replace("d+", "")
            if fn in f2r2_pictures_rev:
                global_data.default_dir_data.make_file(f2r2_picture_frame3, os.path.join("loadfile2/room2", f2r2_pictures_rev[fn]))
                return "f2r2_added"
            else:
                fn = f2r2_pictures[l2[0]] + "+" + f2r2_pictures[l1[0]]
                if fn != "c+d" and fn != "d+c" and "c" in fn and "d" in fn:
                    fn = fn.replace("+c", "").replace("+d", "").replace("c+", "").replace("d+", "")
                if fn in f2r2_pictures_rev:
                    global_data.default_dir_data.make_file(f2r2_picture_frame3, os.path.join("loadfile2/room2", f2r2_pictures_rev[fn]))
                    return "f2r2_added"
                else:
                    return "f2r2_couldnt_add"
        else:
            # picture frame1かpicture frame2の中身がおかしい
            return "f2r2_couldnt_add"

default f2r2_add_button_clicked = False
default f2r2_add_button_selected = False
label f2r2_ev_add_button_clicked:
    
    if f2r2_add_button_clicked:
        show girl at right with dissolve

        g "ボタンを押すよ"

        play sound se_add_button
        $ f2r2_jump_event = f2r2_add_picture()

    else:
        # スイッチを押していない

        if f2r2_add_button_selected:
            show girl at right with dissolve

            g "やっぱり押してみる？"

            menu:
                "はい":
                    g "わかった、押してみるね"

                    play sound se_add_button
                    $ f2r2_add_button_clicked = True
                    $ f2r2_jump_event = f2r2_add_picture()

                "いいえ":
                    g "わかった、押さないでおく"
        else:
            call .first

    hide girl with dissolve

    $ event_end(loop_label())

label .first:
    show girl surprise at right with dissolve

    g "なんの変哲もないボタンがある...."

    show girl smile at right with dissolve

    g "押してみる？"

    $ f2r2_add_button_selected = True

    menu:
        "はい":

            show girl at right with dissolve

            g "本当に押すの？"

            g "何も書いてないボタンなんて怪しいよ？"

            menu:
                "それでも押す":

                    g "君は押そうとするんだ"

                    show girl smile at right with dissolve

                    g "大体の人はここで一旦諦めると思ったんだけどね"

                    g "君はボタンを押すことが正しいと信じているんだね"

                    g "じゃあ、君の要望通り押してみるよ"

                    play sound se_add_button
                    $ f2r2_add_button_clicked = True
                    $ f2r2_jump_event = f2r2_add_picture()

                "やっぱり押さない":

                    show girl smile at right with dissolve

                    g "そう言うと思ったよ"

                    g "「はい」を選んだ後にもう一度訊かれると自分が安易な選択をしたと思って過去の選択を取り消そうとする"

                    g "そこまで考えずに選択肢を選んだつもりでも無意識にそんな心理が働いてるのかもしれないよ"

                    show girl at right with dissolve

                    g "まあ、君が押さないっていうなら、ここは押さないでおくよ"

        "いいえ":

            show girl surprise at right with dissolve

            g "押さないの？"

            g "君がそういうならいいけど"
    return


# aとbを足そうとしたときのイベント
label f2r2_add_denied:

    $ renpy.notify("ERROR！！二つの画像は保護されています！！")

    $ event_end(loop_label())

# !TODO
# 画像の足し算が成功したときのイベント
label f2r2_added:

    $ event_end(loop_label())

# !TODO
# 用意されていない組み合わせで画像を足そうとしたときのイベント
label f2r2_couldnt_add:

    $ event_end(loop_label())