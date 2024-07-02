def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    chars_dict = count_char(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

    

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
    
def word_count(text):
    words = text.split()
    return len(words)

def count_char(text):
    lower_case_text = text
    char_dict = {}
    
    for letter in lower_case_text:
        lower_letter = letter.lower()
        if lower_letter in char_dict:
            char_dict[lower_letter] += 1
        else:
            char_dict[lower_letter] = 1

    return char_dict

def chars_dict_to_sorted_list(dict):
    def sort_on(dict):
        return dict["num"]
    
    sorted_list = []
    for l in dict:
        if l.isalpha():
            sorted_list.append({"char": l, "num": dict[l]})

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()
