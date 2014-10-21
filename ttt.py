# tic tac toe
# author: Bo Meers

import time
import random
gridA = ["_","_","_"]
gridB = ["_","_","_"]
gridC = [" "," "," "]
lst = []

game = False
O = 0
X = 1

comp = input("Are you playing with someone else? (Y/N) ")
if comp in ("Y","y"):
    p1 = input("Player 1, what is your name? ")
    print("You will be 'X'")
    time.sleep(1)
    p2 = input("Player 2, what is your name? ")
    print("You will be 'O'")
    time.sleep(1)
    
    while not game:

        while X == 1:
            print("\n\t 0   1   2")
            print("\t_" + gridA[0] + "_|_" + gridA[1] + "_|_" + gridA[2] + "_ 0")
            print("\t_" + gridB[0] + "_|_" + gridB[1] + "_|_" + gridB[2] + "_ 1")
            print("\t " + gridC[0] + " | " + gridC[1] + " | " + gridC[2] + "  2\n")
            print("It is " + p1 + "'s turn.")
            time.sleep(2)
            a = int(input("Choose a horizontal row (0/1/2) "))
            b = int(input("Choose a vertical row (0/1/2) "))

            if a == 0:
                if b == 0:
                    if "0a" not in lst:
                        gridA[0] = "X"
                        lst.append("0a")
                        X = 0
                        O = 1
                    elif "0a" in lst:
                        print("This spot is already taken.")
                        time.sleep(1)
                        
                elif b == 1:
                    if "0b" not in lst:
                        gridA[1] = "X"
                        lst.append("0b")
                        X = 0
                        O = 1
                    elif "0b" in lst:
                        print("This spot is already taken.")
                        time.sleep(1)
                        
                elif b == 2:
                    if "0c" not in lst:
                        gridA[2] = "X"
                        lst.append("0c")
                        X = 0
                        O = 1
                    elif "0c" in lst:
                        print("This spot is already taken.")
                        time.sleep(1)
                    
            elif a == 1:
                if b == 0:
                    if "1a" not in lst:
                        gridB[0] = "X"
                        lst.append("1a")
                        X = 0
                        O = 1
                    elif "1a" in lst:
                        print("This spot is already taken.")
                        time.sleep(1)
                        
                elif b == 1:
                    if "1b" not in lst:
                        gridB[1] = "X"
                        lst.append("1b")
                        X = 0
                        O = 1
                    elif "1b" in lst:
                        print("This spot is already taken.")
                        time.sleep(1)
                        
                elif b == 2:
                    if "1c" not in lst:
                        gridB[2] = "X"
                        lst.append("1c")
                        X = 0
                        O = 1
                    elif "1c" in lst:
                        print("This spot is already taken.")
                        time.sleep(1)

            elif a == 2:
                if b == 0:
                    if "2a" not in lst:
                        gridC[0] = "X"
                        lst.append("2a")
                        X = 0
                        O = 1
                    elif "2a" in lst:
                        print("This spot is already taken.")
                        time.sleep(1)
                        
                elif b == 1:
                    if "2b" not in lst:
                        gridC[1] = "X"
                        lst.append("2b")
                        X = 0
                        O = 1
                    elif "2b" in lst:
                        print("This spot is already taken.")
                        time.sleep(1)
                        
                elif b == 2:
                    if "2c" not in lst:
                        gridC[2] = "X"
                        lst.append("2c")
                        X = 0
                        O = 1
                    elif "2c" in lst:
                        print("This spot is already taken.")
                        time.sleep(1)

        while O == 1:
            print("\t 0   1   2")
            print("\t_" + gridA[0] + "_|_" + gridA[1] + "_|_" + gridA[2] + "_ 0")
            print("\t_" + gridB[0] + "_|_" + gridB[1] + "_|_" + gridB[2] + "_ 1")
            print("\t " + gridC[0] + " | " + gridC[1] + " | " + gridC[2] + "  2\n")
            print("It is " + p2 + "'s turn.")
            time.sleep(2)
            a = int(input("Choose a horizontal row (0/1/2) "))
            b = int(input("Choose a vertical row (0/1/2) "))

            if a == 0:
                if b == 0:
                    if "0a" not in lst:
                        gridA[0] = "O"
                        lst.append("0a")
                        X = 1
                        O = 0
                    elif "0a" in lst:
                        print("This spot is already taken.")
                        time.sleep(1)
                        
                elif b == 1:
                    if "0b" not in lst:
                        gridA[1] = "O"
                        lst.append("0b")
                        X = 1
                        O = 0
                    elif "0b" in lst:
                        print("This spot is already taken.")
                        time.sleep(1)
                        
                elif b == 2:
                    if "0c" not in lst:
                        gridA[2] = "O"
                        lst.append("0c")
                        X = 1
                        O = 0
                    elif "0c" in lst:
                        print("This spot is already taken.")
                        time.sleep(1)

            elif a == 1:
                if b == 0:
                    if "1a" not in lst:
                        gridB[0] = "O"
                        lst.append("1a")
                        X = 1
                        O = 0
                    elif "1a" in lst:
                        print("This spot is already taken.")
                        time.sleep(1)
                        
                elif b == 1:
                    if "1b" not in lst:
                        gridB[1] = "O"
                        lst.append("1b")
                        X = 1
                        O = 0
                    elif "1b" in lst:
                        print("This spot is already taken.")
                        time.sleep(1)
                        
                elif b == 2:
                    if "1c" not in lst:
                        gridB[2] = "O"
                        lst.append("1c")
                        X = 1
                        O = 0
                    elif "1c" in lst:
                        print("This spot is already taken.")
                        time.sleep(1)
                        
            elif a == 2:
                if b == 0:
                    if "2a" not in lst:
                        gridC[0] = "O"
                        lst.append("2a")
                        X = 1
                        O = 0
                    elif "2a" in lst:
                        print("This spot is already taken.")
                        time.sleep(1)
                        
                elif b == 1:
                    if "2b" not in lst:
                        gridC[1] = "O"
                        lst.append("2b")
                        X = 1
                        O = 0
                    elif "2b" in lst:
                        print("This spot is already taken.")
                        time.sleep(1) 
                elif b == 2:
                    if "2c" not in lst:
                        gridC[2] = "O"
                        lst.append("2c")
                        X = 1
                        O = 0
                    elif "2c" in lst:
                        print("This spot is already taken.")
                        time.sleep(1)

# Against Computer ##########################################################################################################################################################

if comp in ("N","n"):
    girlName = ["Sophia","Charlie","Julia","Sadie","Ruby","Eva","Alice","Eliana","Taylor","Callie","Penelope","Camilla","Bailey","Kaelyn","Alexis"]
    boyName = ['Jackson','Aiden','Liam','Lucas','Noah','Mason','Jayden','Ethan','Jacob','Jack','Caden','Logan','Benjamin','Michael','Caleb']
    
    p1 = input("Ok, what is your name? ")
    print("You will be 'X'")
    time.sleep(1)
    ranNameA = random.randint(0,1)
    if ranNameA == 0:
        ranNameB = random.randint(0,14)
        print("Your opponent will be " + girlName[ranNameB])
    elif ranNameA == 1:
        ranNameB = random.randint(0,14)
        print("Your opponent will be " + boyName[ranNameB])

    while not game:

        while X == 1:
            print("\n\t 0   1   2")
            print("\t_" + gridA[0] + "_|_" + gridA[1] + "_|_" + gridA[2] + "_ 0")
            print("\t_" + gridB[0] + "_|_" + gridB[1] + "_|_" + gridB[2] + "_ 1")
            print("\t " + gridC[0] + " | " + gridC[1] + " | " + gridC[2] + "  2\n")
            print("It is " + p1 + "'s turn.")
            time.sleep(2)
            a = int(input("Choose a horizontal row (0/1/2) "))
            b = int(input("Choose a vertical row (0/1/2) "))

            if a == 0:
                if b == 0:
                    if "0a" not in lst:
                        gridA[0] = "X"
                        lst.append("0a")
                        X = 0
                        O = 1
                    elif "0a" in lst:
                        print("This spot is already taken.")
                        time.sleep(1)
                        
                elif b == 1:
                    if "0b" not in lst:
                        gridA[1] = "X"
                        lst.append("0b")
                        X = 0
                        O = 1
                    elif "0b" in lst:
                        print("This spot is already taken.")
                        time.sleep(1)
                        
                elif b == 2:
                    if "0c" not in lst:
                        gridA[2] = "X"
                        lst.append("0c")
                        X = 0
                        O = 1
                    elif "0c" in lst:
                        print("This spot is already taken.")
                        time.sleep(1)
                    
            elif a == 1:
                if b == 0:
                    if "1a" not in lst:
                        gridB[0] = "X"
                        lst.append("1a")
                        X = 0
                        O = 1
                    elif "1a" in lst:
                        print("This spot is already taken.")
                        time.sleep(1)
                        
                elif b == 1:
                    if "1b" not in lst:
                        gridB[1] = "X"
                        lst.append("1b")
                        X = 0
                        O = 1
                    elif "1b" in lst:
                        print("This spot is already taken.")
                        time.sleep(1)
                        
                elif b == 2:
                    if "1c" not in lst:
                        gridB[2] = "X"
                        lst.append("1c")
                        X = 0
                        O = 1
                    elif "1c" in lst:
                        print("This spot is already taken.")
                        time.sleep(1)

            elif a == 2:
                if b == 0:
                    if "2a" not in lst:
                        gridC[0] = "X"
                        lst.append("2a")
                        X = 0
                        O = 1
                    elif "2a" in lst:
                        print("This spot is already taken.")
                        time.sleep(1)
                        
                elif b == 1:
                    if "2b" not in lst:
                        gridC[1] = "X"
                        lst.append("2b")
                        X = 0
                        O = 1
                    elif "2b" in lst:
                        print("This spot is already taken.")
                        time.sleep(1)
                        
                elif b == 2:
                    if "2c" not in lst:
                        gridC[2] = "X"
                        lst.append("2c")
                        X = 0
                        O = 1
                    elif "2c" in lst:
                        print("This spot is already taken.")
                        time.sleep(1)
                        
        while O == 1:
            if ranNameA == 0:
                print(girlName[ranNameB] + " is thinking...")
            elif ranNameA == 1:
                print(boyName[ranNameB] + " is thinking...")
                
            time.sleep(2)
            a = random.randint(0,2)
            if a == 0:
                b = random.randint(0,2)
                if b == 0:
                    if "0a" not in lst:
                        gridA[0] = "O"
                        lst.append("0a")
                        X = 1
                        O = 0
                    elif "0a" in lst:
                        time.sleep(0)
                        
                elif b == 1:
                    if "0b" not in lst:
                        gridA[1] = "O"
                        lst.append("0b")
                        X = 1
                        O = 0
                    elif "0b" in lst:
                        time.sleep(0)
                        
                elif b == 2:
                    if "0c" not in lst:
                        gridA[2] = "O"
                        lst.append("0c")
                        X = 1
                        O = 0
                    elif "0c" in lst:
                        time.sleep(0)

            elif a == 1:
                b = random.randint(0,2)
                if b == 0:
                    if "1a" not in lst:
                        gridB[0] = "O"
                        lst.append("1a")
                        X = 1
                        O = 0
                    elif "1a" in lst:
                        time.sleep(0)
                        
                elif b == 1:
                    if "1b" not in lst:
                        gridB[1] = "O"
                        lst.append("1b")
                        X = 1
                        O = 0
                    elif "1b" in lst:
                        time.sleep(0)
                        
                elif b == 2:
                    if "1c" not in lst:
                        gridB[2] = "O"
                        lst.append("1c")
                        X = 1
                        O = 0
                    elif "1c" in lst:
                        time.sleep(0)
                        
            elif a == 2:
                b = random.randint(0,2)
                if b == 0:
                    if "2a" not in lst:
                        gridC[0] = "O"
                        lst.append("2a")
                        X = 1
                        O = 0
                    elif "2a" in lst:
                        time.sleep(0)
                        
                elif b == 1:
                    if "2b" not in lst:
                        gridC[1] = "O"
                        lst.append("2b")
                        X = 1
                        O = 0
                    elif "2b" in lst:
                        time.sleep(0) 
                elif b == 2:
                    if "2c" not in lst:
                        gridC[2] = "O"
                        lst.append("2c")
                        X = 1
                        O = 0
                    elif "2c" in lst:
                        time.sleep(0)
