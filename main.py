from sys import argv, exit
from stats import get_num_words, count_characters, sort_chars_by_count


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents
    
def main():
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    book_path =  argv[1] 
    book_content = get_book_text(book_path)
    word_count = get_num_words(book_content)
    char_count = count_characters(book_content)
    
    # Get the sorted list of character dictionaries
    sorted_chars = sort_chars_by_count(char_count)
    
    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Print each character and its count (if it's alphabetical)
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():  # Only print alphabetical characters
            print(f"{char}: {count}")
    
    print("============= END ===============")

main()