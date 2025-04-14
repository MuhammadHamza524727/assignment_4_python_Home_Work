import math


def main():
    # BC ** 2 = AB ** 2 + AC ** 2

    AB: float = float(input("\033[1;3;32m Enter the length of AB: \033[0m"))
    AC: float = float(input("\033[1;3;32m Enter the length of AC: \033[0m"))

    BC: float = math.sqrt(AB**2 + AC**2)
    print(f"\033[1;3;35m The length of BC (The Hypotenuse) is: {BC} \033[0m")


if __name__ == "__main__":
    main()
