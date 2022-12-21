label f3r1_jumproom:
    $ label_jump = ""
    python:
        import os
        file_path = './game_data/loadfile3/room1/Door.txt'
        if os.stat(os.path.join(config.basedir,file_path)).st_size == 0:
            renpy.jump ("f3r1.scloop")
        else:
            os.chdir(os.path.join(config.basedir,"./game_data/loadfile3/room1"))
            with open("Door.txt",'r') as file:
                data = file.read()
                roomdir = data
                if os.path.exists(os.path.join(config.basedir, "./game_data/", "./"+roomdir)):
                    roomdir = roomdir.replace("loadfile","f").replace("room","r").replace("/","")
                    label_jump = roomdir
                    renpy.jump (roomdir)
    return


        
