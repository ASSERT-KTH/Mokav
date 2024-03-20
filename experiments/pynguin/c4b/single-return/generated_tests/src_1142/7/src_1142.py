def func(*args):
	
	(n, m) = args[0].split()
	(n, m) = (int(n), int(m))
	start = 0
	count = 0
	add = [(m // 5), (m // 5), (m // 5), (m // 5), (m // 5)]
	if ((m % 5) == 1):
	    add[0] += 1
	elif ((m % 5) == 2):
	    add[0] += 1
	    add[1] += 1
	elif ((m % 5) == 3):
	    add[0] += 1
	    add[1] += 1
	    add[2] += 1
	elif ((m % 5) == 4):
	    add[0] += 1
	    add[1] += 1
	    add[2] += 1
	    add[3] += 1
	for i in range(1, (n + 1)):
	    if ((i % 5) == 1):
	        count += add[3]
	    elif ((i % 5) == 2):
	        count += add[2]
	    elif ((i % 5) == 3):
	        count += add[1]
	    elif ((i % 5) == 4):
	        count += add[0]
	    else:
	        count += add[4]
	return(int(count))
