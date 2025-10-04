from stats import get_book_text
from stats import get_char_count
from stats import print_report
from stats import find_longest_word
import sys

has_book = len(sys.argv[0:-1]) # 1 if arg input, 0 if no arg
    
if has_book != 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)    
else:
    book = sys.argv[-1]



def main():
    with open(book) as f:
        file_contents = f.read()
    longest_word = ""
    for line in file_contents.split("\n"):
        alphabetic_only = ''.join(
            char if char.isalpha() or char.isspace() else ' ' for char in line
            )
        long_word = find_longest_word(alphabetic_only)
        if len(long_word) >= len(longest_word):
            longest_word = long_word
    

    a = get_book_text(file_contents)
    b = get_char_count(file_contents)
    c = print_report(a, b, book)
    print(f"longest word in the book is {longest_word}")
    


main()