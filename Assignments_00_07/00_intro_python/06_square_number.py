def main():
    print("\033[1;3;33m Calculate the square root\033[0m")
    
    num : float = float(input("\033[1;3;32m Type a number to see its square: \033[0m"))
    print(f"{num} squared is {num ** 2}")

if __name__ == "__main__":
    
    main()