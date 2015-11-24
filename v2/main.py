__author__ = 'maestroi'
import os
import time

def header():
    print "  __  __                 _             _ "
    print " |  \/  |               | |           (_)"
    print " | \  / | __ _  ___  ___| |_ _ __ ___  _ "
    print " | |\/| |/ _` |/ _ \/ __| __| '__/ _ \| |"
    print " | |  | | (_| |  __/\__ \ |_| | | (_) | |"
    print " |_|  |_|\__,_|\___||___/\__|_|  \___/|_|"
    print "                                         "

def tijd():
    from time import strftime
    print strftime("%H:%M:%S")

def cls():
    os.system("clear")

def fl():
    os.path.isfile()

def print_menu():
    header()
    print 30 * "-" , "MENU" , 30 * "-"
    print "1. Meerdere ip adressen scan"
    print "2. Single ip adres scan"
    print "3. Test stuff"
    print "4. RESET"
    print "5. Exit"
    print 67 * "-"

loop=True

while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = input("Enter your choice [1-5]: ")
    if choice==1:
        os.system("clear")
        header()
        ipadres = raw_input("ip-range: ")
        aantalip = input("aantal ip-adressen: ")
        count = 0
        os.system("mkdir %s" % ipadres)
        while (count < aantalip):
            cls()
            os.system("enum4linux %s.%s > /%s/%s.%s.txt" % (ipadres,count,ipadres,ipadres,count))
            print 'IP nu: %s van %s'%(count,aantalip)
            time.sleep(3)
            count = count + 1
        print "%s ip-adressen gescanned \n" % count
    ## scan multi ip's and save them as ip name's
    elif choice==2:
        cls()
        header()
        ipadres = raw_input("ip-adres: ")
        count = 0
        while (count < 1):
            if os.path.exists(ipadres):
                os.system("rm %s.txt " % ipadres)
            else:
                print "Start scan!"
                os.system("enum4linux %s > %s.txt" % (ipadres,ipadres))
                time.sleep(3)
                count = count + 1
                cls()
            print "ipadres gescanned! \n"
            time.sleep(2)
        ## scan a single ip and output it with ip as name
    elif choice==3:
        cls()
        header()
        print tijd()
        time.sleep(3)
        ## test commands
    elif choice==4:
        cls()
        os.system("python main.py")
        ## reload application test purpuse only
    elif choice==5:
        cls()
        print "quitting!!"
        loop=False # This will make end to the while loop
    else:
        # error if option is higher than 5
        cls()
        raw_input("Wrong option selection. Enter any key to try again..")
        cls()