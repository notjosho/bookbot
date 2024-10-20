import re

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    get_chars(text)

def get_chars(text):
    chars_dictionary = {}
    for char in text:
        lower_case_char = char.lower()
        if lower_case_char not in chars_dictionary:
            chars_dictionary[lower_case_char] = 1
        else: 
            chars_dictionary[lower_case_char] += 1
    log_chars(chars_dictionary, get_num_words(text))

def log_chars(chars_dictionary, total_chars): 
    print('--- Begin report books/frankenstein.txt ---')
    print(f'{total_chars} words found in the document \n')
    for key, value in chars_dictionary.items():
        if key.isalpha():
            print(f"The '{key}' character was found {value} times")
    print('--- End report ---')

def get_num_words(text):
    return len(text.split())


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
