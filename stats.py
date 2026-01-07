def sorted_book_char_log(book_char_log):
    char_sorted_log = []
    for char in book_char_log:
        char_sorted_log.append({"char": char, "num": book_char_log[char]})

    char_sorted_log.sort(reverse=True, key=sort_on)
    return char_sorted_log

def sort_on(char_log):
    return char_log["num"]

def count_book_words(book_text):
    book_words_list = book_text.split()
    word_count = len(book_words_list)

    return word_count

def count_book_char_type_count(book_text):
    char_log = {}

    words_list = book_text.split()
    char_list = "".join(words_list)

    for char in char_list:
        my_char = char.lower()
        if my_char in char_log:
            char_log[my_char] = char_log[my_char] + 1
        else:
            char_log[my_char] = 1

    return char_log