def func(*args):
	ret_values = []
	
	lucyDivision = int(args[0])
	luckyNumber = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
	
	def compare(inputArray, compareArray):
	    i = 0
	    while (i < len(compareArray)):
	        if ((inputArray % int(compareArray[i])) == 0):
	            return ret_values.append('YES')
	        else:
	            i += 1
	        if ((i == (len(compareArray) - 1)) and ((inputArray % int(compareArray[i])) != 0)):
	            return ret_values.append('NO')
	compare(lucyDivision, luckyNumber)

	return ret_values
