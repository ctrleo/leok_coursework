import os, random, time, math

def play(session):
    names = []
    artists = []
    failed = False
    if os.path.exists(os.path.join("music", session)) != True:
        raise Exception("Error! User\'s music library not found!")
    else:
        lib = open(os.path.join("music", session))
        for line in lib:
            split = line.split("-")
            names.append(split[0])
            artists.append(split[1])
        index = random.randint(0, len(names) - 1)
        song = names[index]
        artist_name = artists[index]
        print("Selecting song...")
        for i in song:
            time.sleep(0.05)
            if i == song[0]:
                print(i, end="")
            else:
                print("_", end="")

        print(" by ", end="")

        for i in artist_name:
            time.sleep(0.05)
            if i == artist_name[0]:
                print(i, end="")
            else:
                print("_", end="")
        guess = input("Guess the song or artist: ")
        if guess == song:
            print("First Time!")
            return 1
        if guess != song or guess == artist_name:
            print("Artist name correct! revealing more characters...")
            charactersindex = []
            for i in range(math.floor(len(song) * 0.25)):
                randindex = random.randint(1, len(song) - 1)
                charactersindex.append(song[randindex])
            for i in song:
                if i == song[0]:
                    print(i, end="")
                elif i in charactersindex:
                    print(i, end="")
                else:
                    print("_", end="")
            print(f" by {artist_name}")
            print("last chance...")
            guess = input("Enter guess: ")
        if guess != song and guess != artist_name:
            print("Incorrect! Last guess...")
            guess = input("Enter guess: ")
        
        if guess == song:
            print(f"Correct!\nThe song was: {song} by {artist_name}")
            print("Play again soon!")
        else:
            print("You suck -_-")
            print(f"The song was: {song} by {artist_name}")
            print("No points for you!")