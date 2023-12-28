def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_txt(book_path)
    word_count = count_words(file_contents)
    letter_count = count_letters(file_contents)
    chars_sorted_list = chars_dict_to_sorted_list(letter_count)

    # print(file_contents)
    print(f"--- Begin report of {book_path} ---")
    print(f"There are {word_count} words in this text.")
    print()
    # print(letter_count)
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times.")
    print()
    print("--- End report ---")

def get_book_txt(path):
    with open(path) as f:
        return f.read()

def count_words(path):
    words = path.split()
    return len(words)

def count_letters(file_contents):
    letters = {}
    for words in file_contents:
        lowers = words.lower()
        if lowers in letters:
            letters[lowers] +=1
        else:
            letters[lowers] = 1
    return letters

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()