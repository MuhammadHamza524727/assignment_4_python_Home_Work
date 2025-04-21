def print_divisors(num):
    print(f"\033[1;3;34m Here are the divisors of {num}\033[0m ")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")
    print() 
def main():
    number = int(input("\033[1;3;34m 2Enter a number: \033[0m "))
    print_divisors(number)

if __name__ == "__main__":
    main()
