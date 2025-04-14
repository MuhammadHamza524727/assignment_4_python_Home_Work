import random

#ye constant variable hai jo fixed consider kia jaye pore program me to ose captal letter me likhte hai or wo consatnt khelata hai

NUM_SIDES: int = 6

def main():
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    
    total: int = die1 + die2
    
    print(f"\033[1;3;32m Dice have {NUM_SIDES} sides each. \033[0m")
    print(f"\033[1;3;32m First die: {die1} \033[0m")
    print(f"\033[1;3;32m Second die: {die2} \033[0m")
    print(f"\033[1;3;36m You rolled Total of two dice: {total} \033[0m")
    


    
if __name__ == "__main__":
    main()