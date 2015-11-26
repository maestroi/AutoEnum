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
    print "3 Back"
    print 67 * "-"

update = True
while update:
    header()
    update_menu()
    choice = input("Enter your choice [1-3]: ")
    if choice==1:
        cls()
        print "je hebt gekozen voor stable"
        os.system("mv main.py main-old.py")
        os.system("wget https://github.com/maestroi/autoenum/blob/master/main.py")
        time.sleep(3)
        os.execl(sys.executable, sys.executable, *sys.argv)
    elif choice==2:
        cls()
        print "je hebt gekozen voor beta"
        os.system("mv main.py main-old.py")
        os.system("wget https://raw.githubusercontent.com/maestroi/autoenum/dubbel/v2/main.py")
        time.sleep(3)
        os.execl(sys.executable, sys.executable, *sys.argv)
    elif choice==3:
         cls()
         update = False
        ## reload application test purpuse only