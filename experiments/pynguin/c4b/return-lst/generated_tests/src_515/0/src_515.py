def func(*args):
	ret_values = []
	
	iniStr = args[0]
	strLen = len(iniStr)
	ans = str()
	index = 0
	while (index < strLen):
	    theLower = iniStr[index].lower()
	    if ((theLower == 'a') or (theLower == 'e') or (theLower == 'i') or (theLower == 'o') or (theLower == 'u') or (theLower == 'y')):
	        index = (index + 1)
	        continue
	    else:
	        ans = ((ans + '.') + theLower)
	        index = (index + 1)
	ret_values.append(ans)

	return ret_values
