# ATM Machine
attempt = 0
balance = 10000
pin = '1234'
a = ''
bye = 0
while True:
    if attempt<3:
        attempt += 1
        a = input("Enter your PIN:")
        if a == pin:
            while True:
                print("\n1. Check balance\n2. Deposit Money\n3. Withdraw Money\n4. Exit")
                b = input("Choose option:")
                if b == '1':
                    print(f"Balance:{balance}")
                elif b == '2':
                    deposit = input("Enter amount:")
                    if deposit.isnumeric():
                        deposit = int(deposit)
                        if deposit>0:
                            balance+=deposit
                            print("Deposit successful!")
                            print(f"Balance:{balance}")
                        else:
                            print("Invalid Deposit amount!")
                            continue
                    else:
                        print("Invalid Deposit amount!")
                        continue
                elif b == '3':
                    withdraw = input("Enter amount:")
                    if withdraw.isnumeric():
                        withdraw = int(withdraw)
                        if withdraw<=balance and withdraw>0:
                            balance-=withdraw
                            print("Withdraw successful!")
                            print(f"Balance:{balance}")
                        else:
                            print("Invalid Withdraw amount!")
                            continue
                    else:
                        print("Invalid Withdraw amount!")
                        continue
                elif b == '4':
                    bye = 1
                    break
                else:
                    print("Enter 1, 2, 3 or 4 only.")
                    continue
        else:
            print("Wrong PIN")
            continue
    elif attempt>=3 and a!=pin:
        print("Sorry, you've reached your attempt limits.")
        break
    if bye:
        break
print("BYE BYE!")