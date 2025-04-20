MAX_LENGTH : int = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()
        print(last_elem)

# There is no need to edit code beyond this point

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("\033[1;3;32m Please enter an element of the list or press enter to stop. \033[0m\n")
    while elem != "":
        lst.append(elem)
        elem = input("\033[1;3;32m Please enter an element of the list or press enter to stop. \033[0m\n ")
    return lst

def main():
    lst = get_lst()
    shorten(lst)


if __name__ == '__main__':
    main()