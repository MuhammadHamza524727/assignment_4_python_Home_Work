INCHES_IN_FOOT: int = 12

def main():
    foot:float= float(input("\033[1;3;32mEnter Foot Number:\033[0m "))
    
    totalInches:float = INCHES_IN_FOOT * foot
    
    print(f"\033[1;3;35mTotal of inches:{totalInches}\033[0m ")
    
    
if __name__ == "__main__":
    main()