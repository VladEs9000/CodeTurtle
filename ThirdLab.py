from abc import ABC, abstractmethod, abstractclassmethod
import random

class Basic(ABC):
    def pathcheck(self,str):
        flag = True
        while flag:
            way=input("Write the name.expansion of your file:")
            try:
                try:
                    way_rule=way.split('.')
                    way_rule.reverse()
                    if way_rule[0]==str:
                        return way
                    raise Exception("Wrong file extension")
                except Exception:
                    print("Wrong input or file not found")
            except BaseException:
                print("You have entered the wrong input")
    def read_txt(self):
        print("Please,enter the name of your text file")
        self.file_open = open(self.pathcheck("txt"),'r',encoding='utf-8').read()
        return(self.file_open)
    
    def alpha_read(self):
        print("Please,enter the name of your alphabet file")
        self.alphabet_list=[]
        with open(self.pathcheck("alph"),"r",encoding='utf-8') as file_alpha:
            line=file_alpha.readline()
            while line:
                if line[0]!='\n':
                    if self.alphabet_list.count(line[0]) == 0:
                        self.alphabet_list.append(line[0])
                line=file_alpha.readline()
        return(self.alphabet_list)
    @abstractmethod
    def encrypt(self):
        pass
        
    @abstractmethod
    def decrypt(self):
        pass
        
    @abstractmethod 
    def generate(self):
        pass
        
class Replace(Basic):
    
    def _prodigy(self):  
        self.alpha_replace = self.alpha_read()
        
    def generate(self):
        self._prodigy()
        key_list = self.alpha_replace
        alpha_key = key_list.copy()
        random.shuffle(key_list)
        print("Please,name your new key file")
        with open(self.pathcheck("key"),'w',encoding='utf-8') as file_key:
            for i in range(len(alpha_key)):
                file_key.write(alpha_key[i]+' '+key_list[i]+'\n')
            file_key.write("Replace - method")

    def _cryptod(self):
        print("Enter the name of your key file")
        self.dict1 = {}
        with open(self.pathcheck("key"),'r',encoding='utf-8') as checkfile:
            size_key = len(checkfile.readlines()) - 1
            checkfile.seek(0)
            for i in range(size_key):
                checkfile.readline()
            method = checkfile.readline().split(' - ')
            if method[0] == "Replace":
                pass
            else:
                return(False)
            checkfile.seek(0)
            for line in checkfile:
                if line[0]!='\n':
                    new_list=line.split(' ',1)
                    if len(new_list)==2:
                        self.dict1[line[0]]=line[2] 
                if line == "Replace - method":
                    pass  
        return(self.dict1)          
                        
    def encrypt(self):
        flag = True
        while flag:
            cryptodict = self._cryptod()
            if cryptodict == False:
                print("Wrong key file")
            else:    
                print("Enter the name of your text file")
                text1 = self.pathcheck("txt")
                new_line = ''
                with open(text1,'r',encoding='utf-8') as text:
                    for line in text:
                        for letter in line:
                            if letter in cryptodict.keys():
                                new_letter = cryptodict[letter]
                                new_line = new_line + new_letter
                            else:
                                new_line = new_line + letter
                print("Please,name your new encrypted file")
                with open(self.pathcheck("encode"),'w',encoding='utf-8') as encrypt_file:
                    encrypt_file.write(new_line)
                    encrypt_file.write("\nReplace - method")
                flag = False

    def decrypt(self):
        print("Enter the name of your crypted file")
        text1 = self.pathcheck("encode")
        with open(text1,'r',encoding='utf-8') as check_file:
            text_size = len(check_file.readlines()) - 1
            check_file.seek(0)
            for i in range(text_size):
                check_file.readline()
            last_line = check_file.readline()
            method = last_line
            last_line = len(last_line)
            method = method.rstrip().split(" - ")
            if method[0] == "Replace":
                pass
            else:
                print("Please,choose another crypted file")
                return(False)
        flag = True
        while flag:
            cryptoddict = self._cryptod()
            if cryptoddict == False:
                print("Wrong key file")
            else:
                dedict = dict(reversed(item) for item in cryptoddict.items())
                
                new_line = ''
                with open(text1,'r',encoding='utf-8') as delete_file:
                    size_crypt = len(delete_file.readlines()) - 1
                    delete_list = []
                    delete_file.seek(0)
                    for i in range(size_crypt):
                        delete_list.append(delete_file.readline())
                with open(text1,'w',encoding='utf-8') as new_file:
                    for i in range(len(delete_list)):
                        new_file.writelines(delete_list[i])
                with open(text1,'r',encoding='utf-8') as text:
                    for line in text:
                        for letter in line:
                            if letter in dedict.keys():
                                new_letter = dedict[letter]
                                new_line = new_line + new_letter
                            else:
                                new_line = new_line + letter
                with open(text1,'a',encoding='utf-8') as append_file:
                    append_file.write("Replace - method")
                print("Please,name your decrypted file")
                with open(self.pathcheck("txt"),'w',encoding='utf-8') as decrypt_file:
                    decrypt_file.write(new_line)
                flag = False
            
obj_replace = Replace()

class Transposition(Basic):
    def generate(self): 
        try: 
            j = 0
            for j in range(3):
                key_len = int(input("Please,enter the length of your key:"))
                if key_len < 2:
                    print("Wrong input")
                    j += 1
                    if j == 3:
                        print("You don't learn anything...")
                        break
                else:
                    key = list(range(0,key_len))
                    random.shuffle(key)
                    print("Please,enter the name of your new key file")
                    key_text = self.pathcheck("key")
                    new_line = ''
                    i = 0
                    with open(key_text,'w',encoding='utf-8') as key_file: 
                        while i < len(key):
                            if i == (len(key) - 1):
                                new_line = new_line + str(key[i]) + ':'
                                i += 1
                                break
                            new_line = new_line + str(key[i]) + ':'
                            i += 1
                        key_file.write(new_line) 
                        key_file.write("Transposition")  
                    break
        except Exception:
            print("Wrong input")   

    def encrypt(self):
        print("Enter the name of your text file")
        text = self.pathcheck("txt")
        text_line = open(text,'r',encoding='utf-8').read()
        print("Enter the name of your key file")
        flag = True
        while flag:
            key = self.pathcheck("key")
            key_text = open(key,'r',encoding='utf-8').read()
            key_text = key_text.split(':')
            if key_text[-1] == "Transposition":
                key_text.pop()
                flag = False
            else:
                print("Wrong key file.Enter the correct key please")
        count = len(key_text)
        new_line = ''
        count_text = len(text_line)
        diff = count_text % count
        if diff != 0:
            for q in range(count - diff):
                add_text = (chr(random.randrange(ord('а'), ord('я'), 1)))
                text_line = text_line + add_text
        count_text = len(text_line)
        trans_list = []
        with open(text,'r',encoding='utf-8') as crypted_text:
            for letter in range(0,count_text,count):
                if letter <= count_text:
                    trans_list = list(text_line[letter:letter + count])
                i = 0
                crypt_list=[None]*count
                for element in trans_list:
                    crypt_list[int(key_text[i])]=trans_list[trans_list.index(element)]
                    i+=1
                for crypt_element in crypt_list:
                    new_line = new_line + crypt_element
        print("Please,name your new encrypted file")
        with open(self.pathcheck("encode"),'w',encoding='utf-8') as encrypted_file:
            encrypted_file.write(new_line)
            encrypted_file.write("\nTransposition" +" - "+"method")
                             
    def decrypt(self):
        print("Enter the name of your crypted file") 
        crypt = self.pathcheck("encode")   
        with open(crypt,'r',encoding='utf-8') as check_file:
            text_size = len(check_file.readlines()) - 1
            check_file.seek(0)
            for i in range(text_size):
                check_file.readline()
            last_line = check_file.readline()
            method = last_line
            last_line = len(last_line)
            method = method.rstrip().split(" - ")
            if method[0] == "Transposition":
                pass
            else:
                print("Please,choose another crypted file")
                return(False)
        flag = True
        print("Enter the name of your key file")
        while flag:
            key = self.pathcheck("key")
            key_text = open(key,'r',encoding='utf-8').read()
            key_text = key_text.split(':')
            if key_text[-1] == "Transposition":
                key_text.pop()
                flag = False
            else:
                print("Wrong key file.Enter the correct key please")
        with open(crypt,'r',encoding='utf-8') as delete_file:
            size_crypt = len(delete_file.readlines()) - 1
            delete_list = []
            delete_file.seek(0)
            for i in range(size_crypt):
                delete_list.append(delete_file.readline())
        with open(crypt,'w',encoding='utf-8') as new_file:
            for i in range(len(delete_list)):
                new_file.writelines(delete_list[i])
        crypt_open = open(crypt,'r',encoding='utf-8')
        count_key = len(key_text)
        count_crypt = len(crypt_open.read())
        new_line = ''
        antitrans_list = []
        with open(crypt,'r',encoding='utf-8') as decrypt_text:
            line = decrypt_text.read()
            for letter in range(0,count_crypt,count_key):
                if letter <= count_crypt:
                    antitrans_list = list(line[letter:letter + count_key])
                i = 0
                for element in antitrans_list:
                    try:
                        new_element=antitrans_list[int(key_text[i])]
                        new_line = new_line + new_element
                        i+=1
                    except IndexError:
                        pass
        with open(crypt,'a',encoding='utf-8') as append_file:
            append_file.write("Transposition - method")    
        print("Please,name your decrypted file")
        with open(self.pathcheck("txt"),'w',encoding='utf-8') as decrypted_file:
            decrypted_file.write(new_line)
           
obj_trans = Transposition()   

class Gamming(Basic):

    def _prodigy_xor(self):  
        self.alpha_xor = self.alpha_read()

    def generate(self):
        self._prodigy_xor()
        alpha_list = self.alpha_xor
        key_list = []
        for number in range (len(alpha_list)):
            key_list.append(number)
        random.shuffle(key_list)
        print("Please,enter the name of your new key file")
        with open(self.pathcheck("key"),'w',encoding='utf-8') as file_key:
            for i in range(len(alpha_list)):
                file_key.write(alpha_list[i]+' - '+str(key_list[i])+'\n')
            file_key.write("XOR - method")

    def _cryptod_xor(self):
            print("Enter the name of your key file")
            self.dict_xor = ()
            with open(self.pathcheck("key"),'r',encoding='utf-8') as checkfile:
                    size_key = len(checkfile.readlines()) - 1
                    list_gamma = [x for x in range(size_key)]
                    list_alpha = list_gamma.copy()
                    checkfile.seek(0)
                    for i in range(size_key):
                        checkfile.readline()
                    method = checkfile.readline().rstrip().split(' - ')
                    if method[0] == "XOR":
                        pass
                    else:
                        return(False) 
                    checkfile.seek(0)
                    for i in range(size_key): 
                        line = checkfile.readline().rstrip().split(' - ') 
                        list_gamma[i] = line[1]
                        list_alpha[i] = line[0]       
                    return(list_alpha,list_gamma)          

    def encrypt(self):
        er = True
        print("Enter the name of your text file")
        text = self.pathcheck("txt")
        text_file = open(text,'r',encoding='utf-8')
        text_count = len(text_file.read())
        text_file.seek(0)
        new_line = ''
        while er:    
            cryptodict = self._cryptod_xor()
            if cryptodict == False:
                print("Wrong key file")
            else:
                while True:
                    try:
                        gamma = int(input("Please,enter the value of gamma:"))
                    except ValueError:
                        print("Enter the correct value")
                        continue
                    else:
                        if gamma > len(cryptodict[1]) or gamma < 1:
                            print("Wrong value of gamma")
                            continue
                        break
                if cryptodict == False:
                    print("Wrong key file")
                else:
                    count = 0
                    for char in range(text_count):
                        letter = text_file.read(1)
                        for i in range(len(cryptodict[0])):
                            if letter == cryptodict[0][i]:
                                letter = i
                                flag = True
                                break
                            else:
                                flag = False
                        if flag == True:
                            new_letter = int(letter) + int(cryptodict[1][count])
                            if count == gamma:
                                count = 0
                            count += 1
                            new_letter = new_letter % len(cryptodict[0])
                            new_line = new_line + cryptodict[0][new_letter]
                        elif flag == False:
                            new_line = new_line + letter
                print("Please,name your new crypted file")            
                with open(self.pathcheck("encode"),'w',encoding='utf-8') as encrypt_file:
                    encrypt_file.write(new_line)
                    encrypt_file.write("\nXOR - " + str(gamma))
                text_file.close()
                er = False

    def decrypt(self):
        print("Please,enter your crypted file")
        encode_file = self.pathcheck("encode")
        with open(encode_file,'r',encoding='utf-8') as check_file:
            text_size = len(check_file.readlines()) - 1
            check_file.seek(0)
            for i in range(text_size):
                check_file.readline()
            last_line = check_file.readline()
            method = last_line
            last_line = len(last_line)
            method = method.rstrip().split(" - ")
            if method[0] == "XOR":
                pass
            else:
                print("Please,choose another crypted file")
                return(False)
        er = True 
        while er:
            cryptodict = self._cryptod_xor()
            if cryptodict == False:
                print("Wrong key file")
            else:    
                new_line = ''
                encrypt_file = open(encode_file,'r',encoding='utf-8')
                text_count = len(encrypt_file.read()) - last_line
                encrypt_file.seek(0)
                if cryptodict == False:
                    print("Wrong key file")
                else:
                    count = 0
                    for char in range(text_count):
                        letter = encrypt_file.read(1)
                        for i in range(len(cryptodict[0])):
                            if letter == cryptodict[0][i]:
                                letter = i
                                flag = True
                                break
                            else:
                                flag = False
                        if flag == True:
                            new_letter = letter + len(cryptodict[0])
                            new_letter = new_letter - int(cryptodict[1][count])
                            if count == int(method[1]):
                                count = 0
                            count += 1
                            new_letter = new_letter % len(cryptodict[0])
                            new_line = new_line + cryptodict[0][new_letter]
                        elif flag == False:
                            new_line = new_line + letter
                print("Please,name your new decrypted file")            
                with open(self.pathcheck("txt"),'w',encoding='utf-8') as decrypt_file:
                    decrypt_file.write(new_line)
                encrypt_file.close()             
                er = False
obj_xor = Gamming() 

flag = True
i = 0
o = 0
p = 0
u = 0
q = 0
while flag == True:
    try:
        flag = True
        while u < 3:
            print("This is the start")
            print("\t Generateration of keys for methods - 1")
            print("\t Encryption/decryption - 2")
            print("\t Exit - 3")
            command = int(input("Please,choose:"))
            if command == 1:
                for i in range(3):
                    print("Here is the list of methods:")
                    print("\tGenerate key for replacement method - 1")
                    print("\tGenerate key for transposition method - 2")
                    print("\tGenerate key for XOR method - 3")
                    print("\tEnd the programm - 4")
                    print("\tReturn to previous menu - 5")
                    new_command = int(input("Please,choose:"))
                    if new_command == 1:
                        obj_replace.generate()
                        break
                    if new_command == 2:
                        obj_trans.generate()
                        break
                    if new_command == 3:
                        obj_xor.generate()
                        break
                    if new_command == 4:
                        print("Finishing programm...")
                        exit(0)
                    if new_command == 5:
                        break   
                    else:
                        print("Wrong input")
                        i += 1
                        if i == 3:
                            print("Никто не ожидает Испанскую Инквизицию")
                            flag = False
                            break
                break
            if command == 2:
                for q in range(3):
                    print("What do you choose?")
                    print("\tEncryption - 1")
                    print("\tDecryption - 2")
                    print("\tEnd the programm - 3")
                    print("\tReturn to previous menu - 4")
                    new2_command = int(input("Please,choose:"))
                    if new2_command == 1:
                        for o in range(3):
                            print("Encryption methods")
                            print("\tReplacement method - 1")
                            print("\tTransposition method - 2")
                            print("\tXOR method - 3")
                            print("\tEnd the programm - 4")
                            print("\tReturn to main menu - 5")
                            command_encrypt = int(input("Please,choose:"))
                            if command_encrypt == 1:
                                obj_replace.encrypt()
                                break
                            if command_encrypt == 2:
                                obj_trans.encrypt()
                                break
                            if command_encrypt == 3:
                                obj_xor.encrypt()
                                break
                            if command_encrypt == 4:
                                print("Finishing programm...")
                                exit(0)
                            if command_encrypt == 5:
                                break
                            else:   
                                print("Wrong input")
                                o += 1
                                if o == 3:
                                    print("Никто не ожидает Испанскую Инквизицию")
                                    flag = False
                                    break
                        break 
                    if new2_command == 2:
                        for p in range(3):
                            print("Decryption methods")
                            print("\tReplacement method - 1")
                            print("\tTransposition method - 2")
                            print("\tXOR method - 3")
                            print("\tEnd the programm - 4")
                            print("\tReturn to main menu - 5")
                            decrypt_command = int(input("Please,choose:"))
                            if decrypt_command == 1:
                                obj_replace.decrypt()
                                break
                            if decrypt_command == 2:
                                obj_trans.decrypt()
                                break
                            if decrypt_command == 3:
                                obj_xor.decrypt()
                                break
                            if decrypt_command == 4:
                                print("Finishing programm")
                                exit(0)
                            if decrypt_command == 5:
                                break
                            else:   
                                print("Wrong input")
                                o += 1
                                if o == 3:
                                    print("Никто не ожидает Испанскую Инквизицию")
                                    flag = False
                                    break 
                        break
                    if new2_command == 3:
                        print("Finishing programm...")
                        exit(0)
                    if new2_command == 4:
                        break
                    else:
                        print("Wrong input")
                        q += 1
                        if q == 3:
                            print("Никто не ожидает Испанскую Инквизицию")
                            flag = False
                            break 
                break
            if command == 3:
                print("Finishing programm...")
                exit(0)
            else:
                print("Wrong command")
                u += 1
                if u == 3:
                    print("Никто не ожидает Испанскую Инквизицию")
                    flag = False
                    break
    except SyntaxError:
        print("Wrong command")
    except ValueError:
        print("Wrong input data")
    except PermissionError:
        print("File cant be open because of underpermission")
        flag=False
        break
    except FileNotFoundError:
                print("File not found")
                                 
    except BaseException:
        print("System error")
        flag=False
        break 

    
