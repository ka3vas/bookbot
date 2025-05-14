def count_words(str):
	words_list = str.split()
	return len(words_list)

def count_characters(str):
	char_count = {}

	for char in str.lower():
		if char not in char_count:
			char_count[char] = 1
		else:
			char_count[char] += 1
	
	return char_count

def sort_dict(char_dict):
	def sort_on(dict):
		return dict["num"]

	char_list = []

	for key, val in char_dict.items():
		if key.isalpha():
			char_list.append({"char": key, "num": val})

	char_list.sort(reverse=True, key=sort_on)

	return char_list

def generate_book_report(path, num_words, sorted_char):
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path}...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for char in sorted_char:
		print(f"{char['char']}: {char['num']}")
	print("============= END ===============")