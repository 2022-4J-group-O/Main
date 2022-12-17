# 渡された文字列を改行区切りでgirlにしゃべらせる
label say_simple(msg, jumplabel=None):
    show girl at right
    python:
        for s in msg.splitlines():
            g(s)
    hide girl
    if jumplabel != None:
        jump expression jumplabel
    
    return

# 引数を破棄してreturnする
label nop(*args, **kwargs):
    return
