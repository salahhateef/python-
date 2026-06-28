print("Hello Dear ")
x = float(input("enter the number : "))
if x < 100 :
    print("there is no discount : 00.0 ")
    print(f"total of payment is: {x}")
elif 100 <= x < 500 :
    discount = x * 0.1
    final = x - discount
    print(f"Value of discount is: {discount}")
    print(f"total of payment is: {final}")
else : 
    discount = x * 0.2
    final = x - discount
    print(f"Value of discount is: {discount}")
    print(f"total of payment is: {final}")