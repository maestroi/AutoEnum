__author__ = 'maestroi'
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

def fl():
    os.path.isfile()

def print_menu():
    header()
    print 30 * "-" , "MENU" , 30 * "-"
    print "1. IP-Range scan"
    print "2. IP Scan"
    print "3. Test Ttool"
    print "4. nmap scan op 445"
    print "5. reset tool"
    print "6. update"
    print "7. Exit"
    print 67 * "-"

def update_menu():
    print 30 * "-" , "MENU" , 30 * "-"
    print "1 for Stable"
    print "2 for Beta"
    print "3 Back"
    print 67 * "-"


loop=True

while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = input("Enter your choice [1-7]: ")
    if choice==1:
        cls()
        header()
        tijd = time.strftime("%H-%M-%S")
        print "example 0.0.0"
        ipadres = raw_input("ip-range: ")
        count = input("begin vanaf: ")
        aantal = input("tot ip-adres: ") +1
        os.system("mkdir %s" % (tijd))
        x = 1
        while (x):
            cls()
            print "scanning.... %s.%s" % (ipadres,count)
            os.system("enum4linux %s.%s > %s/%s.%s.txt" % (ipadres,count,tijd,ipadres,count))
            print "Done!"
            time.sleep(3)
            count += 1
            if count >= aantal:
                os.system("ls %s" % (tijd))
                time.sleep(3)
                x = x - 1
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
        ipadres = raw_input("ip-range: ")
        count = input("begin vanaf: ")
        aantal = input("tot ip-adres: ") +1
        ##totaal = count+aantal
        x = 1
        while (x):
            print "ik ben ip %s.%s" % (ipadres,count)
            count += 1
            if count >= aantal:
                x = x - 1
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
        os.system('cat -s %s-iplist.txt | grep open | cut -f1,2 -d" " > %s-cat.txt' % (tijd,tijd))
        os.system('cat %s-cat.txt' % (tijd))
        time.sleep(2)
        ## scan with nmap
        ## cat -s lol.txt | grep open | cut -f1,2 -d" " > test1.txt
    elif choice==5:
        cls()
        os.execl(sys.executable, sys.executable, *sys.argv)
        ## reload application test purpuse only
    elif choice==6:
        cls()
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
    elif choice==7:
        cls()
        print "quitting!!"
        loop=False # This will make end to the while loop
    else:
        # error if option is higher than 7
        cls()
        raw_input("Wrong option! i think you need coffee and enter any key to try again..")
        cls()
