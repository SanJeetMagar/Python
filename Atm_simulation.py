balance = 10000
while True:
    print("----Open Menu----")
    print("1. Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = int(input("Enter the choice between (1 to 4)?"))
    if choice == 1:
        print(f"Your Balance is: {balance}")
    elif choice == 2:
        deposit = float(input("How much u want to desposit? \n"))
        balance += deposit
        print(f"Your new balance is {balance}")
    elif choice == 3:
        withdraw_amount = float(input("How much u want to withdraw? \n"))
        if balance < withdraw_amount:
            print("Insufficient Balance")
        else:    
            balance -= withdraw_amount
            print(f"Your new balance is {balance}")
    else:
        exit()            