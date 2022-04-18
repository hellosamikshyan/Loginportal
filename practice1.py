from time import sleep


username="Samikshyan Mishra"
password="Ghtmlz21"

User=input("Enter your username")
Pass=input("Enter your password")

if username==User and password==Pass:
    sleep(1)
    print("Checking your username...///..")
    print("Authunticate")

else:
    print("Again checking once more . keep pataince")
    sleep(0.6)
    print("XXX Authentication failed you are kicked out of this login portal")
    exit()
