define f2r2_path = "loadfile2/room2"
define f2r2_safe_pass = "2758"
define f2r2_safe_path = os.path.join(user_directory, f2r2_path, "safe")
define f2r2_safe_path_abs = os.path.join(config.basedir, f2r2_safe_path)

default f2r2_evflg_opening = True
default f2r2_jump_event = None
default f2r2_ev_add_button_clicked_seen = False
default f2r2_secret_images_generated = False

init python:
    f2r2_safe_pass_fp = os.path.join(f2r2_safe_path_abs, "password.txt")

    def f2r2_safe_check():
        if os.path.isfile(f2r2_safe_pass_fp):
            print(dumpfile(f2r2_safe_pass_fp))
            return dumpfile(f2r2_safe_pass_fp) == f2r2_safe_pass
        else:
            return False
    
    # 生成できたらTrue、できなかったらFalse
    def f2r2_gen_secret_images():
        check_folder_new(config.basedir, f2r2_safe_path)
        cwd = os.getcwd()
        os.chdir(f2r2_safe_path_abs)
        if os.path.isdir(f2r2_pictures_rev["a"]) or os.path.isdir(f2r2_pictures_rev["b"]):
            return False
        else:
            global_data.default_dir_data.make_file(".", os.path.join(f2r2_path, f2r2_pictures_rev["a"]))
            global_data.default_dir_data.make_file(".", os.path.join(f2r2_path, f2r2_pictures_rev["b"]))
            os.chdir(cwd)
            return True

label f2r2:
    if f2r2_evflg_opening:
        $ init_room("loadfile2/room2")
    $ move_room("loadfile2/room2")
    scene bg f2r2

label .scloop:
    window hide
    show screen f2r2_screen(read_room(), os.path.isdir(f2r2_safe_path_abs))

    python:
        if jump_label != None:
            tmp = jump_label
            jump_label = None
            Event(tmp)()

    if f2r2_evflg_opening:
        python:
            f2r2_evflg_opening = False
            Event("f2r2_ev_opening")()
    
    if f2r2_jump_event != None:
        python:
            renpy.dynamic(je=f2r2_jump_event)
            f2r2_jump_event = None
            Event(je)()
    
    if not f2r2_secret_images_generated and f2r2_safe_check():
        if f2r2_gen_secret_images():
            $ f2r2_secret_images_generated = True
            $ Event("f2r2_opening_safe")()

    pause
    jump .scloop

