def some_three_copies(list ,data):
    for i in range(3):
        list.append(data)
        
def main():
    message=input("\033[1;3;32m Enter your message:\033[0m\n")
    list= []
    print("list-before",list)
    some_three_copies(list,message)
    
    print("list-after",list)
    
    
              
if __name__ == "__main__":
    main()            