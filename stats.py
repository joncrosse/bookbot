def get_word_count(text):
    words = text.split()
    return len(words)

def count_chars(text):
    words = text.split()
    char_dict = {}
    for word in words:
        for letter in word:
            letter = letter.lower()
            if letter in char_dict:
                char_dict[letter] += 1
            else:
                char_dict[letter] = 1
    return char_dict

def sort_on(dict):
    return dict[0]

def print_report(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "count": count})

    def sort_on(dict):
        return dict["count"]
    
    char_list.sort(reverse=True, key= sort_on)

    for i in char_list:
        if i["char"].isalpha():
            
            print(f"{i["char"]}: {i["count"]}")
    return
