label f1r2_show_screen:
    show screen f1r2_screen(read_room())
    call f1r2.check(jlbl="nop")
    pause
    jump f1r2_show_screen