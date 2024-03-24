def func(*args):
	ret_values = []
	
	
	def div(num):
	    div = []
	    if (num == 1):
	        div.append(1)
	    else:
	        for i in range(1, ((num // 2) + 1)):
	            if ((num % i) == 0):
	                div.append(i)
	                if ((num // i) not in div):
	                    div.append((num // i))
	    return div
	
	def cdiv(n1, n2):
	    cd = []
	    for i in div(n1):
	        if ((i in div(n2)) and (i not in cd)):
	            cd.append(i)
	    return cd
	(wh, lh, lw) = map(int, args[0].split())
	ph = cdiv(wh, lh)
	pw = cdiv(wh, lw)
	pl = cdiv(lh, lw)
	(l, w, h) = (1, 1, 1)
	while 1:
	    if ((wh == (w * h)) and (lh == (l * h)) and (lw == (l * w))):
	        break
	    for i in ph:
	        for j in pw:
	            for k in pl:
	                if ((wh == (i * j)) and (lh == (k * i)) and (lw == (k * j))):
	                    h = i
	                    w = j
	                    l = k
	                    break
	            if ((wh == (w * h)) and (lh == (l * h)) and (lw == (l * w))):
	                break
	        if ((wh == (w * h)) and (lh == (l * h)) and (lw == (l * w))):
	            break
	ret_values.append((((l + h) + w) * 4))

	return ret_values
