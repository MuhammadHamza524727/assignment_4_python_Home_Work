 
PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48
def main():
      
    vote:int= int(input("\033[1;3;34m How old are you? \n \033[0m "))
    
    if vote ==  PETURKSBOUIPO_AGE:
        print("You can vote in Peturksbouipo.\n You cannot vote in Stanlau where the voting age is 25.\nYou cannot vote in Mayengua where the voting age is 48.")    
        
    if vote == STANLAU_AGE:
        print("You can vote in Stanlau and Peturksbouipo\n You cannot vote in Mayengua where the voting age is 48.\n ") 
     
    if vote == MAYENGUA_AGE :
        print("You can vote in Mayengua where the voting age is 48.  \n and also you can vote in Peturksbouipo and Stanlau your age ise above of 16 and 25  ")         
    elif vote < 16:
        print("You can not vote any country")
if __name__ == '__main__':
    main()
    
   