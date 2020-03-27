flag = 0
while flag < 3:
    flag = 0
    data1 = []
    dict1 = {}
    print('There is the list of your parameters')
    with open ('conf','r') as data:
        for line in data:
            if line[0] != '#' and line[0] != '\n' and line[0] != ';':
                data1.append(line)
                print(line.split()[0])
    key = input('Please,enter the required parameter: get param ')
    for line in data1:
        line = line.rstrip().split()
        data1 = True
        if len(line) > 1:
            data1 = line[1:len(line)]
        dict1[line[0]] = data1
    if key in dict1:
        print("You entered :",key,'.',"Its parameter is equal to :",dict1[key])
    else:
        print("There is now such a key in this file")
    while flag < 3:
        command = input("Would you like to repeat the programm(Y/N)")
        if command == 'Y' or command == 'y':
            break
        elif command =='N' or command == 'n':
            flag = 3
            break
        else:
            print("Wrong command")
            flag += 1 
    
            
    
    

