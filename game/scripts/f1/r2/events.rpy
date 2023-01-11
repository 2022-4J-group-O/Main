
init python:
    import shutil

    room2pathrel = os.path.join(user_directory, "loadfile1/room2")
    room2path = os.path.join(config.basedir, user_directory, "loadfile1/room2")

    # オブジェクトを移動する関数 room2 -> room1
    def move_obj(objlist):
        cwd = os.getcwd()
        check_folder_new(config.basedir, room2pathrel)
        check_folder_new(config.basedir, os.path.join(user_directory, "loadfile1/room1"))
        os.chdir(room2path)
        path = "../room1"
        for o in objlist:
            shutil.move(o, path)
        os.chdir(cwd)

    # 隠しファイルでないファイルを取得
    def not_hidden_raw():
        l = read_room("loadfile1/room2")
        if l == []:
            return []
        os.chdir(room2path)
        return [p for p in l if not is_hidden_file(p)]

    def not_hidden():
        cwd = os.getcwd()
        l = not_hidden_raw()
        os.chdir(cwd)
        return l
