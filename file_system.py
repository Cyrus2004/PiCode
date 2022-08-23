#Things to do:
    #Add option to delete files (and mayby separate lines).
    #If possible, mayby even the possibility to not only read, but also edit the text in the .txt file, from the terminal, like in a word-document.



import time


files = []

while True:
    time.sleep(0.2)
    
    print("Commands:")
    print("     New")
    print("     Edit")
    print("     Read")
    
    #User input.
    command = input()
    
    #New file.
    if command == "New" or command == "new":
        print("Name:")
        name = input()
        file = open(name + '.txt', 'x')
        files.append(name)
        
    #Edit file
    if command == "Edit" or command == "edit":
        
        #Prints available files.
        x = 0
        for x in files:
            print(x)
        
        name = input()
        file = open(name + '.txt', 'a')
        text = "" #Makes the while-loop happy.
        while not text == "exit" and not text == "Exit":
            text = input()
            if text != "exit" and text != "Exit": #Avoids appending "exit" when the loop exits....
                file.write(text)
                file.write('\n')

    #Read file
    if command == "Read" or command == "read":
        
        #Prints available files.
        x = 0
        for x in files:
            print(x)

        name = input()
        file = open(name + '.txt', 'r')
        print(file.read())