label books_clicked:
    show girl at right with dissolve

    g "乱雑に本が置かれてる......"

    g "本棚にしまえばいいのにね"

    hide girl with dissolve

    $ event_end()


label bookshelf_clicked:
    show girl at right with dissolve

    g "本棚だね"

    g "難解そうな本ばかりだよ"

    show girl smile at right with dissolve

    g "......って言っておけば、この本棚の絵には難解な本が入っていることになるよね"

    hide girl with dissolve

    $ event_end()


define f1r1_cnt_calendar = 0
label calendar_clicked:
    $ f1r1_cnt_calendar += 1

    show girl at right with dissolve

    if f1r1_cnt_calendar <= 1:
    
        g "カレンダーだね"

        g "何かメモがしてある......"

        g "......\"regex\"？"

        g "なんのことだろう"
    
    if f1r1_cnt_calendar >= 2:
        g "カレンダーだね"

        g "さっきは知らないふりをしたけど、この\"regex\"っていう書き込み......"

        g "\"regex\"って、regular expression、つまり、正規表現のことだと思うな"

        g "正規表現は、特定の条件を満たす文字列をまとめて表現する方法のことだよ"

        g "今後の謎解きに関係するかわからないけど、調べてみてね"

    hide girl with dissolve

    $ event_end()