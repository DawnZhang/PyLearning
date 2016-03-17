from datetime import datetime

"""print("Please input your name!")
first_name = input("\tFirst Name: ")
last_name = input("\tLast Name: ")
print("\nMy name is %s %s.\n" % (first_name, last_name))"""

now = datetime.now()
print(now)
print("%s/%s/%s %s:%s:%s\n" % (now.month, now.day, now.year, now.hour, now.minute, now.second))

my_list = [1,9,3,8,5,7]
my_list.sort()
for item in my_list:
	print(item)
print()
for i in range(len(my_list)):
	print(my_list[i])
print()
	
def double_list(x):
	for i in range(len(x)):
		x[i] *= 2
	return x
		
print(double_list(my_list))
print(my_list, '\n')

phrase = "A bird in the hand..."
for char in phrase:
	if char == 'A' or char == 'a':
		print('X', end='')
	else:
		print(char, end='')		
print('\n')

choices = ['pizza', 'pasta', 'salad', 'nachos']
for index, item in enumerate(choices):
	print(index + 1, item)
	
