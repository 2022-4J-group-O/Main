﻿define g = Character('girl', color="#c8ffc8")

label main_menu:
    return

label start:
    # TODO: 実行済みであることを記録し、Prologueから検知可能にする処理

    jump f1r3_show_screen
    
    return

# ロールバックの無効化
init:
    $ config.keymap["rollback"] = []

# 各種フラグの初期化
default f1opening_flg = False