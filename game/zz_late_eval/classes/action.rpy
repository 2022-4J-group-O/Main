init python:
    # インタラクション的なことをしながらラベルを呼ぶ
    # callするラベルは必ずreturnされなければならない
    # screenからセリフを呼び出したいときは必ずこれを使う
    class FromSc(Action):

        def __init__(self, calllabel, jumplabel=None, **kwargs):
            self.clabel = calllabel
            self.jlabel = jumplabel
            self.kwargs = kwargs
        
        def __call__(self):
            renpy.call("say_about", calllabel_0=self.clabel, jumplabel_0=self.jlabel, **self.kwargs)
