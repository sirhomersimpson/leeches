"""
Utils functions
"""


def generate_substrings(str1):
	
	my_substrings = []
	
	my_substrings = [str1[i:j] for i in range(len(str1)) for j in range(i+1, len(str1)+1)]
	return my_substrings


def main():
	print(generate_substrings("ab")) # Expects ['a', 'b', 'ab']
	print(generate_substrings("abc"))  # Expects ['a', 'b', 'ab']
	
	
main()
