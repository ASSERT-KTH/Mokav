def patched_func(*args):
	global_list = []
	
	(isa, isb, isc) = map(int, args[0].split())
	(na, nb, nc) = map(int, args[1].split())
	fa = (isa - na)
	fb = (isb - nb)
	fc = (isc - nc)
	fa = max(fa, 0)
	fb = max(fb, 0)
	fc = max(fc, 0)
	fa = (fa // 2)
	fb = (fb // 2)
	fc = (fc // 2)
	canmake = ((fa + fb) + fc)
	pa = (na - isa)
	pb = (nb - isb)
	pc = (nc - isc)
	pa = max(0, pa)
	pb = max(0, pb)
	pc = max(0, pc)
	needmake = ((pa + pb) + pc)
	if (needmake <= canmake):
	    global_list.append('Yes')
	else:
	    global_list.append('No')
	return global_list