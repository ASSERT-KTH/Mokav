def func(*args):
	ret_values = []
	
	string = args[0]
	AEI = 'aeiouy'
	BCD = 'bcdfghjklmnpqrstvwxz'
	i = (len(string) - 1)
	while ((string[i].lower() not in AEI) and (string[i].lower() not in BCD)):
	    i -= 1
	if (string[i].lower() in AEI):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
