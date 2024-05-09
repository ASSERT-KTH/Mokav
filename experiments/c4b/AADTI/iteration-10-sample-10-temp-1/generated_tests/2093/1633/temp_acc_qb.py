def patched_func(*args):
	global_list = []
	
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	string = args[0]
	numbers = string.split()
	(a, b) = (int(numbers[0]), int(numbers[1]))
	condition = ((a > 1) and (b == 1))
	if ((b > a) or condition):
	    global_list.append((- 1))
	else:
	    if (a == 1):
	        s = 'a'
	    else:
	        s = ''
	        for x in range(((a - b) + 2)):
	            s += alphabet[(x % 2)]
	        for x in range(2, b):
	            s += alphabet[x]
	    global_list.append(s)
	return global_list