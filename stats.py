def get_num_of_words(bookstr):
    wordlist = bookstr.split()
    wordcount = len(wordlist)
    print(f"----------- Word Count ---------- \n\n", 
    f"Found {wordcount} total words\n")


def count_characters(bookstr):
    bookstr = bookstr.lower() 
    char_count = {}

    for char in bookstr:
        if not char.isalpha():
            continue
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    sort_characters(char_count)

def sort_characters(char_count):
    characters = list(char_count.items())
    characters.sort(reverse=True, key = lambda item: item[1])
    print ("--------- Character Count -------\n")
    for char, count in characters:
        print(f"{char}: {count}")
    print("\n============= END ===============\n\n")