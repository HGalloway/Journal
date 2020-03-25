import sys
import datetime
import time
import keyboard
import os
import pathlib

try:
    import Var_config
except ModuleNotFoundError:
	print ("Welcome!")
	print ("There is no config file available sooooooooooooo")
	name = input("What is your name?")
	print ("Thanks!")
	newconfigfile = "Var_config.py"
	f = open(newconfigfile, "a+")
	f.write("Name = '" + name + "'")
	f.close()
	os.makedirs("Entries")
	import Var_config

def tprint(stuff):
	print (stuff)
	time.sleep(1.)

print ("  Journal 1.0")
print ("  Made by Hilliard Drew Galloway")

print ("")

Date = str(datetime.date.today())
Time = str(datetime.datetime.today())
file_name = str((".\\Entries\\" +  "Entry" + Var_config.Name + Date + ".txt"))

#_______________________________________________________________________________
print ("Welcome " + Var_config.Name)
print ("Would you like to: ")
print ("Make a new entry")
print ("Add a subentry")
MER =input("Read an entry = ")

#_______________________________________________________________________________
if (MER == "Make a new entry"):
    print ("Begining Entry for the day: ")
    EI =input()
    f = open(file_name,"a+")
    f.write(Date + " " + Time +" = ")
    f.write(EI)
    f.close()
    Read =input ("Woud you like to read? /nYes /nNo ")
    if (Read == "Yes"):
        for x in ofr:
            print(x)
            QUIT = input("Press enter to quit application once done reading ")
    if (Read == "yes"):
        for x in ofr:
            print(x)
            QUIT = input("Press enter to quit application once done reading ")

    elif (Read == "No"):
        print ("Ok")
        sys.exit()
    elif (Read == "no"):
        print ("Ok")
        sys.exit()
if (MER == "make a new entry"):
    print ("Begining Entry for the day: ")
    EI =input()
    f= open(file_name,"a+")
    fr = open(file_name, "r")
    f.write(Time + " " + Date +" = ")
    f.write(EI)
    f.close()
    Read =input ("Woud you like to read? /nYes /nNo ")
    if (Read == "Yes"):
        for x in fr:
            print(x)
            QUIT = input("Press enter to quit application once done reading ")
    if (Read == "yes"):
        for x in fr:
            print(x)
            QUIT = input("Press enter to quit application once done reading ")

    elif (Read == "No"):
        print ("Ok")
        sys.exit()
    elif (Read == "no"):
        print ("Ok")
        sys.exit()
#_____________________________________________________________________________________________________________________________________________________________________
elif (MER == "Add a subentry"):
    EF =input("Date of entry? = ")
    of = open("Entry" + Var_config.Name + EF + ".txt","a+")
    ofr = open("Entry" + Var_config.Name + EF + ".txt","r")
    print ("Begin subentry:")
    SB = input("")
    of.write(" ")
    of.write("Subentry entered at " + Time + " = ")
    of.write(SB)
    of.close()
    Read =input ("Woud you like to read? /nYes /nNo ")
    if (Read == "Yes"):
        for x in ofr:
            print(x)
            QUIT = input("Press enter to quit application once done reading ")
    if (Read == "yes"):
        for x in ofr:
            print(x)
            QUIT = input("Press enter to quit application once done reading ")

    elif (Read == "No"):
        print ("Ok")
        sys.exit()
    elif (Read == "no"):
        print ("Ok")
        sys.exit()
elif (MER == "add a subentry"):
    EF =input("Date of entry? = ")
    of = open("Entry" + Var_config.Name + EF + ".txt","a+")
    ofr = open("Entry" + Var_config.Name + EF + ".txt","r")
    print ("Begin subentry:")
    SB = input("")
    of.write(" ")
    of.write("Subentry entered at " + Date + " = ")
    of.write(SB)
    of.close()
    Read =input ("Woud you like to read? /nYes /nNo ")
    if (Read == "Yes"):
        for x in ofr:
            print(x)
            QUIT = input("Press enter to quit application once done reading ")
    if (Read == "yes"):
        for x in ofr:
            print(x)
            QUIT = input("Press enter to quit application once done reading ")

    elif (Read == "No"):
        print ("Ok")
        sys.exit()
    elif (Read == "no"):
        print ("Ok")
        sys.exit()
#______________________________________________________________________________________________________________________________________________________________________
elif (MER == "Read an entry"):
        EF =input("Date of entry? = ")
        ofr = open("Entry" + Var_config.Name + EF + ".txt","r")
        for x in ofr:
                print(x)
                QUIT = input("Press enter to quit application once done reading")
                sys.exit()
elif (MER == "read an entry"):
        EF =input("Date of entry? = ")
        ofr = open("Entry" + Var_config.Name + EF + ".txt","r")
        for x in ofr:
                print(x)
                QUIT = input("Press enter to quit application once done reading")
                sys.exit()
