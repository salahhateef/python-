print("welcome to ATM machine")
pin_code = 6383
balance = 6700
pin = int(input("enter your pin code : "))
if pin != pin_code :
    print ("invalid pin code ")
    exit()
else :
    print("choose your transaction : ")
print("1. check balance")
print("2. withdraw money")
transaction = int(input("enter your choice : "))
if transaction == 1 :
    print(f"your balance is : {balance}")
elif transaction == 2 :
    the_amount = int(input("enter the amount of money do you want to withdraw :"))
    if the_amount > balance :
       print("your balance noot enough for this transaction")
    else :
        balance -= the_amount
        print(f"your transaction is successful and your new balance is : {balance}")