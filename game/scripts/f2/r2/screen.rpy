# a,b,c,d,e,fの6枚の画像と、それらのうちどれか2つを足した15種類の画像が用意されている
# ehiq.pngのようなよくわからない名前の画像はa,b,...,a+b,a+c,...のうちのどれかに対応している
# プレーヤーはaに対応する画像とbに対応する画像がわかっているものとする
# cとdは本当は白黒の画像
define f2r2_pictures = {
    "door.png": "a+b",
    "aaaa.png": "c+d",
    "pass.png": "e+f",
    "rnjk.png": "a",
    "mbfh.png": "b",
    "srps.png": "c",
    "ijli.png": "d",
    "ehiq.png": "e",
    "ltkc.png": "f",
    "jeyc.png": "a+c",
    "zwus.png": "a+d",
    "vura.png": "a+e",
    "cgtm.png": "a+f",
    "esuz.png": "b+c",
    "ukqp.png": "b+d",
    "qihx.png": "b+e",
    "xupj.png": "b+f",
    "wyxi.png": "c+e",
    "dkzu.png": "c+f",
    "mqty.png": "d+e",
    "tcvk.png": "d+f",
}

define f2r2_pictures_rev = {v: k for k, v in f2r2_pictures.items()}

define f2r2_path = os.path.join(config.basedir, user_directory, "loadfile2/room2")

define f2r2_picture_frame1 = os.path.join(f2r2_path, "picture frame 1")
define f2r2_picture_frame2 = os.path.join(f2r2_path, "picture frame 2")
define f2r2_picture_frame3 = os.path.join(f2r2_path, "picture frame 3")

init python:
    def f2r2_read(folder):
        if os.path.isdir(folder):
            os.chdir(folder)
            return [pic for pic in f2r2_pictures if check_hash_binary(pic)]
        else:
            return []


screen f2r2_pictures_screen(pictures, **properties):
    draggroup:
        if len(pictures) == 1:
            $ pic = pictures[0]
        drag:
            if len(pictures) == 1:
                if renpy.can_show(f2r2_pictures[pic]):
                    add f2r2_pictures[pic]
                else:
                    add SampleImage(f2r2_pictures[pic], 150, 150, "#000000")
                clicked Event("f2r2_ev_picture_clicked", picture=pic)
            else:
                if renpy.can_show("picture error"):
                    add "picture error"
                else:
                    add SampleImage("picture error", 150, 150, "#000000")
                clicked Event("f2r2_ev_picture_clicked", picture="error")
            draggable False
            droppable False
            anchor (0.5, 0.5)
            properties properties

screen f2r2_screen(current, safe_visible):
    layer "master"
    use obj_screen(current)
    if os.path.isdir(f2r2_picture_frame1):
        use f2r2_pictures_screen(f2r2_read(f2r2_picture_frame1), pos=(770, 420))
    if os.path.isdir(f2r2_picture_frame2):
        use f2r2_pictures_screen(f2r2_read(f2r2_picture_frame2), pos=(1255, 420))
    if os.path.isdir(f2r2_picture_frame3):
        use f2r2_pictures_screen(f2r2_read(f2r2_picture_frame3), pos=(1720, 420))

    imagebutton:
        if renpy.can_show("add_button"):
            idle "add_button"
            at transform:
                xzoom 0.4
                yzoom 0.4
        else:
            idle SampleImage("足し算ボタン", 100, 100, "#0080ff")

        pos (1845, 600)
        anchor (0.5, 0.5)
        action Event("f2r2_ev_add_button_clicked")

    if safe_visible:
        imagebutton:
            idle "safe"
            hover "safe"
            pos (1615, 950)
            anchor (0.5, 1.0)
            action Event("f2r2_safe_clicked")