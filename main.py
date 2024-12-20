def main():
    book = "books/frankenstein.txt"
    content = read_book(book)
    num_words = count_words(content)
    num_chars = count_characters(content)
    print_report(book, num_words, num_chars)


def read_book(book):
    with open(book, "r") as f:
        content = f.read()
    return content


def count_words(text):
    return len(text.split())


def count_characters(text):
    counter = {}
    for c in text.lower():
        if not c.isalpha():
            continue

        if c not in counter:
            counter[c] = 1
        else:
            counter[c] += 1
    return counter


def print_report(book, num_words, char_counter):
    print(f"--- Begin report of {book} ---")
    print(f"{num_words} words found in the document\n")

    # sort counter by char count
    sorted_char_counts = sorted(char_counter.items(), key=lambda x: x[1], reverse=True)

    for k, v in sorted_char_counts:
        print(f"The '{k}' character was found {v} times")

    print("--- End report ---")

if __name__ == '__main__':
    main()
