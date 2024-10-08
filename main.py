def read_whole_book(path):
    with open(path, 'r') as f:
        return f.read()

def count_words(book):
    words_list = book.split()
    return len(words_list)

def main():
    frankie = read_whole_book("books/frankenstein.txt")
    print(frankie)
    frankie_words_count = count_words(frankie)
    print(frankie_words_count)


if __name__ == "__main__":
    main()