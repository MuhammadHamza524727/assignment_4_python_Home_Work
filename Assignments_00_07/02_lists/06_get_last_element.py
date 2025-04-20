def get_first_element(lst):
    """
    Prints the first element of a provided list.
    """

    # print(lst[-1])
    print(lst[len(lst) - 1])


def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("\033[1;3;32m Please again enter an element of the list or press enter to stop. \033[0m\n")
    return lst

def main():
    lst = get_lst()
    get_first_element(lst)


if __name__ == '__main__':
    main()

