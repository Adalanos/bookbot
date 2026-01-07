from stats import count_book_words
from stats import count_book_char_type_count
from stats import sorted_book_char_log

def sort_log(char_log):
    return char_log["num"]

def get_book_text(path_to_file):
    file_contents = None

    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = count_book_words(book_text)

    char_count = count_book_char_type_count(book_text)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    print("----------- Word Count ----------")
    print(f'Found {word_count} total words')

    print("--------- Character Count -------")
    sorted_list = sorted_book_char_log(char_count)
    for char in sorted_list:
        if char["char"].isalpha() is True:
            print(f"{char["char"]}: {char["num"]}")
pass

main()