print("Welcome to Phinma-COC Bank")
username = input("Enter Your Name: ")
pinnun = 1234
total_money = 10000
pin = int(input("Please Enter Four Digit Pin: "))
if pin != pinnun:
    print("Wrong Pin Number")
else:
    useraw = input("[d]Deposit or [w]Withdraw: ")
    if useraw == "d":
        userdep = float(input("Please Enter the Amount You Would Like to Deposit: "))
        dep = float(input("Please Retype The Amount For Confirmation: "))
        print(userdep, " Pesos Have Been Deposited Into Your Account")
        sum1 = dep + total_money
        print("Would You Like To Have a Receipt?")
        userrec = input("[y]Yes or [n]No:")
        if userrec == "y":
            print("____________________________")
            print("Phinma-COC Bank")
            print("____________________________")
            print("Customer Name: ", username)
            print("Card Number XXXXXXXXXX54")
            print("Deposited: ", dep)
            print("Withdrawn: 0.0")
            print("New Balance: ", sum1 )
            print("______________________________")




    elif useraw == "w":
        userin = float(input("Please Enter The Amount of Money You Would to Withdraw: "))
        wit = float(input("Please Retype The Amount For Confirmation: "))
        if userin > total_money:
            print("Insufficient Amount")
        elif userin <= total_money:
            print(userin, " Pesos Have Been Withdrawn From Your Account")
            diff1 = total_money - wit 
            print("Would You Like To Have a Receipt?")
            userrec = input("[y]Yes or [n]No:")
            if userrec == "y":
                print("____________________________")
                print("Phinma-COC Bank")
                print("____________________________")
                print("Customer Name: ", username)
                print("Card Number XXXXXXXXXX54")
                print("Deposited: 0.0")
                print("Withdrawn: ", wit)
                print("New Balance: ", diff1)
                print("______________________________")




    else:
        print("Invalid Keyword")
