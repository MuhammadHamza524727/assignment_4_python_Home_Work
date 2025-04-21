def main():
    
      A_Year :int= int(input("Please Enter a year:"))
      
      if A_Year % 4 :
          if A_Year % 100 == 0:
              if A_Year % 400 == 0:
                    print("\033[1;3;34m That's a leap year! \n \033[0m")
              else:
                print("That's not a leap year.")
          else:  
            print("That's a leap year!")
      else:  
        print("That's not a leap year.")
            
    
      
      
          
if __name__== "__main__":
    main()