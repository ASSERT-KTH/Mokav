def func(*args):
	ret_values = []
	
	'\nCreated on Mon Jun 12 23:56:29 2017\n\n@author: umang\n'
	string = args[0]
	flag = (- 1)
	count = {i: [] for i in 'helo'}
	for i in range(len(string)):
	    if (string[i] in count.keys()):
	        count[string[i]].append(i)
	    if ((len(count['h']) >= 1) and (len(count['e']) >= 1) and (len(count['l']) >= 2) and (len(count['o']) >= 1)):
	        minh = min(count['h'])
	        inde = (- 1)
	        for j in sorted(count['e']):
	            if (j > minh):
	                inde = j
	                break
	        l1ind = (- 1)
	        l2ind = (- 1)
	        temp = []
	        for j in sorted(count['l']):
	            if (j > inde):
	                l1ind = j
	                break
	        temp = list(count['l'])
	        try:
	            temp.remove(l1ind)
	        except:
	            pass
	        for j in sorted(temp):
	            if (j > l1ind):
	                l2ind = j
	                break
	        oind = (- 1)
	        for j in sorted(count['o']):
	            if (j > l2ind):
	                oind = j
	                break
	        if (minh < inde < l1ind < l2ind < oind):
	            ret_values.append('YES')
	            flag += 1
	            break
	if (flag < 0):
	    ret_values.append('NO')

	return ret_values
