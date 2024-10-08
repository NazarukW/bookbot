from string import ascii_lowercase

def read_whole_book(path: str) -> str:
    with open(path, 'r') as f:
        return f.read()

def count_words(book:str) -> int:
    words_list = book.split()
    return len(words_list)

def count_letters(book: str) -> dict:
    book = book.lower()
    letters_counts_dict = {}
    for letter in ascii_lowercase:
        letters_counts_dict[letter] = book.count(letter)
    return letters_counts_dict

def main():
    frankie = read_whole_book("books/frankenstein.txt")
    print(frankie)
    frankie_words_count = count_words(frankie)
    print(f"That book has {frankie_words_count} words.")
    letters_counts_dict = count_letters(frankie)
    for letter in letters_counts_dict:
        print(f"{letter}: {letters_counts_dict[letter]}")


if __name__ == "__main__":
    main()