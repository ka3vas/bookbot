# from file_name_without_extension import function_name
import sys
from stats import count_words, count_characters, sort_dict, generate_book_report

def get_book_text(path):
	with open(path) as file:
		return file.read()

def main():
	print(len(sys.argv))
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		return sys.exit(1)
	
	path = sys.argv[1]

	text = get_book_text(path)
	num_words = count_words(text)
	sorted_char = sort_dict(count_characters(text))
	
	generate_book_report(path, num_words, sorted_char)

main()
