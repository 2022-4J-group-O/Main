define default_user_dir_abs = os.path.join(config.basedir, default_user_dir)

init python:
    import shutil
    import glob

    def delete_dir_file(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
            os.mkdir(path)
    
    def delete_savefile():
        delete_dir_file(os.path.join(config.basedir, "game/saves"))
    
    # バイナリデータの全単射写像を定義するためのテーブルを作成
    # shiftは0~8のどれか
    def maketable(shift):
        num = 0
        for i in range(0, 256):
            num <<= 8
            num |= ((i << shift) | (i >> (8 - shift))) & 0x00FF
        return num.to_bytes(256, byteorder="big")
    
    # pathで指定されるファイルの中身を返す
    def dumpbfile(path):
        s = bytes()
        with open(path, "rb") as f:
            s = f.read()
        return s
    
    # デコード失敗時Noneを返す
    def dumpfile(path):
        s = str()
        try:
            with open(path, "r", encoding="utf-8") as f:
                s = f.read()
        except UnicodeDecodeError:
            return None
        return s

    # デフォルトのユーザー用ディレクトリ構造をバイナリデータで暗号化してpathで指定されるファイルに保存
    def update_user_dir(path=default_user_dir_abs):
        direc = Directory.read(path)
        by = direc.__repr__().encode("utf-8").translate(global_data.crypttable)
        with open(default_user_dirdata_path_abs, "wb") as f:
            f.write(by)
    
    # デフォルトのユーザー用ディレクトリ構造を読み込んで返す
    # 戻り値はDirectoryクラス
    def load_user_dirdata():
        by = dumpbfile(default_user_dirdata_path_abs).translate(global_data.decrypttable)
        return eval(by.decode("utf-8"))
    
    # 部屋をリセット(相対パスで)
    # ディレクトリが存在しない場合は生成される
    # 親ディレクトリが存在しないとエラー(要修正)
    def reset_room(room_path: str):
        cwd = os.getcwd()
        os.chdir(user_dir_path)
        if os.path.isdir(room_path):
            shutil.rmtree(room_path)
        # os.makedirs(room_path)
        global_data.default_dir_data.make(room_path, room_path)
        os.chdir(cwd)