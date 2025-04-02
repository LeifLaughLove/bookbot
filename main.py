import sys
from stats import get_num_of_words, count_characters

def get_book_text(file_path):
    print(f"Analyzing book found at {file_path}...\n")
    with open(file_path) as f:
        return f.read()
        

def main():
    print("\n\n============ BOOKBOT ============\n")
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    bookstr = get_book_text(file_path)
    get_num_of_words(bookstr)
    count_characters(bookstr)

if __name__ == '__main__':
    main()