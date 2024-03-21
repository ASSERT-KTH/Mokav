def func(*args):
	ret_values = []
	
	import sys
	input = list(map(int, sys.stdin.readline().strip().split()))
	if (input[1] == input[0]):
	    ret_values.append('YES')
	elif ((input[2] < 0) and (input[1] <= input[0]) and ((input[1] % input[2]) == (input[0] % input[2]))):
	    ret_values.append('YES')
	elif ((input[2] > 0) and (input[1] >= input[0]) and ((input[1] % input[2]) == (input[0] % input[2]))):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
