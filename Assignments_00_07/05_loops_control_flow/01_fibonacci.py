MAX_TERM_VALUE : int = 10000

def main():
    curr_term = 0  
    next_term = 1  
    while curr_term <= MAX_TERM_VALUE:
        print(f"\033[1;3;32m {curr_term} \033[0m\n")
        term_after_next = curr_term + next_term
        curr_term = next_term
        next_term = term_after_next


if __name__ == '__main__':
    main()