def func(*args):
	
	number = int(args[0])
	min_val = int((number / 7))
	max_val = (int((number / 4)) + 1)
	fact_num = (- 1)
	for i in range(min_val, (max_val + 1)):
	    found = False
	    for j in range((i + 1)):
	        sevens = j
	        fours = (i - j)
	        fact = ((fours * 4) + (sevens * 7))
	        if (number == fact):
	            found = True
	            fact_num = (('4' * fours) + ('7' * sevens))
	            break
	    if found:
	        break
	return(fact_num)
