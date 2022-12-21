label f3r1:
   $ move_room("loadfile3/room1")
   scene bg f3r1

label .scloop:
   window hide
   show screen f3r1_screen (read_room())
   pause
   jump f3r1.scloop

