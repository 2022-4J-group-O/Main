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


label calendar_clicked:
    show girl at right with dissolve

    g "カレンダーだね"

    g "何かメモがしてある......"

    g "......\"regex\"？"

    g "なんのことだろう"

    hide girl with dissolve

    $ event_end()