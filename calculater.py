def show_mean():
    print("\n calculater")
    print("1-Add")
    print("2-Subtract")
    print("3-Multiply")
    print("4-Divide")
    print("5-Exit")

while True:
    show_mean()
    choice = int(input("Enter the number:"))
    if(choice in [1,2,3,4,5]):
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))

    if(choice == 1):
        result = num1+num2
    if(choice == 2):
        result = num1-num2
    if(choice == 3):
        result = num1*num2
    if(choice == 4):
        result = num1//num2
    if(choice == 5):
        break
    else:
        print("Invalid operation entered")
        
    print("The result of the operation is {}".format(result))

   
   
