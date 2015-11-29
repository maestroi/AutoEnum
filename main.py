__author__ = 'maestroi'

import os
import time
import sys
import string

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
    print "3. Test Tool"
    print "4. NMAP scan on 445"
    print "5. Update"
    print "6. Cleanup directory"
    print "9. Exit"
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
    choice = input("Enter your choice [1-6]: ")
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
                print("list of files")
                os.system("ls %s" % (tijd))
                time.sleep(3)
                x = x - 1
                cls()
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
                cls()
                print "Start scan!"
                os.system("enum4linux %s > %s.txt" % (ipadres,ipadres))
                time.sleep(3)
                count = count + 1
                cls()
            print "ipadres gescanned! \n"
            time.sleep(2)
            cls()
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
    elif choice==4: ##todo make list ready for enumerate
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
        list = os.popen('cat -s %s-iplist.txt | grep open | cut -f2 -d" "' % (tijd)).read()
        ##list = os.popen('%s-file.txt' % (tijd)).read()
        print 67 * "-"
        print list
        ##os.system('rm %s-cat.txt' % (tijd))
        ##os.system('rm %s-iplist.txt' % (tijd))
        time.sleep(1)
        ## scan with nmap
        ## cat -s lol.txt | grep open | cut -f1,2 -d" " > test1.txt
    elif choice==5:
        update = True
        while update:
            cls()
            header()
            update_menu()
            choice = input("Enter your choice [1-3]: ")
            if choice==1:
                print "You made the choice of Stable"
                os.system("curl https://raw.githubusercontent.com/maestroi/autoenum/master/main.py -o mainv1.py")
                cls()
                os.system("python mainv1.py")
                sys.exit()
            elif choice==2:
                cls()
                print "You made the choice of Beta"
                os.system("curl https://raw.githubusercontent.com/maestroi/autoenum/beta/main.py -o main.py")
                cls()
                os.system("python main.py")
                sys.exit()
            elif choice==3:
                cls()
                update = False
    elif choice==6:
        cls()
        header()
        choice = raw_input("Are you sure delete all the files except main.py? yes/no: ")
        if choice == "yes":
            os.system("find ! -name 'main.py' -type f -exec rm -f {} +")
            os.system("find ! -name 'main.py' -type d -exec rm -r {} +")
            cls()
            print "everything is deleted!"
        else:
            cls()
            print "nothing is deleted!"
            time.sleep(2)
        cls()
    elif choice==7:
        cls()
        header()
        tijd = time.strftime("%H-%M-%S")
        ipadres = raw_input("ip-adres range: ")
        print "Scan started this may take some while...."
        os.system("nmap -p 20,21,22,23,25,53,69,80,110,119,137,139,143,161,162,389,443,445,465,546,547,587,990,993,995,445 %s > %s-test.txt" % (ipadres,tijd))
        os.system('cat -s %s-test.txt | grep open %s-nmap.txt' % (tijd,tijd))
        print "Scan finnished!"
        time.sleep(10)
        cls()
    elif choice==9:
        cls()
        print "quitting!!"
        sys.exit()
    elif choice==10:
        cls()
        os.execl(sys.executable, sys.executable, *sys.argv)
        ## reload application test purpuse only
    else:
        # error if invalid option
        cls()
        raw_input("Wrong option! i think you need coffee and enter any key to try again..")
        cls()