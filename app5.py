# Prompts the user for a nonnegative integer that codes a set S as follows:
# - Bit 0 codes 0
# - Bit 1 codes -1
# - Bit 2 codes 1
# - Bit 3 codes -2
# - Bit 4 codes 2
# - Bit 5 codes -3
# - Bit 6 codes 3
# ...
# Computes a derived nonnegative number that codes the set of running sums
# of the members of S when those are listed in increasing order.
#
# Computes the ordered list of members of a coded set.



import sys

try:
    encoded_set = int(input('Input a nonnegative integer: '))
    if encoded_set < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
        
def display(L):
    print('{', end = '')
    print(', '.join(str(e) for e in L), end = '')
    print('}')

def decode(encoded_set):
	l = list(bin(encoded_set))
	l = l[2:]
	l = l[::-1]
	l1 = []
	if(l[0]=='1'):
		l1.append(0)
	i = 1
	j = 1
	n = 1
	while i<len(l):
		k = int(l[i])*j
		if(n==2):
			if k:
				l1.append(int(k))
			j+=1
			n = 0
		elif(i%2!=0):
			if k:
				l1.append(int(k)*-1)
		elif(n!=2 or i%2==0):
			if k:
				l1.append(int(k))
		i+=1
		n+=1
	l1 = sorted(l1)
	return l1
    # REPLACE RETURN [] ABOVE WITH YOUR CODE 
    
def code_derived_set(encoded_set):
	l = decode(encoded_set)
	l1 = []
	if(len(l)==0):
		return 0
	if(len(l)==1):
		l1.append(int(l[0]))
	else:
		l1.append(int(l[0]))
		for i in range(1,len(l)):
			k = l[i]
			for j in range(0,i):
				k+=l[j]
			l1.append(k)
	l1 = set(l1)
	k = 0
	for x in l1:
		if(x>=0):
			k += 2 ** (int(x)+int(x))
		else:
			k += 2 ** (abs(int(x))+abs(int(x))-1)
	return k

print('The encoded set is: ', end = '')
display(decode(encoded_set))
code_of_derived_set = code_derived_set(encoded_set)
print('The derived set is encoded as:', code_of_derived_set)
print('It is: ', end = '')
display(decode(code_of_derived_set))
