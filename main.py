import os, re, hashlib

if os.path.exists(".passwords") == False:
    print("Passwords not found! Creating now")
    os.mkdir(".passwords")
    user = input("Enter username: ")
    specials = re.compile("[@_!#$%^&*()<>?/\|}{~:]")
    while specials.search(user) != None:
        print("Username cannot contain special characters!")
        user = input("Enter username: ")
    pw = input("Enter a new password: ")
    utfpw = pw.encode("utf8")
    hashpw = hashlib.sha256(utfpw)
    password = hashpw.hexdigest()

    profile = open(os.path.join(".passwords", user), "w")
    profile.write(password)
    profile.close()
    print("User created successfully!")

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

while True:
    # menu
    print("Welcome to Leo\'s song quiz")
    print("1. Play quiz \n2. Add a new user \n3.Add songs \n4. Exit")
    choice = input(">>> ")