import os
import time
import sys

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
    os.system("wget https://github.com/maestroi/autoenum/archive/master.zip")
    os.system("unzip master.zip")
    os.system("rm master.zip")

def beta():
    os.system("wget https://raw.githubusercontent.com/maestroi/autoenum/dubbel/v2/main.py")

def updater():
    os.system("wget https://github.com/maestroi/autoenum/archive/dubbel.zip")
    os.system("unzip dubbel.zip")
    os.system("rm dubbel.zip")


update = True
while update:
    header()
    update_menu()
    choice = input("Enter your choice [1-2]: ")
    if choice==1:
        cls()
        print "je hebt gekozen voor stable"
        ##os.system("mv main.py main-old.py")
        stable()
        time.sleep(3)
        cls()
        os.system("python autoenum-master/main.py")
        sys.exit()
    elif choice==2:
        cls()
        print "je hebt gekozen voor beta"
        ##os.system("mv main.py main-old.py")
        beta()
        updater()
        time.sleep(3)
        cls()
        os.system("python autoenum-dubbel/v2/main.py")
        sys.exit()
    elif choice==3:
         cls()
         update = False