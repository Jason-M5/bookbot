
def get_book_text():
    list_words = []
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        list_words = file_contents.split()
        num_words = 0
        print(f"{len(list_words)} words found in the document")

def get_char_count():
    chars = {}
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        low = file_contents.lower()
        #print(low)
        cnt = 0
        for l in low:
            cnt += 1 
            if l not in chars:
                chars[l] = 1
            else:
                chars[l] += 1
        print(chars)

#get_char_count()
#get_book_text()
