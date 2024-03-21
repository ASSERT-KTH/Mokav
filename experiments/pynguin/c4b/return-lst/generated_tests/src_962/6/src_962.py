def func(*args):
	ret_values = []
	
	mat = list(map(int, args[0].split()))
	sat = [0]
	d = {}
	for i in mat:
	    if (i in d):
	        d[i] += 1
	    else:
	        d[i] = 1
	for j in d:
	    if (d[j] > 3):
	        d[j] = 3
	    if (d[j] > 1):
	        sat.append((j * d[j]))
	ret_values.append((sum(mat) - max(sat)))

	return ret_values
