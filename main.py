import os, hashlib, sys, time
import password_manager, music, game

if os.path.exists(".passwords") == False:
    print("Passwords not found, creating login system now!")
    password_manager.init_pwsystem()

session = ""
olduser = ""

while session == "":
    if 'checkuser' in locals():
        try:
            olduser = checkuser
        except:
            # cry
            olduser = ""
    checkuser = input("Enter username: ")
    if os.path.exists(os.path.join(".passwords", checkuser)) == False:
        print("User not found, please try again!")
        if olduser == checkuser:
            print("TIP: You can set up a new user from an already authorized account!")
    else:
        checkpw = input("Enter password: ")
        checkpw = checkpw.encode("utf8")
        pwhash = hashlib.sha256(checkpw)
        pwdigest = pwhash.hexdigest()
        pwfile = open(os.path.join(".passwords", checkuser))
        if pwfile.read() == pwdigest:
            print("Authorized!")
            session = checkuser
        else:
            print("Invalid Password! Try again...")
pwfile.close()
print(f"Welcome, {session}")

if os.path.exists(os.path.join("music", session)) == False:
    print("Music library not found, would you like to create it?")
    choice = input("y or n? ")
    if choice == "y":
        music.createLibrary(session)

while True:
    # menu
    print("Welcome to Leo\'s song quiz")
    print("1. Play quiz \n2. Add a new user \n3. Add song \n4. Check user points\n5. Exit")
    try:
        choice = int(input(">>> "))
    except:
        print("Error! Choice must be a number!")

    match choice:
        case 1:
            print("Entering song quiz!")
            game.play(session)
        case 2:
            un = input("Enter username for new user: ")
            pw = input("Enter password: ")
            password_manager.newuser(un, pw)
            print("Successfully added user")
        case 3:
            sn = input("Enter song name: ")
            sa = input("Enter song artist: ")
            music.addSong(sn, sa, session)
            print("Successfully added song")
        case 4:
            if os.path.exists(os.path.join(".scores", session)):
                print(f"{session} has {game.getPoints(session)} points!")
                sys.exit()
            else:
                print("Scores not found! Try playing a game first...")
        case 5:
            print("Come back soon!")
            sys.exit()
        case _:
            print("ERROR 404: OPTION NOT FOUND")
            print("ERROR 262: DISCONNECTED FROM OPTION PIPE")
            secret = input("press enter to reconnect to MAIN.PY...")
            reconnect = password_manager.socketmanager(404, 262, secret)
            if reconnect == True:
                print("Reconnecting...")
                time.sleep(1)
            if reconnect == False:
                print("Repairing connection...")
                password_manager.reconnect_pipe()