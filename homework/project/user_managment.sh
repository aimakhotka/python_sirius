#!/bin/bash

add_user(){
    echo "Adding new user account to $(hostname)"
    echo "Setting up account $1..."
    useradd -m -d /home/$1 -s /bin/bash $1
    passwd $1
    echo -e "\nNew user account $1 has been added.\n"
}

del_user(){
    echo "Delete user account from $(hostname)"
    echo "Blocking the account $1..."
    usermod -L $1
    echo "Log out of the $1 account ..."
    killall -9 -u $1
    echo "Deleting an account $1..."
    userdel -r $1
    echo -e "\nThe user account $1 has been deleted.\n"
}

change_user(){

    echo -e "\nWould you like to change? Write a number OR press q\n"
    echo -e "1)Block user \n2)Unblock user \n3)Add additional info \n4)Change home directory \n5)Change user's group \n6)Add a user to additional groups"
    echo -e "7)Change username \n8)Change command shell \n9)Change UID \n10)Change GID\n"
    echo -n "Your choice: "; read answ

    case $answ in
        1)  usermod -L $1
            echo "The user's account $1 has been blocked."
            ;;
        2)  usermod -U $1
            echo "The user's account $1 has been unblocked."
            ;;
        3)  echo -n "Enter a line with the information: "; read info
            usermod -c "$info" $1
            ;;
        4)  echo -n "Enter the full path to the user's new home folder: "; read hpath
            usermod -d $hpath -m $1
            grep -E "$1" /etc/passwd
            ;;
        5)  echo -n "Enter the group to which the user will be added: "; read gname
            usermod -g $gname $1
            id $1
            ;;
        6)  echo -n "Enter the groups to which the user will be added. Comma separation, without spaces: "; read gnames
            usermod -a -G $gnames $1
            id $1
            ;;
        7)  echo -n "Enter new username: "; read chname
            usermod -l $chname $1
            id $chname
            ;;
        8)  echo -n "Enter new command shell: "; read commshell
            usermod -s $commshell $1
            ;;
        9)  echo -n "Enter new UID: "; read uid
            usermod -u $uid $1
            id $1
            ;;
        10) echo -n "Enter new GID: "; read gid
            usermod -g $gid $1
            id $1
            ;;
        q) exit 0
            ;;
    esac

}

if [ "$(id -un)" != "root" ] ; then
    echo "Error: You must be root to run this command."
    exit 1
fi

while :
do
    echo -e "\nLet's start! What do you want to do? [1/2/3/4/5]\n"
    echo -e "1) Add new user account \n2) Delete user account \n3) Change user account \n4) Display a list of users \n5) Show detailed user information \n6) Exit"
    echo -n "Your choice: "; read answ
    case $answ in
        1)  echo -n "Enter user login to adding: "; read login
            add_user "$login"
            ;;
        2)  echo -n "Enter user login to delete: "; read login
            del_user "$login"
            ;;
        3)  echo -n "User account to change: " ; read login
            change_user "$login"
            ;;
        4)  echo ""; sed 's/:.*//' /etc/passwd | tr '\n' ' '; echo ""
            ;;
        5)  echo -n "Enter user login: "; read login
            echo ""; grep "$login" /etc/passwd; echo ""
            ;;
        6)  exit 0
            ;;
    esac
done