
for i in range(int(input())):
	n=int(input())
	a=list(map(int,input().split()))
	a.sort()
	b=[]
	for i in range(n):
		b.append(a[(2*n)-i-1])
		b.append(a[i])
	print(*b)		
					
