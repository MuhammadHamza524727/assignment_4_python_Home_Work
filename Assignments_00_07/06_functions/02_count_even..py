def count_even(lst):

    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    print(f"\033[1;3;35m Total even count: {count} \033[0m \n")

def get_list_of_ints():
    """
    Reads in integers until the user presses enter and returns the resulting list.
    """
    lst = []
    user_input = input("\033[1;3;32m Enter an integer or press enter to stop: \033[0m ")
    while user_input != "":
        lst.append(int(user_input))
        user_input = input("\033[1;3;32m Enter an integer or press enter to stop: \033[0m ")
    return lst

def main():
    lst = get_list_of_ints()
    count_even(lst)

if __name__ == '__main__':
    main()
