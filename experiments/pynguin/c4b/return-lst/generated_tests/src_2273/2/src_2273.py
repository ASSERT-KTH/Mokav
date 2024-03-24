def func(*args):
	ret_values = []
	
	
	def main():
	    pattern = 'hello'
	    line = args[0]
	    current_letter_index = 0
	    for letter in line:
	        if (letter == pattern[current_letter_index]):
	            current_letter_index += 1
	            if (current_letter_index == 5):
	                ret_values.append('YES')
	                break
	    else:
	        ret_values.append('NO')
	if (__name__ == '__main__'):
	    main()

	return ret_values
