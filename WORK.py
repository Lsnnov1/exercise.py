def print_upper_words(words):

    # LOOP THROUGH
    for char in words:

        # USE UPPER FUNC ON EACH CHAR
        return char.upper()
    
def printEs(words):
    # LOOP THROUGH
    for word in words:

        # USE  BUILT-IN STARTSWITH FUNC TO SEPARATE Es
        if word.startswith("e") or word.startswith("E"):

            # UPPERCASE
            print(word.upper())

def print_upper_words2(words, must_start_with):
    # FOR EACH WORD
    for word in words:

        # AND FOR EACH LETTER
        for letter in must_start_with:

            # IF THE STARTING LETTER OF WORD AND LETTER EQUALS TRUE
            if word.startswith(letter):
                
                # MATCH
                print(word.upper())
                break


print_upper_words("The", "only", "cherry", "tree")
