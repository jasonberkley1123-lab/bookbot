import sys
from stats import num_per_char
from stats import get_num_words
from stats import sorted_char_counts

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    contents = sys.argv[1]
    text = get_book_text(contents)

    num = get_num_words(text)
    print(f"Found {num} total words")

    char_counts = num_per_char(text)
    items = sorted_char_counts(char_counts)

    for item in items:
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}")

def get_book_text(books):
    with open(books) as f:
        return f.read() 


main()
