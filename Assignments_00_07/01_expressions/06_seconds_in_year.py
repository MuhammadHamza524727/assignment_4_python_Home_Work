DAYS_PER_YEAR: int = 365
HOURS_PER_DAY: int = 24
MIN_PER_HOUR: int = 60
SEC_PER_MINUTE: int = 60


def main():
    quest1: int = int(
        input("\033[1;3;33m Would you like to  count a second in 1 year? Select and press enter \n 0: Yes \n 1: No \n \033[0m")
    )
    if quest1 == 0:

        Total_Second: int = (
            DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MINUTE
        )
        print(f"\033[1;3;36m There are {Total_Second} seconds in a year!😊 \033[0m")

    else:
        print("\033[1;3;35m Happy Coding😒 \033[0m")


if __name__ == "__main__":
    main()
