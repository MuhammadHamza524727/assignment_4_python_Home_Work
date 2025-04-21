def main():
    name : str = input("What's your name? ")
    print(greet(name))


def greet(name):
    return (f"\033[1;3;34m Greething {name}! \033[0m\n")
	
if __name__ == '__main__':
    main()
