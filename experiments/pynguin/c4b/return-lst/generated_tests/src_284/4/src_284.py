def func(*args):
	ret_values = []
	
	s = int(args[0])
	if (((s % 47) == 0) or ((s % 74) == 0) or ((s % 44) == 0) or ((s % 77) == 0) or ((s % 4) == 0) or ((s % 7) == 0) or ((s % 444) == 0) or ((s % 777) == 0) or ((s % 447) == 0) or ((s % 774) == 0) or ((s % 474) == 0) or ((s % 477) == 0) or ((s % 747) == 0) or ((s % 744) == 0)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
