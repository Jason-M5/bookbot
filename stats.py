
def get_book_text(file_contents):
    list_words = []
    #with open("books/frankenstein.txt") as f:
     #   file_contents = f.read()
    list_words = file_contents.split()
    #num_words = 0
    return f"Found {len(list_words)} total words"

def get_char_count(file_contents):
    chars = {}
    #with open("books/frankenstein.txt") as f:
    #    file_contents = f.read()
    low = file_contents.lower()
        #print(low)
    cnt = 0
    for l in low:
        cnt += 1 
        if l not in chars:
            chars[l] = 1
        else:
            chars[l] += 1
    #print(chars)
    return chars



def print_report(a, b):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
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

                  
    
    
    
    
    #b.sort(reverse=True, key=sort_on)
    
    
    #for char in chars:
     #   print(char)





#get_book_text()
#get_char_count()
#print_report()


