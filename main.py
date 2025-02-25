from stats import count_words, count_char, sort_dict
import sys

def get_book_text(filepath) :
    with open(filepath) as f :
        return f.read()


def main() :
    if(len(sys.argv) < 2) :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    num_words = count_words(text)
    split_char_count = count_char(text)
    sorted_dict = sort_dict(split_char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    # Loop through the sorted list
    for char,count in sorted_dict.items():
        if char.isalpha():
            print(f"{char}: {count}")

main()