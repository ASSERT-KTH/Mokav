def func(*args):
	ret_values = []
	
	
	def int_map():
	    return map(int, args[0].split(' '))
	sem = []
	for _ in range(4):
	    sem.append(list(int_map()))
	for i in range(4):
	    if ((sem[i][3] * (((((sem[i][0] + sem[i][1]) + sem[i][2]) + sem[((i + 1) % 4)][0]) + sem[((i + 2) % 4)][1]) + sem[((i + 3) % 4)][2])) != 0):
	        ret_values.append('YES')
	        exit()
	ret_values.append('NO')

	return ret_values
