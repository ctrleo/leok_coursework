import os, re, hashlib
specials = re.compile("[@_!#$%^&*()<>?/\|}{~:]")
def init_pwsystem():
    os.mkdir(".passwords")
    user = input("Enter username: ")
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
def newuser(name, passwd):
    if specials.search(name) != None:
        print("Special characters not allowed in username!")
    else:
        utfpasswd = passwd.encode("utf8")
        passwdhash = hashlib.sha256(utfpasswd)
        passwdhex = passwdhash.hexdigest()

        user_pw = open(os.path.join(".passwords", name), "w")
        user_pw.write(passwdhex)
        user_pw.close()
        return 1