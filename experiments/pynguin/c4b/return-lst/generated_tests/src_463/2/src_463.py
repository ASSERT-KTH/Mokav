def func(*args):
	ret_values = []
	
	initial = args[0]
	answer = ''
	if initial.isupper():
	    answer = initial.lower()
	elif (initial[1:].isupper() or (len(initial) == 1)):
	    for i in range(0, len(initial)):
	        if (i == 0):
	            answer += initial[i].upper()
	        else:
	            answer += initial[i].lower()
	else:
	    for i in range(0, len(initial)):
	        answer += initial[i]
	ret_values.append(answer)

	return ret_values
