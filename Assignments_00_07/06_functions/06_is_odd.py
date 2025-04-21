def main():

    for i in range(20):
        if odd(i):
            print(f"{i} is Odd number")
        else:
            print(f"{i} is even Number")


def odd(value:int):
    num = value % 2
    return num == 1


if __name__ == "__main__":
    main()
