init python:
    import shutil
    # オブジェクトを移動する関数
    def move_obj(objlist, path=None):
        if path == None:
            os.chdir(os.path.join(user_dir_path, "loadfile1/room2"));
            path = "../room1"
        for o in objlist:
            shutil.move(o, path)
    # 隠しファイルでないファイルを取得
    def not_hidden():
        os.chdir(os.path.join(user_dir_path, "loadfile1/room2"))
        l = read_room("loadfile1/room2")
        return [p for p in l if not is_hidden_file(p)]
