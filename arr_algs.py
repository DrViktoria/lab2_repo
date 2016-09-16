arr = [5,9,1,2,45,3,8]
s=arr[0]
l= len(arr)
#print(l)
#print(s)

def min(m):
	k = m[0]
	for el in m:
		if el < k:
			k=el
	return k
			
			
			
print(min(arr))	


def arg(f):
			s=0
			for el in f:
				s+=el	
			return s/len(f) 

print(arg(arr))
