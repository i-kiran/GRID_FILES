import random_gen
import grid
from random_gen import generate_randno
from grid import g_file


print("Enter total no. of records : ")
r = int(input())
'''****************generate synthetic dataset*********************'''
with open("syn_set.txt" , 'w') as fd:
	for i in range(1,r+1):
		index = str(i)
		x = generate_randno()
		y = generate_randno()
		fd.write(index +','+ x +','+ y +'\n')
	fd.close()
grid = g_file()
i = 0
'''*****************read dataset and insert into the grid files*****************'''
with open('syn_set.txt', 'r') as f:
	lines = f.readlines()
	f.close()
	for l in lines:
		i+=1
		index , x , y = l.strip().split(',')
		s_no = int(index)
		x_cod= int(x)
		y_cod= int(y)
		grid.insert(s_no, x_cod , y_cod)
