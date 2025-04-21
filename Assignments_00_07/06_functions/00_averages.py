def average(a: float, b: float):

    sum = a + b
    return sum / 2

def main():
    average1 = average(0, 10)
    average2 = average(8, 10)
    
    final_average= average(average1, average2)
    
    print(f"average1 {average1}")
    print(f"average2 {average2}")
    print(f"final_average {final_average}")
    
    
  
    
    
    
if __name__ == "__main__":
    main()
