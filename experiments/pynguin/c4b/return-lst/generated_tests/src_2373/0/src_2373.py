def func(*args):
	ret_values = []
	
	
	def Boy():
	    s = args[0].lower()
	    l = len(s)
	    k = s[0]
	    i = 0
	    while (i < l):
	        flag = 1
	        if (len(k) == 0):
	            k = s[i]
	        else:
	            j = 0
	            while ((j < len(k)) and (flag != 0)):
	                if (s[i] != k[j]):
	                    flag = (flag + 1)
	                else:
	                    flag = 0
	                j = (j + 1)
	        if (flag != 0):
	            k = (k + s[i])
	        i = (i + 1)
	    r = len(k)
	    if ((r % 2) != 0):
	        ret_values.append('IGNORE HIM!')
	    else:
	        ret_values.append('CHAT WITH HER!')
	Boy()

	return ret_values
