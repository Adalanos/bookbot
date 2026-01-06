def count_book_words(book_text):
    return len(book_text.split())

def get_book_text(path_to_file):
    file_contents = None
    with open(path_to_file) as f:
        file_contents = f.read()
    
    return file_contents

def main():
    print(f'Found {count_book_words(get_book_text("books/frankenstein.txt"))} total words')
pass

main()