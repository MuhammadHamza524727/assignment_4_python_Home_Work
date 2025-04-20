def main():
    lst = []  

    value:int = input("\033[1;3;32m Enter a first value: \033[0m\n ") 
    while value: 
        lst.append(value) 
        value = input("\033[1;3;33m Enter again a value: \033[0m\n") 

    print("Here's the list:", lst)



if __name__ == '__main__':
    main()