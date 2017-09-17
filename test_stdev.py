import random
import statistics

n = 2 # the program will start here and increment up to nmax
nmax = 15

w = 0  
l = n


runs = 200000

percentages = []
matches = 0

with open("output.txt", "w") as f:

	for k in range(nmax-n): 
		for j in range(n+1):
			while (matches < runs):
				winsrecord = []
				p = random.uniform(0,1) # choose a random "true" win rate
				
				for i in range(n): # simulate "n" trials of that win rate
					if(random.uniform(0,1) < p):
						winsrecord.append(1) # win
					else:
						winsrecord.append(0) # loss

				if(winsrecord.count(1) == w): 	# if the win/loss record matches the one we're looking for,
					percentages.append(p)		# add this win rate to the list of ones that matched
					matches += 1

			mean_p = statistics.mean(percentages) # once "percentages" is filled with "runs" number of p's that matched, average them
			stdev_p = statistics.stdev(percentages) # and find standard deviation
			
			print("Mean and Stdev, " + str(w) + "-" + str(l))
			print(mean_p)
			print(stdev_p)
					

			f.write(str(w)+"\t"+ str(l) + "\t" + str(mean_p) + "\t" +str(stdev_p) + "\n")
			w += 1
			l -= 1
			matches = 0
			percentages = []
		print("\n")
		f.write("\n")
		n = n+1
		w = 0
		l = n

		percentages = []
		matches = 0
		

		