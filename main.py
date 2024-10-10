def read_whole_book(path: str) -> str:
    with open(path, 'r') as f:
        return f.read()

def count_words(book:str) -> int:
    words_list = book.split()
    return len(words_list)

def count_chars(book: str) -> dict:
    book = book.lower()
    chars_counts_dict = {}
    for char in book:
        if char in chars_counts_dict:
            chars_counts_dict[char] += 1
        else:
            chars_counts_dict[char] = 1
    return chars_counts_dict

def sort_letters(chars_dict: dict) -> dict:
    letters_dict = {}
    for char in chars_dict:
        if char.isalpha():
            letters_dict[char] = chars_dict[char]

    def sort_on(di):
        return di[1]

    return dict(sorted(letters_dict.items(), key=sort_on, reverse=True))

def main():
    frankie = read_whole_book("books/frankenstein.txt")
    print(frankie)
    frankie_words_count = count_words(frankie)
    print(f"That book has {frankie_words_count} words.")
    print()
    chars_counts_dict = count_chars(frankie)
    sorted_letters_dict = sort_letters(chars_counts_dict)
    for letter in sorted_letters_dict:
        print(f"The '{letter}' character was found {sorted_letters_dict[letter]} times.")



if __name__ == "__main__":
    main()