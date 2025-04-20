def add_Numbers(numbers) -> int:
    """
    This number take 1 number from numbers and add all numbers one by one
    """
    dummy_number: int = 0

    for number in numbers:
        dummy_number += number

    return dummy_number


def main():
    numbers: list[int] = [1, 2, 3, 4, 5]
    sum_of_numbers: int = add_Numbers(numbers)
    print(sum_of_numbers)


if __name__ == "__main__":
    main()

