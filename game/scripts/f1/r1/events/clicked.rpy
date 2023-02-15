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

    if f1r1_cnt_calendar == 1:
    
        g "カレンダーだね"

        g "何かメモがしてある......"

        g "......\"regex\"？"

        g "なんのことだろう"
    
    if f1r1_cnt_calendar == 2:
        g "カレンダーだね"

        g "さっきは知らないふりをしたけど、この\"regex\"っていう書き込み......"

        g "\"regex\"って、regular expression、つまり、正規表現のことだと思うな"

        g "正規表現は、特定の条件を満たす文字列をまとめて表現する方法のことだよ"

        show girl look away at right with dissolve
        
        g "まあ、\"regex\"なんてカレンダーに書き込んだのかは、よくわからないんだけど"
    
    if f1r1_cnt_calendar >= 3:
        menu:
            g "regex、正規表現についてもっと聞きたい？"
            "はい":
                g "さっきも言った通り、正規表現は、特定の条件を満たす文字列をまとめて表現する方法のことだよ"
                g "正規表現は、例えばこんな見た目をしているよ: 「a(a-z)c\{2\}」"
                show girl smile at right with dissolve
                g "顔文字みたいでちょっとかわいいね"
                show girl at right with dissolve
                g "「a(a-z)b\{2\}」は、最初の文字がa、二文字目は小文字のアルファベットのどれか、最後の文字がbbである文字列を表すよ"
                g "「a(a-z)b\{2\}」を満たす文字列には、aabbとかabbbとか、acbb、azbbなんかがあるよ"
                g "こんな感じで、いろんな文字列を表すことができるんだ"
                g "他にもいろんなルールがあって、いろんな条件の文字列を表すことができるよ"
                g "文字列の検索なんかで使われていることがあるから、知っていると便利だったりするよ"
            "いいえ":
                g "わかった"

    hide girl with dissolve

    $ event_end()