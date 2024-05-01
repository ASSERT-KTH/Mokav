def patched_func(*args):
	global_list = []
	
	number = args[0]
	int_number = int(number)
	lucky_numbers = [4, 7]
	half_lucky_numbers = []
	
	def check(n):
	    st = False
	    for i in str(n):
	        if ((i == '4') or (i == '7')):
	            st = True
	        else:
	            st = False
	            return st
	    return st
	
	def check_hard(n):
	    for i in lucky_numbers:
	        if ((n % i) == 0):
	            return True
	    return False
	for num in range(1, (int_number + 1)):
	    easy_check = check(num)
	    if easy_check:
	        lucky_numbers.append(num)
	    else:
	        hard_check = check_hard(num)
	        if hard_check:
	            half_lucky_numbers.append(num)
	status = 'NO'
	if ((int_number in lucky_numbers) or (int_number in half_lucky_numbers)):
	    status = 'YES'
	global_list.append(status)
	return global_list