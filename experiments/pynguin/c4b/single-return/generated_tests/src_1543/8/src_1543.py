def func(*args):
	
	(n, t) = map(int, args[0].split(' '))
	queue = args[1]
	people = []
	for i in queue:
	    people.append(i)
	for j in range(t):
	    i = 0
	    while (i < (n - 1)):
	        if ((people[i] == 'B') and (people[(i + 1)] == 'G')):
	            t = people[i]
	            people[i] = people[(i + 1)]
	            people[(i + 1)] = t
	            i += 2
	        else:
	            i += 1
	result = ''
	for i in people:
	    result += i
	return(result)
