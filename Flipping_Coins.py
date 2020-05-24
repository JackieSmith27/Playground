from random import *


def flip_coin(x):
	h = 0
	t = 0
	for i in range(0, x):
		coin = randint(1,2)
		if coin == 1:
			h = h+1
		else:
			t =t+1
	head_average = (h/x) * 100
	tail_average = (t/x) * 100

	print(f'There were {h} heads and {t} tails.')
	print(f"Average heads:{head_average}%")
	print(f"Average heads:{tail_average}%")
