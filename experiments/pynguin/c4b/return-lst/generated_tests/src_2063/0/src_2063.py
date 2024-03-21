def func(*args):
	ret_values = []
	
	input_str = args[0]
	first_case = True
	second_case = True
	if input_str[0].isupper():
	    second_case = False
	else:
	    first_case = False
	for letter in input_str[1:]:
	    if letter.islower():
	        first_case = False
	        second_case = False
	if first_case:
	    ret_values.append(input_str.lower())
	elif second_case:
	    ret_values.append(input_str.capitalize())
	else:
	    ret_values.append(input_str)

	return ret_values
