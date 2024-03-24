def func(*args):
	ret_values = []
	
	num = args[0]
	fours = num.count('4')
	sevens = num.count('7')
	summ = (fours + sevens)
	if ((summ == 4) or (summ == 7)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
