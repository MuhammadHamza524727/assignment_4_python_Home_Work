ADULT_AGE = 18  

def is_adult(age):
    if age >= ADULT_AGE:
        return True
    else:
        return False

def main():
    
    """This program is check the adult person if adult person > 18 so its return true other wise false"""
    age = int(input("\033[1;3;34m How old is this person? \033[0m \n"))
    result = is_adult(age)
    print(result)

if __name__ == "__main__":
    main()
