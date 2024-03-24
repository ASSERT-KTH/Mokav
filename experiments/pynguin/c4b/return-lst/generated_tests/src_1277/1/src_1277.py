def func(*args):
	ret_values = []
	
	'\nCreated on Tue Apr 11 08:23:58 2017\n\n@author: lawrenceylong\n'
	a = int(args[0])
	b = list(map(int, args[1].split()))
	b.sort(reverse=True)
	count = 0
	k = 0
	yes = True
	while (count < a):
	    count += b[k]
	    k += 1
	    if (k == 12):
	        if (sum(b) < a):
	            ret_values.append((- 1))
	            yes = False
	        break
	if yes:
	    ret_values.append(k)

	return ret_values
