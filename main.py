import os

# This function adds name and password to the file named 
# "passwords.txt" or creates a file and put values
# while there is none
def add():
    name = input("User name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")


# This function sorts usernames and passwords and
# save them in the file named "passwords_sorted.txt"
def sort():
    bands = list()
    filename = 'passwords.txt'
    with open(filename) as f:
        for line in f:
            bands.append(line.strip())
    bands.sort()

    filename = 'passwords_sorted.txt'         
    with open(filename, 'w') as r:
        for band in bands:
            r.write(band + '\n')
            data = band.rstrip()
            user, passw = data.split("|")
            print("User name:", user, "| Password:", passw)


# Function prints the usernames and passwords found in the file.
def check():
    with open('passwords_sorted.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User name:", user, "| Password:", passw)            


# Function deletes the whole file named "passwords.txt".
def delete():
    myfile = "passwords.txt"
    os.remove(myfile)  
    print("File has been successfully deleted!")              


# Initializing the whole programm with while loop.      
while True:
    choice = input("check / add / sort / delete or quit (type q): ")
    if choice == "q":
        break
    
    if choice == "check":
        check()
    elif choice == "add":
        add()
    elif choice == "sort":
        sort()    
    elif choice == "delete":
        delete()    
    else:
        print("Invalid value!")
        continue




