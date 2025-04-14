import random

NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    die1:int = random.randint(1, NUM_SIDES)
    die2:int = random.randint(1, NUM_SIDES)   
    total :int= die1 + die2
    print(f"Total of two dice: {total}\n")
    
    # loacl function me effect ni dalta hai
def main():
    die1 :int = 20
    print (str(f"dei in main as starting point {die1}"))
    
    for _ in range(5):
        
     roll_dice()
    
    
    print (str(f"dei in still main as starting point {die1}"))
    
if __name__ == '__main__':
    main()
       
    

