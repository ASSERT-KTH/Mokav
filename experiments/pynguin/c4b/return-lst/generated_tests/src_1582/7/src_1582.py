def func(*args):
	ret_values = []
	
	full_position = args[0]
	letter_pos = full_position[0]
	number_pos = int(full_position[1])
	if ((letter_pos != 'a') and (letter_pos != 'h')):
	    if ((number_pos != 1) and (number_pos != 8)):
	        ret_values.append(8)
	    elif ((number_pos == 1) or (number_pos == 8)):
	        ret_values.append(5)
	elif ((letter_pos == 'a') or (letter_pos == 'h')):
	    if ((number_pos == 1) or (number_pos == 8)):
	        ret_values.append(3)
	    elif ((number_pos != 1) and (number_pos != 8)):
	        ret_values.append(5)

	return ret_values
