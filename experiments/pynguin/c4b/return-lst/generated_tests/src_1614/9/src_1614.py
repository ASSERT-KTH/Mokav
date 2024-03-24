def func(*args):
	ret_values = []
	
	n = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'B', 'H']
	(x, y, z) = sorted(map((lambda x: n.index(x)), args[0].split()))
	l = [x, y, z]
	for i in range(3):
	    if ((((l[((i + 2) % 3)] - l[((i + 1) % 3)]) % 12) == 3) and (((l[((i + 1) % 3)] - l[(i % 3)]) % 12) == 4)):
	        ret_values.append('major')
	        exit(0)
	    elif ((((l[((i + 2) % 3)] - l[((i + 1) % 3)]) % 12) == 4) and (((l[((i + 1) % 3)] - l[(i % 3)]) % 12) == 3)):
	        ret_values.append('minor')
	        exit(0)
	ret_values.append('strange')

	return ret_values
