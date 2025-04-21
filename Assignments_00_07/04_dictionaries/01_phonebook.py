def read_phone_numbers():

    phonebook = {}                   

    while True:
        name = input("\033[1;3;34m Name: \033[0m \n")
        if name == "":
            break
        number = input("\033[1;3;34m Number: \033[0m \n ")
        phonebook[name] = number

    return phonebook


def print_phonebook(phonebook):
   
    for name in phonebook:
        print(f"{name} -> {phonebook[name]}")


def lookup_numbers(phonebook):
  
    while True:
        name = input(" \033[1;3;34m Enter name to lookup: \033[0m \n ")
        if name == "":
            break
        if name not in phonebook:
            print(name + " is not in the phonebook")
        else:
            print(phonebook[name])


def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)


if __name__ == '__main__':
    main()
    
    
       
           
           
    
    
    
        
        
    
 
 
 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    