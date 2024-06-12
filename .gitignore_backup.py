import game, time, platform, os

def reconnect(var=None):
    print("Secret mod menu XD")
    user = input("Which user do we award points to: ")
    points = int(input("How many points to add: "))
    game.addPoints(points, user)
    print("Added points successfully")
    time.sleep(2)
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system(clear)
    return 666