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

# 直接呼ばない
label say_about(calllabel_0, jumplabel_0=None, **kwargs):
    if not say_interact:
        $ say_interact = True
        call expression calllabel_0 pass (**kwargs) # must be returned
        $ say_interact = False
        if jumplabel_0 != None:
            python:
                jl = jumplabel_0
                # calllabel,jumplabelなどの変数はドロップされる。
                renpy.pop_call()
            jump expression jl
    return

# 引数を破棄してreturnする
label nop(*args, **kwargs):
    return