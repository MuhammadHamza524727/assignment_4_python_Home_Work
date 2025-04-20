def main():

    numbers: list[int] = [1, 2, 3, 4]

    for i in range(len(numbers)):
        element_at_itrate = numbers[i]

    numbers[i] = element_at_itrate * 2
    print(numbers)


if __name__ == "__main__":
    main()
