def main():
    num: int = 9
    num = subtract_seven(num)
    print("This sould be zero: ", num)


def subtract_seven(num):
    num = num - 9
    return num


if __name__ == "__main__":
    main()
