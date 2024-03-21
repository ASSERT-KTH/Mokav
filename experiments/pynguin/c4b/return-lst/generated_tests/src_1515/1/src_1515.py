def func(*args):
	ret_values = []
	
	text = args[0]
	j = 0
	tmp = ''
	solution = False
	flags = [True, False, False, False, False, False]
	target_chars = ['', 'h', 'e', 'l', 'l', 'o']
	searchable_chars = ['h', 'e', 'l', 'o']
	for x in text:
	    if (x in searchable_chars):
	        tmp += x
	text = tmp
	for i in range(len(text)):
	    if (flags[0] and flags[1] and flags[2] and flags[3] and flags[4]):
	        solution = True
	        break
	    elif ((text[i] == target_chars[j]) and (text[i] != 'l')):
	        continue
	    elif (text[i] == target_chars[(j + 1)]):
	        j += 1
	        flags[j] = True
	if solution:
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
