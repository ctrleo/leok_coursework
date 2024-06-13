import os, random, time, math

def addPoints(points, session):
    if os.path.exists(os.path.join(".scores", session)) == False:
        if os.path.isdir(os.path.join(".scores")) == False:
            os.mkdir(".scores")
            score = open(os.path.join(".scores", session), "w")
            score.write(f"{points}")
        else:
            score = open(os.path.join(".scores", session), "rw")
            try:
                current = score.read()
            except:
                raise TypeError("Error! Score file contains non-int")
            
            final = int(current) + int(points)
            score.write(f"{final}")
        score.close()

def getPoints(session) -> int:
    if os.path.isfile(os.path.join(".scores", session)) == False:
        raise ValueError("Error! user score not found!")
    else:
        score = open(os.path.join(".scores", session), "r")
        try:
            points = int("" + score.read())
        except:
            raise TypeError("Error! Score file contains non-int")
        finally:
            return points


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
            print("+5 points")
            addPoints(5, session)
            return 1
        if guess != song and guess == artist_name:
            print("+2 point bonus")
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
            addPoints(1, session)
        else:
            print("You suck -_-")
            print(f"The song was: {song} by {artist_name}")
            print("No points for you!")