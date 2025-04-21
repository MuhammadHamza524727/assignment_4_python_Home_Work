def user_height():
    MINIMUM_HEIGHT = 50
    user_input = input("How tall are you? ")

    if user_input.strip() == "":
        print("Goodbye! Have a nice day ")
        return
    else:
        try:
            height = int(user_input)
            if height >= MINIMUM_HEIGHT:
                print("\033[1;3;34m You're tall enough to ride! \n \033[0m")
            else:
                print("\033[1;3;34m You're not tall enough to ride, but maybe next year! \n \033[0m")
        except ValueError:
            print(" \033[1;3;34m Please enter a valid number! \n \033[0m")

        user_height()
        
def main():
    
    user_height()

if __name__ == "__main__":
    main()
