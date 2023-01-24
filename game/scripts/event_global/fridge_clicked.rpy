# 今までにディレクトリ上に現れた冷蔵庫の最大数。
# 一度ディレクトリを生成してからそれを削除しても、減ることは無い。
define fridge_count = 1
# すべての冷蔵庫が開かれたか
define all_fridge_opened = False

label fridge_clicked:

    python:
        fridge_count = max(
            fridge_count, len(set(["fridge.zip", "fridge.7z", "fridge_pass.7z", "fridge_pass.zip"]) & set(read_room()))
        )
        if "archive.tar.gz" in read_room():
            all_fridge_opened = True

    show girl at right with dissolve

    # 冷蔵庫関連の謎がすでに終了している場合
    if all_fridge_opened:

        g "大量の冷蔵庫......"

        show girl smile at right with dissolve

        g "壮観だね"

    if fridge_count == 1:

        g "ずいぶん大きな冷蔵庫だね"

        g "なんでも入ってしまいそう"

        g "凍り付いた冷蔵庫を「解凍」して、中身を確認するのは君の仕事だよ"

        show girl smile at right with dissolve

        g "よろしくね"

    if fridge_count == 2:

        show girl surprise at right with dissolve

        g "なんでも入ってしまいそうな、大きな冷蔵庫だとは言ったけど......"

        g "同じ冷蔵庫がもう一個入ってるとは......"

        show girl smile at right with dissolve

        g "このゲーム、何でもありだね"

        show girl at right with dissolve

        g "この冷蔵庫の中身もさっさと「解凍」しましょう"
        
    if fridge_count == 3:

        g "またまた冷蔵庫......"

        show girl surprise at right with dissolve

        g "しかもこの冷蔵庫、鍵がかかってる！"

        g "鍵付きの冷蔵庫って......どんなセキュリティガジェットなの？"

        show girl smile at right with dissolve

        g "なんにせよ、中身を確認しないと、だよね"

        show girl at right with dissolve
        
        g "どこかにパスワードが書かれていたりしないかな"

        g "周辺を探してみて"
        
    if fridge_count == 4:

        g "また冷蔵庫......今回もご丁寧に、パスワード付き......"

        g "また、パスワードのヒントを探さないとね"

        show girl smile at right with dissolve

        g "......それとも、君なら力ずくで開錠できたりとかしない？"
    
    hide girl with dissolve

    $ event_end()

# すべての冷蔵庫は、クリックされるとfridge_clickedを呼び出す。
label fridge_zip_clicked:
    jump fridge_clicked
    $ event_end()

label fridge_7z_clicked:
    jump fridge_clicked
    $ event_end()

label fridge_pass_7z_clicked:
    jump fridge_clicked
    $ event_end()

label fridge_pass_zip_clicked:
    jump fridge_clicked
    $ event_end()
