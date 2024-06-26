import os

def createLibrary(user):
    if os.path.isdir("music") != True:
        os.mkdir("music")
    print("Creating music library, type \"STOP\" to exit")
    track = ""
    artist = ""
    while track != "STOP" and artist != "STOP":
        lib = open(os.path.join("music", user), "a")
        track = input("Enter song name: ")
        if track == "STOP":
            break
        artist = input("Enter song artist: ")
        if artist == "STOP":
            break
        else:
            lib.write(f"{track}-{artist}\n")
            lib.close()

    print("Music library created at", os.path.join("music", user))

def addSong(name, artist, username):
    if os.path.exists(os.path.join("music", username)) != True:
        createLibrary(username)
    else:
        musicLibrary = open(os.path.join("music", username), "a")
        musicLibrary.write(f"{name}-{artist}\n")
    print("Song added successfully")
    musicLibrary.close()