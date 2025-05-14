# from file_name_without_extension import function_name
from stats import count_words, count_characters

def get_book_text(path):
	with open(path) as file:
		return file.read()

def main():
	text = get_book_text('books/frankenstein.txt')
	num_words = count_words(text)
	num_char = count_characters(text)
	print(f"{num_words} words found in the document")
	print(num_char)

main()
