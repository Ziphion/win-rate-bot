import random
import statistics

n = 400
p = 0.1
runs = 100000

for k in range(9):
	winrates = []
	for j in range(runs):
		winsrecord = []
		for i in range(n):
			if(random.uniform(0,1) < p):
				winsrecord.append(1)
			else:
				winsrecord.append(0)
		winrates.append(sum(winsrecord)/(len(winsrecord)))

	print("Mean and Stdev, "+str(p)+":")
	print(statistics.mean(winrates))
	print(statistics.stdev(winrates))
	print("\n")

	p += 0.1
	