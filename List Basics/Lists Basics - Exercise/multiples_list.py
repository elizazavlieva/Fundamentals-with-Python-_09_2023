factor=int(input())
count = int(input())
my_list=[]
for i in range(1 , count+1):
	num= i*factor
	my_list.append(num)
print(my_list)