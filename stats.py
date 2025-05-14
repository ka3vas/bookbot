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
