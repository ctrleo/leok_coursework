import os

def play(session):
    names = []
    artists = []
    if os.path.exists(os.path.join("music", session)) != True:
        raise Exception("Error! User\'s music library not found!")
    else:
        lib = open(os.path.join("music", session))
        for line in lib:
            split = line.split("-")
            print(f"{split[0]} by {split[1]}")