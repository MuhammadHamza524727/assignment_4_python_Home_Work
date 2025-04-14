SENTENCE_START: str = "Hi😊 My name is Hamza and I am " # adjective noun verb

def main():
    # Get the three inputs from the user to make the adlib
    adjective: str = input("\033[1;3;33m Please type an adjective and press enter.\033[0m ")
    noun: str = input("\033[1;3;33m Please type a noun and press enter.\033[0m ")
    verb: str = input("\033[1;3;33m Please type a verb and press enter.\033[0m ")

    # Join the inputs together with the sentence starter
    print(f"\033[1;3;35m {SENTENCE_START} {adjective} {noun} {verb}!\033[0m")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()