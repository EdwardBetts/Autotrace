
import sys
import os

if __name__ == '__main__':
	threshold = 2.9
	results = sys.argv[-1]
	
	if not os.path.isfile(results):
		print "python time_savings.py /path/to/compare/contours/results.txt"
		sys.exit(1)

	lines = open(results, 'r').readlines()[:-1] #get rid of overall average...
	scores = [float(l.strip().split(",")[-1]) for l in lines]
	to_check = [s for s in scores if s > threshold]
	print
	print "Filename: {}".format(os.path.basename(results))
	print "MSD threshold: {}".format(threshold)
	print "Total labels: {}".format(len(scores))
	print "Labels > threshold: {}".format(len(to_check))
	print "Reduction: {:.2%}".format(1-(float(len(to_check))/len(scores)))
