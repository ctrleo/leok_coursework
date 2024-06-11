import os, hashlib
import password_manager, music

if os.path.exists(".passwords") == False:
    password_manager.init_pwsystem()

session = ""

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
print(f"Welcome, {session}")

if os.path.exists(os.path.join("library", session)) == False:
    print("Music library not found, would you like to create it?")
    choice = input("y or n?")
    if choice == "y":
        music.createLibrary(session)

while True:
    # menu
    print("Welcome to Leo\'s song quiz")
    print("1. Play quiz \n2. Add a new user \n3.Add songs \n4. Exit")
    choice = input(">>> ")