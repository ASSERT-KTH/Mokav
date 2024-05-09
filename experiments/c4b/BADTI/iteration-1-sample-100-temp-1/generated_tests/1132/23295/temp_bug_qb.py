def original_func(*args):
	global_list = []
	
	number_division = int(args[0])
	luckynumber = []
	for number in range(1, 1001):
	    number_string = str(number)
	    index = 0
	    for digit in number_string:
	        if ((digit != '4') and (digit != '7')):
	            break
	        elif (index == (len(number_string) - 1)):
	            luckynumber.append(number)
	        index += 1
	
	def compare(arrayinput, comparenumber):
	    for item in luckynumber:
	        if ((arrayinput % item) == 0):
	            return global_list.append('YES')
	        else:
	            return global_list.append('NO')
	compare(number_division, luckynumber)
	return global_list