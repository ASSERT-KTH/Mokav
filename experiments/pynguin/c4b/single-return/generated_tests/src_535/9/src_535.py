def func(*args):
	
	
	def doubleCola(n):
	    trueVal = 0
	    subVal = 5
	    exp = 0
	    while (n > 0):
	        trueVal = n
	        n -= subVal
	        exp += 1
	        subVal = (5 * (2 ** exp))
	    exp -= 1
	    character = 0
	    while (trueVal > 0):
	        trueVal -= (2 ** exp)
	        character += 1
	    trueVal += (2 ** exp)
	    character -= 1
	    charDict = {0: 'Sheldon', 1: 'Leonard', 2: 'Penny', 3: 'Rajesh', 4: 'Howard'}
	    return charDict[character]
	return(doubleCola(int(args[0])))
