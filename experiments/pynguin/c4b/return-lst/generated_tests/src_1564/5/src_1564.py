def func(*args):
	ret_values = []
	
	from sys import stdin
	from math import log2
	n = (int(stdin.readline()) - 1)
	batch_number = int(log2(((n + 5) / 5)))
	batch_first = ((5 * (2 ** batch_number)) - 5)
	current_in_batch = (n - batch_first)
	person = int((current_in_batch / (2 ** batch_number)))
	ret_values.append(['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard'][person])

	return ret_values
