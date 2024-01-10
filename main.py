import os

while True:

    try:
        n = int(input("enter n: "))
    except:
        print("invalid number")
        os.system("clear")
    else:
        rem = str(n)
        bottom = str(n + 4)
        total = str(((n + 4)*3) + n)
        print("remmainder: " + rem + "| number of bottom sides: " + bottom + " | total number of pieces " + total)
        usrInput = input("quit() to quit else press any other key to continue: ")
        if usrInput == "quit()":
            break
        else:
            os.system("clear")