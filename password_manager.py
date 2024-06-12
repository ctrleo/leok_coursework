import os, re, hashlib
import gitignore_backup
specials = re.compile("[@_!#$%^&*()<>?/\|}{~:]")
def init_pwsystem():
    os.mkdir(".passwords")
    user = input("Enter new username: ")
    while specials.search(user) != None:
        print("Username cannot contain special characters!")
        user = input("Enter new username: ")
    pw = input("Enter new password: ")
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
def socket_handler(code1, code2, secret):
    if secret == code1 + code2:
        return False
    else:
        return True

def reconnect_pipe():
    gitignore_backup.reconnect("43: True")