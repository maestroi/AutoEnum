__author__ = 'maestroi'
import os
import time

print "  __  __                 _             _ "
print " |  \/  |               | |           (_)"
print " | \  / | __ _  ___  ___| |_ _ __ ___  _ "
print " | |\/| |/ _` |/ _ \/ __| __| '__/ _ \| |"
print " | |  | | (_| |  __/\__ \ |_| | | (_) | |"
print " |_|  |_|\__,_|\___||___/\__|_|  \___/|_|"
print "                                         "




ipadres = raw_input("ip-range: ")
aantalip = input("aantal ip-adressen: ")
##filename = raw_input("filename:")

count = 10
while (count < aantalip):
   os.system("clear")
   os.system("enum4linux %s.%s > %s.%s.txt" % (ipadres,count,ipadres,count))
   print 'IP nu: %s van %s'%(count,aantalip)
   #print 'IP Totaal:', aantalip
   time.sleep(3)
   count = count + 1
print count
os.system("clear")
print "%s ip-adressen gescanned \n" % count
os.system("ls -A")

