import os
import time
import sys

##todo Delte directory and move file to main en replace old

def header():
    print "  __  __                 _             _ "
    print " |  \/  |               | |           (_)"
    print " | \  / | __ _  ___  ___| |_ _ __ ___  _ "
    print " | |\/| |/ _` |/ _ \/ __| __| '__/ _ \| |"
    print " | |  | | (_| |  __/\__ \ |_| | | (_) | |"
    print " |_|  |_|\__,_|\___||___/\__|_|  \___/|_|"
    print "                                         "

def cls():
    os.system("clear")

def update_menu():
    print 30 * "-" , "UPDATER" , 30 * "-"
    print "1 for Stable"
    print "2 for Beta"
    print 67 * "-"

def stable():
    os.system("curl https://raw.githubusercontent.com/maestroi/autoenum/master/main.py -o main.py")

def beta():
    os.system("curl https://raw.githubusercontent.com/maestroi/autoenum/dubbel/v2/main.py -o main.py")

def updater():
    os.system("curl https://raw.githubusercontent.com/maestroi/autoenum/dubbel/v2/updater.py -o update.py")


update = True
while update:
    header()
    update_menu()
    choice = input("Enter your choice [1-2]: ")
    if choice==1:
        print "You made the choice of Stable"
        ##os.system("mv main.py main-old.py")
        stable()
        time.sleep(3)
        cls()
        os.system("python main.py")
        sys.exit()
    elif choice==2:
        cls()
        print "You made the choice of Beta"
        ##os.system("mv main.py main-old.py")
        beta()
        updater()
        time.sleep(3)
        cls()
        os.system("python main.py")
        sys.exit()
    elif choice==3:
         cls()
         update = False

##curl https://raw.githubusercontent.com/maestroi/autoenum/dubbel/v2/main.py -o main.py