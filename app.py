from cryptography.fernet import Fernet
from datetime import datetime as dt
from getpass import getpass
import os



master_key = '0xNone2Deep'

with open(f'{os.getcwd()}/key.key', 'rb') as key_file:
    encr_key = key_file.read()


def view_pass(key):
    with open(f'{os.getcwd()}/passlist.txt', 'rb') as pl:
        passwords = pl.readlines()
        if not passwords:
            print('\nSorry, you do not have any saved passwords. Add a password first. \n')
        else:
            for password in passwords:
                time, account_id, passw = password.decode().split('|')
                fer = Fernet(key)
                clear_pass = fer.decrypt(passw.encode())
                print(f'Acount ID: {account_id}, Password: {clear_pass.decode()}, Added on: {time} \n')
    

def add_pass(key):
    #Collect account details to encrypt
    account_id = input('Enter account ID: \n>>')
    passw = getpass('Enter the password: (password is hidden when typing) \n>>')

    fer = Fernet(key)
    encr_passw = fer.encrypt(passw.encode())

    with open(f'{os.getcwd()}/passlist.txt', 'a') as pl:
        pl.write(f'{dt.now()}|{account_id}|{encr_passw.decode()}\n')
    
    print('Password saved successfully! \n')



while True:
    master_code= getpass('Welcome! Please enter the master password to continue using the tool. (password is hidden when typing) \n>>')
    if master_code == master_key:
        while True:
            prog_mode = input('Do you want to add a new password or view existing ones? (add/view/q (to quit program)) \n>>')
            if prog_mode == "view":
                view_pass(encr_key)
            elif prog_mode == "add":
                add_pass(encr_key)
            elif prog_mode == 'q':
                quit()
            else:
                print('Invalid Mode.')
    else:
        print('You have entered an invalid master password. Please try again. \n')



