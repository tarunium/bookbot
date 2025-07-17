import sys
from stats import count_words
from stats import count_chars
from stats import sort_counts

def get_book_text(filepath):
    book_text = ""
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = get_book_text(sys.argv[1])

    num_words = count_words(book)
    char_counts = count_chars(book)
    count_list = sort_counts(char_counts)

    print(f"""============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")

    for char_dict in count_list:
        if (char_dict["char"].isalpha()):
            print(f"{char_dict["char"]}: {char_dict["num"]}")

    print("============= END ===============")


main()
