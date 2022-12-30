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


label f2r2_ev_add_button_clicked:
    
    $ f2r2_jump_event = f2r2_add_picture()

    $ event_end(loop_label())

# !TODO
# aとbを足そうとしたときのイベント
label f2r2_add_denied:

    "足し算できない時のイベント"

    $ event_end(loop_label())

# !TODO
# 画像の足し算が成功したときのイベント
label f2r2_added:

    "足し算できた"

    $ event_end(loop_label())

# !TODO
# 用意されていない組み合わせで画像を足そうとしたときのイベント
label f2r2_couldnt_add:

    "大人の事情で足せない"

    $ event_end(loop_label())