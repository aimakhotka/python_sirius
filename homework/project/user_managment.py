import os
import subprocess
import sys
import getpass
  
def add_user(login):
    print("Adding new user account to %s" % os.uname()[1])
    print(f"Setting up account {login}...")
    
    try:
        subprocess.run(['useradd', '-m', '-d', f'/home/{login}', login])      
        subprocess.run(['passwd', login])
        print("\nNew user account ", login, "has been added.\n")
    except:
        print("\n", f"Failed to add user {login}.", "\n")                     
        sys.exit(1)

def del_user(login):
    print("Delete user account from %s" % os.uname()[1])
    
    try:
        print(f"Blocking the account {login}...")
        subprocess.run(['usermod', '-L', login])
        print(f"Log out of the {login} account...")
        subprocess.run(['killall', '-9', '-u', login])
        print(f"Deleting an account {login}...")
        subprocess.run(['userdel', '-r', login])
        print("\n", f"The user account {login} has been deleted.", "\n")
    except:
        print("\n", f"Failed to delete user {login}.", "\n")
        sys.exit(1)

def change_user(login):
    print("\nWould you like to change? Write a number OR press q\n")
    print("1) Block user \n2) Unblock user \n3) Add additional info")
    print("4) Change home directory \n5) Change user's group \n6) Add a user to additional groups")
    print("7) Change username \n8) Change command shell \n9) Change UID \n10) Change GID\n")
    answ = input("Your choice: ")
    
    
    
    if answ == '1':
        subprocess.run(['usermod', '-L', login])
        print(f"The user's account {login} has been blocked.")
    elif answ == '2':
        subprocess.run(['usermod', '-U', login])
        print(f"The user's account {login} has been unblocked.")
    elif answ == '3':
        tmp_var = input("Enter a line with the information: ")
        subprocess.run(['usermod', '-c', tmp_var, login])
    elif answ == '4':
        tmp_var = input("Enter the full path to the user's new home folder: ")
        subprocess.run(['usermod', '-d', tmp_var, '-m', login])
        subprocess.run(['grep', '-E', login, '/etc/passwd'])
    elif answ == '5':
        tmp_var = input("Enter the group to which the user will be added: ")
        subprocess.run(['usermod', '-g', tmp_var, login])
        subprocess.run(['id', login])
    elif answ == '6':
        tmp_var = input("Enter the groups to which the user will be added. Comma separation, without spaces: ")
        subprocess.run(['usermod', '-a', '-G', tmp_var, login])
        subprocess.run(['id', login])
    elif answ == '7':
        tmp_var = input("Enter new username: ")
        subprocess.run(['usermod', '-l', tmp_var, login])
        subprocess.run(['id', tmp_var])
    elif answ == '8':
        tmp_var = input("Enter new command shell: ")
        subprocess.run(['usermod', '-s', tmp_var, login])
    elif answ == '9':
        tmp_var = input("Enter new UID: ")
        subprocess.run(['usermod', '-u', tmp_var, login])
    elif answ == '10':
        tmp_var = input("Enter new GID: ")
        subprocess.run(['passwd', '-g', tmp_var, login])
    elif answ == 'q':
        sys.exit(0)

usr = getpass.getuser()
if usr != 'root':
    print("Error: You must be root to run this command.")
    sys.exit(1)

while True:
    print("\nLet's start! What do you want to do? [1/2/3/4/5]\n")
    print("1) Add new user account \n2) Delete user account \n3) Change user account \n4) Display a list of users \n5) Show detailed user information \n6) Exit\n")
    answ = input('Your choice: ')
    if answ == '1':
        tmp_var = input("Enter user login to adding: ")
        add_user(tmp_var)
    elif answ == '2':
        tmp_var = input("Enter user login to delete: ")
        del_user(tmp_var)
    elif answ == '3':
        tmp_var = input("User account to change: ")
        change_user(tmp_var)
    elif answ == '4':
        os.system("echo ''; sed 's/:.*//' /etc/passwd | tr '\n' ' '; echo ''")
    elif answ == '5':
        tmp_var = input("Enter user login: ")
        subprocess.run(['grep', tmp_var, '/etc/passwd'])
    elif answ == '6':
        break