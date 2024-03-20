def func(*args):
	
	
	def Digits(x):
	    ans = x
	    ls = [i for i in str(x)]
	    for i in range((len(ls) - 1), (- 1), (- 1)):
	        if (ls[i] != '0'):
	            ls[i] = str((int(ls[i]) - 1))
	            if (i != (len(ls) - 1)):
	                for i in range((i + 1), len(ls)):
	                    ls[i] = '9'
	        temp = sum(map(int, ''.join(ls)))
	        if (SumOfDigits(ans) < temp):
	            ans = Join(ls)
	    return ans
	
	def Join(ls):
	    index = 0
	    for i in range(len(ls)):
	        if (ls[i] == '0'):
	            index = i
	            break
	    return int(''.join(ls[index:len(ls)]))
	
	def SumOfDigits(n):
	    return (((n % 10) + SumOfDigits((n // 10))) if (n != 0) else 0)
	return(Digits(int(args[0])))
