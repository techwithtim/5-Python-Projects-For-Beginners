from cryptography.fernet import Fernet
import os
import time
global pwdinquiry
def accintro():
    global master_pwd
    print("NOTICE: This program only works on a Windows Operating System.")
    time.sleep(1)
    print("The account manager folder will be stored in the C:/ drive. The account manager folder is named 'accmgr_directory'.\nPlease DO NOT move this folder from the C:/ drive as it will result in your accounts being deleted.")
    print("The account manager folder just stores necessary files that the program needs and uses, so please do not mess with it!")
    time.sleep(1)
    master_pwd = "defaultpass0"
    print("The master password has been set to 'defaultpass0'. Please change your master password as soon as possible.")
parent_dir = "C:/"
directory = "accmgr_directory"
path = os.path.join(parent_dir, directory)
if os.path.exists(path) == False:
    accintro()
    os.mkdir(path)
passkey_path = path + "/pass_key.key"
userkey_path = path + "/user_key.key"
passw_path = path + "/passwords.txt"
def write_pass_key():
    pass_key = Fernet.generate_key()
    with open(passkey_path, 'wb') as pass_key_file:
        pass_key_file.write(pass_key)
def write_user_key():
    user_key = Fernet.generate_key()
    with open(userkey_path, 'wb') as user_key_file:
        user_key_file.write(user_key)
if os.path.exists(passkey_path) == False:
    write_pass_key()
if os.path.exists(userkey_path) == False:
    write_user_key()
def load_pass_key():
    file = open(passkey_path, 'rb')
    pass_key = file.read()
    file.close()
    return pass_key
def load_user_key():
    file = open(userkey_path, 'rb')
    user_key = file.read()
    file.close()
    return user_key
def passchange():
    global passinput, pass_ques
    print("Please change your password as the password in use is the default password and it is not a secure password.")
    time.sleep(2)
    print("If you would like to change your password, please type 'Yes', otherwise, please type 'No'.")
    time.sleep(2)
    pass_ques = input("Would you like to change your password? ")
    print("-" * 50)
def passinput():
    global masterpwd_change, numcheck, pwdreplay
    print("Conditions:\nYour password must be AT LEAST 8 characters long and must include uppercase/lowercase letters.\nYour Password must include numbers as well.\nIt is highly recommended that you include special charcters in your password.")
    print("-" * 50)
    masterpwd_change = input("What would you like for your new password to be? ")    
    numcheck = any(chr.isdigit() for chr in masterpwd_change)
    uppercheck = any(ele.isupper() for ele in masterpwd_change)
    lowercheck = any(ele.islower() for ele in masterpwd_change)
    def pwdreplay():
        global pass_ques
        print("If you would like to still change your password, please type 'Yes', otherwise, please type 'No'.")
        repass_ques = input("Would you like to change your password? ")
        if repass_ques == "Yes":
            passinput()
        if repass_ques == "No":
            pwdinquiry()
    if len(masterpwd_change) < 8:
        print("Your password could not be changed because it is less than 8 characters long.")
        pwdreplay()
    if numcheck == False:
        print("Your password could not be changed because you did not include numbers in your password")
        pwdreplay()
    if uppercheck == False:
        print("Your password could not be changed because you did not include uppercase letters in your password.")
        pwdreplay()
    if lowercheck == False:
        print("Your password could not be changed because you did not include lowercase letters in your password. ")
        pwdreplay()
    else:
        print("You may now login with your new password.")
passchange()
if pass_ques == "Yes":
    passinput()
    master_pwd = masterpwd_change
def pwdinquiry():
    masterpwd_ques = input('What is the master password? ')
    if masterpwd_ques != master_pwd:
        print('Incorrect password, exiting password manager.')
        quit()
pwdinquiry()
pass_key = load_pass_key()
user_key = load_user_key()
fer_pass = Fernet(pass_key)
fer_user = Fernet(user_key)
def view():
    with open(passw_path, 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            acc, user, passw = data.split('|')
            print('Account:', acc,'\n' 
            'User:', 
            fer_user.decrypt(user.encode()).decode(),'\n' 
            'Password:', 
            fer_pass.decrypt(passw.encode()).decode())
            print('-' * 15)
def add():
    account = input('Account: ')
    name = input('Username: ')
    pwd = input('Password: ')
    with open(passw_path, 'a') as f:
        f.write(account + '|' + fer_user.encrypt(name.encode()).decode() + '|' + fer_pass.encrypt(pwd.encode()).decode() + '\n')
while True:
    mode = input('Would you like to add a new password or view your passwords (view, add) press q to quit? ').lower()
    if mode == 'q':
        print('Goodbye')
        exit()
    if mode == 'view':
        if os.path.exists(passw_path) == False:
            print("No passwords have been saved!")
        else:
            view()
    elif mode == 'add':
        add()
    else:
        print('Invalid input')
        exit()
