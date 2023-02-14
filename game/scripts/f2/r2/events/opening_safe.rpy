label f2r2_opening_safe:

    # 金庫が開いた音を鳴らしたい
    play sound se_safe_unlock

    show girl at right with dissolve

    # セリフ

    hide girl with dissolve

    $ event_end(loop_label())