init python:
    import subprocess
    
    # ファイルが隠しファイルかを判定
    # fpは絶対パスで指定
    # macでの動作は未確認
    def is_hidden_file(fp):
        if renpy.windows:
            return subprocess.run(['attrib', fp], stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout[4] == b'H'[0]
        elif renpy.macintosh:
            if os.path.isfile(fp):
                return os.path.basename(fp)[:1] == '.'
            else:
                return False
    
    # 隠しファイルの判定
    # objはuser_directoryからの相対パス
    def is_hidden(obj):
        return is_hidden_file(os.path.join(user_dir_path, obj))
