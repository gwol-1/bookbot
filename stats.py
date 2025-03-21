def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    # Create an empty dictionary
    char_count = {}
    
    # 
    for char in text:
        # Convert the character to lowercase as per instructions
        char = char.lower()
        # Check if the character is already in the dictionary
        if char in char_count:
            # If it is, increment its count
            char_count[char] += 1
        else:
            # If it's not, add it with a count of 1
            char_count[char] = 1
    
    return char_count

def sort_chars_by_count(char_dict):
    # Create a list to hold our dictionaries
    chars_list = []
    
    # Convert each key-value pair in the dictionary to a dictionary
    # and add it to our list
    for char, count in char_dict.items():
        # Create a dictionary for this character
        char_info = {"char": char, "count": count}
        chars_list.append(char_info)
    
    # Sort the list from greatest to least by count
    # Define a function to tell sort() which value to use
    def sort_on(dict):
        return dict["count"]
    
    # Sort in reverse order (greatest to least)
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list