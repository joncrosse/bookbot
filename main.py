import sys
from stats import get_word_count
from stats import count_chars
from stats import print_report

def get_book_text(filepath):
    text = ""
    # Open the file in read mode
    with open(filepath) as f:
        text = f.read()
    return text

def main():
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    
    text = get_book_text(sys.argv[1])
    total_words = get_word_count(text)
    totals_chars = count_chars(text)
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    report = print_report(totals_chars)
    print("============= END ===============")

main()