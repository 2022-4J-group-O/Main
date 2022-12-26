define g = Character('girl', color="#c8ffc8")
define ro1 = Character("cG9ua290c3U=", color="#cdc8ff")
define ro1_unknown = Character("???", color="#cdc8ff")

default global_data = Const()

label main_menu:
    return

label start:
    # TODO: 実行済みであることを記録し、Prologueから検知可能にする処理
    python:
        # 一回実行すれば十分
        # update_user_dir()
        global_data.lazy()

    jump title
    
    return

# ロールバックの無効化
init:
    $ config.keymap["rollback"] = []

# 各種フラグの初期化
default f1opening_flg = False