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
    print "4. nmap scan op 445"
    print "5. RESET"
    print "6. Exit"
    print 67 * "-"

loop=True

while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = input("Enter your choice [1-6]: ")
    if choice==1:
        cls()
        header()
        tijd = time.strftime("%H-%M-%S")
        ipadres = raw_input("ip-range: ")
        aantalip = input("aantal ip-adressen: ")
        count = 0
        os.system("mkdir %s" % (tijd))
        while (count < aantalip):
            cls()
            os.system("enum4linux %s.%s > %s/%s.%s.txt" % (ipadres,count,tijd,ipadres,count))
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
        tijd = time.strftime("%H:%M:%S")
        cls()
        header()
        print tijd
        time.sleep(3)
        ## test commands
    elif choice==4:
        cls()
        header()
        tijd = time.strftime("%H-%M-%S")
        ipadres = raw_input("ip-adres range: ")
        count = 0
        while (count < 1):
            if os.path.exists(ipadres):
                os.system("rm %s-iplist.txt " % tijd)
            else:
                print "Start scan!"
                os.system("nmap -p 445 %s -oG %s-iplist.txt -v" % (ipadres,tijd))
                time.sleep(3)
                count = count + 1
                ##cls()
            print "ip-lijst gegenereerd! \n"
            time.sleep(2)
        ## scan with nmap
        ## cat -s lol.txt | grep open | cut -f1,2 -d" " > test1.txt
    elif choice==5:
        cls()
        os.system("python main.py")
        ## reload application test purpuse only
    elif choice==6:
        cls()
        print "quitting!!"
        loop=False # This will make end to the while loop
    else:
        # error if option is higher than 6
        cls()
        raw_input("Wrong option selection. Enter any key to try again..")
        cls()
