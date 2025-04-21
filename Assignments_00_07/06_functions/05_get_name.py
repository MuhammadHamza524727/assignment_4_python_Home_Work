def get_name():
    return "Jerry"


def main():
    name = get_name()
    # print("Hey", name,"! ")
    print(f"\033[1;3;32m Hey {name} !\033[0m")

if __name__ == '__main__':
    main()