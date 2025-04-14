def main():
    print("This Program adds two numbers")

    num1: str = input("add first number: ")
    num1: int = int(num1)
    
    num2: str = input("add second number: ")
    num2: int = int(num2)

    total: int = num1 + num2
    print("The total is" + str(total) + ".")
    print(f"the sum of total num is: {total}.")
    
if __name__ == '__main__':
    main()
