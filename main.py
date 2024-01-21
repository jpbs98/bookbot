def main():
    file = "books/frankenstein.txt"
    text = read_text(file)
    word_count = count_words(text)
    char_count = count_chars(text)
    report = report_char_counts(file, word_count, char_count)
    print(report)


def read_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    return text


def count_words(text):
    words = text.split()
    return len(words)


def count_chars(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def report_char_counts(file_path, word_count, char_count):
    report = ""
    report += f"--- Begin report of {file_path} ---\n"
    report += f"{word_count} words found in the document{"\n" * 3}"

    for char, count in sorted(char_count.items(), key=lambda x: x[1], reverse=True):
        if char.isalpha():
            report += f"The '{char}' character was found {count} times.\n"

    report += "--- End report ---\n"
    return report


if __name__ == "__main__":
    main()
