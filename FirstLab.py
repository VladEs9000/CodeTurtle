print("Welcome to the common calculator programm")

flag = 0
while flag < 2:
    val1 = int(input("input the first value ="))
    val2 = int(input("input the second value = "))

    

    command = input("input your operation (+,-,*,/):")

    #command = [+,-,*,/]
    if command == '+':
        print(val1 + val2)
    elif command =='-':
        print(val1 - val2)   
    elif command =='*':
        print(val1 * val2)   
    elif command =='/':
        print(val1 // val2)  
    else:
        print("wrong")             
    while (flag<2):
        command = input("Continue(Y/N)")
        if command == 'Y' or command == 'y':
            break
        elif command =='N' or command == 'n':
            flag = 3
            break
        else:
            print("Wrong command")
            flag += 1










