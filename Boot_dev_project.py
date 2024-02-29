def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    for item in book_text.split():
        if item.isnumeric():
            print(item)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()