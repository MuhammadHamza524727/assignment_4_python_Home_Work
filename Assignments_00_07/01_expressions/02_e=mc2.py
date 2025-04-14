C: int = 299792458

def main():
    
    mass : float = float(input("\033[1;3;32m Enter the kilos of mass: \033[0m"))
    E: float = mass * (C ** 2)


    print(f"{E}  joules of energy!")

if __name__ == '__main__':
    main()
    
    
    
    