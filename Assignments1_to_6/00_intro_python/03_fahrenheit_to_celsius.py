def main():
    print("\033[1;3;32m This program just like Wheather App\033[0m\n")
    
    userInput: float = float(input("Enter Temperature in Fahrenheit? "))
    degrees_celsius = (userInput - 32) * 5.0/9.0
    
    print(f"\033[1;3;32m Temperature : {userInput} = {degrees_celsius}C  \033[0m\n")
    
    
    
    
    
    

 
if __name__ == "__main__":
    main()