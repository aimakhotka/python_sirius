# Проектное задание
## Титульный лист
<a name="титульный_лист"></a>
Образовательное учреждение: АНО ВО Колледж «Университет «Сириус»

Группа: 09.02.06 "Сетевое и системное администрирование"

ФИО студента: Махотка Алла Ивановна

ФИО преподавателя: Тенигин Альберт Андреевич

Название дисциплины: Программирование на языке Python


## Содержание

1. [Титульный лист](#титульный_лист)
2. [Введение](#введение)
3. [Описание концепции и как все работает](#концепция)
4. [Запуск сценариев](#запуск)
5. [Реализация на Bash](#bash)
6. [Реализация на Python](#python)
7. [Заключение и выводы](#выводы)


## Введение
<a name="введение"></a>

### Теоретическая справка
Python — высокоуровневый язык программирования общего назначения, ориентированный на повышение производительности разработчика, читаемости кода и его качества, 
а также на обеспечение переносимости написанных на нём программ.
«Язык программирования высокого уровня и его основная философия проектирования - это все о читабельности кода и синтаксисе, который позволяет 
программистам выражать концепции в нескольких строках кода»
Bash —  усовершенствованная и модернизированная вариация командной оболочки Bourne shell и язык программирования проекта GNU. Одна из наиболее популярных
современных разновидностей командной оболочки UNIX.

Различия Python и Bash для автоматизации процессов:

* Python - это язык программирования высокого уровня, простой в реализации и легкочитаемый. В то время как Bash является sh-совместимым интерпретатором 
* командного языка, который выполняет команды, считываемые со стандартного ввода или из файла.
* Python - легкий, простой и мощный язык. На Bash трудно писать и он не так силен, как Python.
* Python более прост в обслуживании, чем другие высокоуровневые языки. Однако bash вообще не требует обслуживания.
* Bash - это оболочка пользователя по умолчанию в каждом дистрибутиве Linux, что делает его относительно быстрее, чем Python с точки зрения 
* производительности
* Python мультиплатформенный, в то время как Bash используется по большей части на UNIX системах.
* Python поддерживает ООП, Bash - нет.
* Python требует установки сторонних программ, Bash - нет.


### Цели и задачи работы

> Придумать скрипт, который будет полезен для системного администратора

> Реализовать скрипт на Bash (минимум 30-40 осмысленных строк) и Python

> Проанализировать удобство реализаций на каждом из них


## Описание концепции и как все работает
<a name="концепция"></a>

Цель моего скрипта - облегчить рутинную работу системных администраторов по управлению учетными записями пользователей в системах UNIX.
Данный скрипт представляет собой удобный интерфейс для быстрого выполнения типовых задач в едином интуитивно понятном интерфейсе.

При запуске сценария в терминале появляется меню первого уровня с предложением выбрать желаемую операцию: 
1) *Добавить нового пользователя* - используются стандартные настройки для корректного создания пользователя. Пользователь добавляется в /etc/passwd, 
пароль шифруется и сохраняется, создается дефолтная домашняя дирректория /home/username, группа с именем пользователя, задается командная оболочка
по умолчанию.
2) *Удалить пользователя* - корректно удаляет пользователя из системы. Сначала блокирует домашнюю директорию пользователя, затем завершает
все процессы, принадлежащие пользователю, осуществляя принудительный выход из системы. Блокирует файлы с информацией о пользовате и удаляет 
пользователя из всех файлов, в том числе удаляет его домашнюю директорию и все файлы в ней.
3) *Изменить пользователя* - содержит список более тонких настроек.
4) *Вывести список имен пользователей в системе* - "вытаскивает" из файла /etc/passwd имена всех пользователей в системе и делает из них удобочитаемую строку.
5) *Вывести детальную информацию о пользователе* - с помощью grep осуществляет поиск строчки по имени пользователя в файле /etc/passwd и выводит ее.
6) *Выйти из программы* - корректно завершает программу.

После выбора опций 1-3, 5 появляется еще одна строчка, в которую нужно ввести username для совершения операции.
После этого операция автоматически выполняется.

При выборе опции 3 появляется меню второго уровня, предлагающее следующие операции: 
1) Заблокировать пользователя
2) Разблокировать пользователя
3) Добавить дополнительную информацию о пользователе (например, имя и фамилия)
4) Заменить домашнюю папку пользователя на новую (с сохранением файлов)
5) Заменить группу пользователя надругую (группа должна уже существовать в системе, старые группы удаляются)
6) Добавить к списку групп пользователя одну или несколько групп (без удаления старых групп)
7) Сменить имя
8) Сменить командную оболочку
9) Заменить UID
10) Заменить GID


## Запуск сценариев
<a name="запуск"></a>

Оба сценария необходимо запускать с **sudo**, тк манипуляции с учетными записями пользователей доступны только с root-правами.

Для того, чтобы запустить скрипт Bash, необходимо сначала дать ему права на выполение:
```
sudo chmod +x user_managment.sh
```
После этого можно запустить сценарий с помощью команды:
```
sudo ./user_managment.sh
```

Для работы python-скрипта необходимы модули os, sys, subprocess, getpass.
Для запуска из папки, в которой находится скрипт, выполните:
```
sudo /bin/python3 /home/$$$YOUR_PATH$$$/user_managment.py
```

## Реализация на Bash
<a name="bash"></a>

<details>
  <summary>Полный код</summary>
  
  ```bash
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
  
  ```
  
</details>


## Реализация на Python
<a name="python"></a>

<details>
  <summary>Полный код</summary>
  
  ```python
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
  
  ```
  
</details>


## Заключение и выводы
<a name="выводы"></a>

Для низкоуровневых операций с операционной системой предпочтительнее использовать Bash. Не использует постоянные вызовы сторонних модулей, а напрямую 
работает с системой. Следовательно, код "легче", проще в редактировании, использует меньше памяти.

Другие плюсы Bash:

1) Удобнее передавать аргументы строки
2) Удобный цикл case, аналог которого появился только в самых новых версиях python3

Плюсы Python:
1) Более удобное считывание пользовательского ввода
2) Лучше обработка ошибок
