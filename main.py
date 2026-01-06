from stats import count_book_words

def get_book_text(path_to_file):
    file_contents = None

    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = count_book_words(book_text)

    print(f'Found {word_count} total words')
pass

main()