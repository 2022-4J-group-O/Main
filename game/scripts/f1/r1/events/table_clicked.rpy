label f1r1_table_clicked:
    $ renpy.dynamic(current=read_room())

    # Sofaが表示されていないとき(テーブルが浮いているとき)

    if "Sofa" not in current:

        show girl look away at right with dissolve

        g "......あー"

        g "......テーブル、浮いちゃってるね"

        show girl smile at right with dissolve

        g "びっくりした？"

        show girl at right with dissolve

        g "これはいわゆる、「仕様」ってやつだね"

        g "大人の事情、ともいえる"

        g "この世界のルールだと思って、受け入れてほしいな"

        hide girl with dissolve

        $ event_end()
    
    call table_clicked
    