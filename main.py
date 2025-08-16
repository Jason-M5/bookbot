from stats import get_book_text
from stats import get_char_count
from stats import print_report
import sys

has_book = len(sys.argv[0:-1]) # 1 if arg input, 0 if no arg
    
if has_book != 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)    
else:
    book = sys.argv[-1]

    print(book)

# OK.. I think i just replace with open to book and download the required books.
    



def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()    
    
    a = get_book_text(file_contents)
    b = get_char_count(file_contents)
    c = print_report(a, b)


main()