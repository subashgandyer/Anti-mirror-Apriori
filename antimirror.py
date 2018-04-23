import CSVtoLIST_def as cs
import csv
import am
import utils
import sys
import time

@profile
def main():
	'''
	Usage: $ python scriptname filename.csv minsup min_confidence
	Ex: $ python testclass.py groceries_small.csv 3 0.5
	'''
	start_time = time.clock()
	n_itemlist = []
	count = 0
	a = []
	result = []
	test_dict = {}
	Mapper_list =[]
	Transaction_list = []
	ReverseList = []
	support_data = {}
	final = []
	dict_list = []
	#filename = "groceries_small.csv"
	print 'Before readCSV'
	#csvv = CSVtoLIST.readCSV()
	filename = sys.argv[1]
	minsup = int(sys.argv[2])
	min_confidence = float(sys.argv[3])	

	print 'Script Name = ', sys.argv[0], '\n', 'Filename = ', sys.argv[1], '\n', 'Minsup = ', sys.argv[2], '\n', 'Min Confidence = ', sys.argv[3]

	n_itemlist, count = cs.readCSV(filename)

	print 'Total Transactions = ', count
	# minsup, supcount = cs.computeMinimumSupportCount(count)
	# print 'MINSUP = ', minsup
	# print 'Support Count = ', supcount

	print 'After readCSV'
	a = cs.manyToOne(n_itemlist)
	result = cs.removeDuplicates(a)
	test_dict = cs.createDictionary(result)
	Mapper_list = cs.mapper(n_itemlist,test_dict)
	Transaction_list = cs.binaryTransactionListBuilder(Mapper_list, result)
	print 'DONE AND OVER'


	###########
	### NEW ADDITIONS TO THIS ALREADY WORKING PYTHON FILE
	###########



	list2 = []
	temp_list1 = []
	Transaction_list2 = []
	b = []

	#a = [[1,1,1],[0,0,0],[1,1,1],[1,1,0],[1,1,1],[0,0,0],[0,0,0],[0,0,0],[0,1,0]]
	#a3 = [[1,1,0],[0,1,0],[1,0,1],[1,1,1],[0,1,0],[1,0,1],[0,1,1],[1,1,1],[1,0,1],[1,1,0],[0,1,0],[1,1,0],[1,0,1],[0,1,1]]
	#a4 = [[1,1,1,0],[1,1,1,0],[1,1,1,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,1,0,1],[1,1,0,1],[1,0,1,0],[1,0,1,0],[1,0,1,0],[1,0,1,0],[1,0,1,0],[1,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,1],[0,0,1,1],[0,0,1,1],[0,0,1,1],[0,1,0,0],[0,1,0,0],[0,1,0,1],[0,1,0,1],[0,1,0,1],[0,1,1,1],[0,1,1,1],[0,1,1,1],[0,1,1,1],[0,0,1,0],[0,0,1,1],[0,0,1,1],[0,0,0,1],[0,0,0,1],[0,0,0,1]]
	#a5 = [[1,1,0,0,1],[1,1,0,1,0],[1,0,1,0,0],[1,0,1,0,0],[1,1,1,0,1],[1,1,1,0,0],[0,1,0,1,0],[0,1,1,0,0],[0,1,1,0,0]]
	#a_verysmall8 = [[1, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [0, 1, 0, 0, 0, 0, 1, 1]]
	#a = [[1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
	print 'Input Transactions: \n',a
	#t = a[:]
	#Transaction_list = a[:]

	Transaction_list2 = am.countTransactions(Transaction_list)
	b = am.remDupSortReverseList(Transaction_list2)
	temp_list1 = am.addCountersTransactions(b)
	not_to_be_pruned_items, to_be_pruned_items_list, list1, list2, support_data = am.antiMirroring(temp_list1,minsup)
	print ' PROGRAM OVER'
	print 'TRANSACTIONS COUNT = ', count
	print 'FINAL LIST TO BE CONSIDERED FOR RULES GENERATION = ', list2
	print 'SUPPORT DATA  :\n', support_data


	rules = am.rules_generator(list2, minsup, min_confidence, support_data)
	print 'RULES = \n', rules

	cleanRules = am.cleanRules(rules)
	print 'CLEANED RULES = \n', cleanRules


	result = am.reversed(cleanRules, final, test_dict)
	print 'Final Result :\n', result


	answer = am.formattedRules(result)
	print 'Answer :\n', answer

	print ' '
	print ' '
	print 'Association Rules \n'
	i = 1
	for items in answer:
		print i, '.',items	 
		i+=1 
		# print 'MINSUP = ', minsup
	# print 'Support Count = ', supcount
	print ' '
	print ' '
	print '---- PROGRAM OVER in %s seconds ----' % (time.clock() - start_time)

	#print("--- %s seconds ---" % (time.clock() - start_time))

if __name__ == '__main__':
    main()
