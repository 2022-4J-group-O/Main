label f2r1_cup_clicked:
    show girl at right with dissolve

    g "コップのオブジェだね"

    g "これ、さっきも見たような？"
    
    hide girl with dissolve
    $ event_end()

label f2r1_apple_clicked:
    show girl at right with dissolve

    g "リンゴのオブジェだね"
    
    hide girl with dissolve
    $ event_end()

label f2r1_dog_clicked:
    show girl at right with dissolve

    g "犬のオブジェだね"

    hide girl with dissolve
    $ event_end()

label f2r1_pic_clicked:
    show girl at right with dissolve

    g "絵画が飾られているね"

    show girl look away at right with dissolve

    g "うーん......私には、芸術ってやつはよくわからないな"

    show girl at right with dissolve

    g "......って、そういえば私自身も\"絵\"だったね"

    g "絵が、絵を品定めしている様子はどう？"

    show girl smile at right with dissolve

    g "......絵になってる？"

    hide girl with dissolve
    
    $ event_end()

label f2r1_pic_error_clicked:
    show girl at right with dissolve

    g "この絵画......"

    g "現代アートの類が飾られてるのかと思ったけど......"

    g "違うっぽいね"

    g "どうやら、エラーが起こって表示できてないみたい"

    g "エラーを解決することはできるのかな"

    hide girl with dissolve
    
    $ event_end()