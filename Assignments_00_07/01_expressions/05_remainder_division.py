def main():
    num1:int =  int(input("\033[1;3;32m Please enter an integer to be divided: \033[0m"))
    num2:int =  int(input("\033[1;3;32m Please enter an integer to divide by: \033[0m"))
    
    quotient:int = num1 // num2
    reminder:int = num1 % num2
    
    print(f"\033[1;3;35m The result of this division is {quotient} with a remainder of {reminder} \033[0m")
    
    
    
         
if __name__ == "__main__":
    main()