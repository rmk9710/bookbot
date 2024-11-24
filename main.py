def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    chars_count = character_count(text)
    sorted_chars = sort_on(chars_count)

    print_report(num_words, sorted_chars)


def word_count(string):
    word_list = string.split()
    return(len(word_list))


def character_count(string):
    chars = {}
    for c in string:
        lowered = c.lower()
        if lowered.isalpha():
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return(chars)

def sort_on(char_dict):
    sorted_chars = sorted(char_dict.items(), key=lambda item: item[1], reverse=True)
    return sorted_chars

def print_report(num_words, sorted_chars):
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
