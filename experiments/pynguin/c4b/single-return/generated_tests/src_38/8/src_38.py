def func(*args):
	
	n = (int(args[0]) - 1)
	while (n > 4):
	    n = ((n - 5) // 2)
	return(['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard'][n])
