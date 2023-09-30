num= input()
my_list= num.split()
new_list=[]
for i in my_list:
	new_num=int(i)
	if new_num > 0:
		new_num *= -1
		new_list.append(new_num)
	elif new_num < 0:
		new_num=abs(new_num)
		new_list.append(new_num)
	else:
		new_list.append(new_num)
print(new_list)