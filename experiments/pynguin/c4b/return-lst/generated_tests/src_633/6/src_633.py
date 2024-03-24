def func(*args):
	ret_values = []
	
	
	def main():
	    (s, x) = map(int, args[0].split())
	    if (s < x):
	        ret_values.append(0)
	        return
	    (s, x) = ([(c == '1') for c in bin(int(_))[2:]] for _ in (s, x))
	    x = (([False] * (len(s) - len(x))) + x)
	    (a, b) = (([False] * len(s)), ([False] * len(s)))
	
	    def deeper(idx, carry):
	        if idx:
	            idx -= 1
	            if carry:
	                if (s[idx] == x[idx]):
	                    return
	                if s[idx]:
	                    deeper(idx, False)
	                    a[idx] = True
	                    b[idx] = True
	                    deeper(idx, True)
	                    a[idx] = False
	                    b[idx] = False
	                else:
	                    b[idx] = True
	                    deeper(idx, True)
	                    b[idx] = False
	            else:
	                if (s[idx] != x[idx]):
	                    return
	                if s[idx]:
	                    b[idx] = True
	                    deeper(idx, False)
	                    b[idx] = False
	                else:
	                    a[idx] = True
	                    b[idx] = True
	                    deeper(idx, True)
	                    a[idx] = False
	                    b[idx] = False
	                    deeper(idx, False)
	        else:
	            raise TabError
	    try:
	        deeper(len(s), False)
	    except TabError:
	        ret_values.append(((1 << (sum(b) - sum(a))) - (0 if any(a) else 2)))
	    else:
	        ret_values.append(0)
	if (__name__ == '__main__'):
	    main()

	return ret_values
