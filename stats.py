
def get_book_text(file_contents):
    list_words = []
    list_words = file_contents.split()
    return f"Found {len(list_words)} total words"

def get_char_count(file_contents):
    chars = {}
    low = file_contents.lower()
    cnt = 0
    for l in low:
        cnt += 1 
        if l not in chars:
            chars[l] = 1
        else:
            chars[l] += 1
    return chars

def find_longest_word(file_contents, longest_word=""):
    if len(file_contents) == 0:
        return longest_word
    words = file_contents.split(maxsplit=1)
    if len(words) < 1:
        return longest_word
    first_word = words[0]
    if len(first_word) > len(longest_word):
        longest_word = first_word
    if len(words) < 2:
        return longest_word
    return find_longest_word(words[1], longest_word)



def print_report(a, b, book):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(a)
    print(" --------- Character Count -------")
    
    sorted_list = []
    for i in b:
        val = b[i]
        sorted_list.append({"char": i, "num": val})
    
    def sort_on(sorted_list):
        return sorted_list["num"]



    sorted_list.sort(reverse=True, key=sort_on)
    
    for i in sorted_list:
        if str.isalpha(i["char"]):
            print(f"{i['char']}: {i['num']}")


