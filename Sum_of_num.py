def sum_num(raw_num):
	#Adds numbers up to a given number for total
	
	#Checking to see if Number
	num = int(raw_num) 


		#adding the numbers
	sum = 0
	for x in range(0, num+1):
		sum = sum + x
		x += 1
	#Printing 0ut the log hand form
	if num >=4:
		print(f"{num} + {num-1} + ... + 1 = {sum}")
	elif num == 3:
		print(f"{num} + {num-1} = {sum}")
	elif num == 2:
		print(f"{num} + {num-1} = {sum}")
	elif num == 1 or num == 0: 
		print(f"{num} = {sum} (Really)")
	else:
		print("I wonder what went wrong. Back to the drawing board")
