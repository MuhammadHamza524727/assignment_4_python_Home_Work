import random

def main():
    secret_num = random.randint(1, 5)
    
    print("\033[1;3;35m I am thinking of a number between 1 and 5... \033[0m \n")
    
    guess = int(input("Enter a guess: "))
    while guess != secret_num:
        if guess < secret_num:  
            print("\033[1;3;35m Your guess is too low \033[0m \n")
        else:
            print("\033[1;3;35m  Your guess is too high \033[0m \n")
            
        print() 
        guess = int(input("Enter a new guess: "))
        
    print(f"\033[1;3;46;33m Congrats! The number was: {secret_num} \033[0m \n" )
    
if __name__ == '__main__':
    main()