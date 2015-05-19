import os
import shutil
l1 = []
l2 = []
l3 = []
l4 = []
innotop = [] 
def copyqq(src, dest):
	src_files = os.listdir(src)
	dest_files = os.listdir(dest)
	for k in src_files:
		l1.append(k.split("."))
	for l in l1:
		l2.append(l[0])
	
	print l2
	for m in dest_files:
		l3.append(m.split("."))
	for n in l3:
		l4.append(n[0])
	print l4
	for i in l2:
		if i not in l4:
			innotout.append(i)
		else:
			pass
	for j in l4:
		if j not in l2:
			outnotin.append(j)
	

copyqq("/home/vagrant/1/", "/home/vagrant/2/")
