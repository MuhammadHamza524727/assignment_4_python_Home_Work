def main():
    print("\033[1;3;33m Triangle size app\033[0m \n")
    
    question1 : float = float(input("\033[1;3;32mEnter the length of Side 1?\033[0m  "))
    question2 : float = float(input("\033[1;3;32mEnter the length of Side 2?\033[0m  "))
    question3 : float = float(input("\033[1;3;32mEnter the length of Side 3?\033[0m  "))
    
    sum_of_triangle: str = question1+question2+question3
    
    print(f"\033[1;3;32m  The perimeter of the triangle is {sum_of_triangle} \033[0m ") 
    
    
    
    
    
if __name__ == "__main__":
    main()