import csv
import itertools

n_itemlist = []
a = []
result = []
Mapper_list =[]
Transaction_list = []
ReverseList = []
test_dict = {}

#filename = "groceries_verysmall.csv"


#class CSVtoLIST:

def readCSV(filename):
	reader = csv.reader(open(filename, "rb"), dialect="excel")
	count = 0

	for row in reader:
		n_itemlist.append(row)
		count += 1
		#print row

	print "CREATED LIST ITEMS WITH DUPLICATES: \n", count, len(n_itemlist), n_itemlist
	return n_itemlist, count

def computeMinimumSupportCount(count):
	minsup = 0
	supcount = 0
	import math
	minsup = math.exp(-0.4*count - 0.2) + 0.2
	supcount = minsup * count / 100
	return minsup, supcount

def manyToOne(n_itemlist):
	#a=[]
	for i in range(len(n_itemlist)):
		#print i
		a.extend(n_itemlist[i])

	print "ONLY ONE LIST with duplicates: \n", len(a),a
	return a

def removeDuplicates(seq, idfun=None): 
	# order preserving
	if idfun is None:
	   def idfun(x): return x
	seen = {}
	#result = []
	for item in seq:
	   marker = idfun(item)
	   # in old Python versions:
	   # if seen.has_key(marker)
	   # but in new ones:
	   if marker in seen: continue
	   seen[marker] = 1
	   result.append(item)
	print "DUPLICATES REMOVED LIST :\n", len(result), result
	return result

	
def createDictionary(result):
	test_dict = dict(zip(result,range(1,len(result)+1)))
	print 'DICTIONARY = ',test_dict

	# for key, value in sorted(test_dict.iteritems(), key=lambda (k,v): (v,k)):
	#     print "%s: %s" % (key, value)

	for key in sorted(test_dict.iterkeys()):
	    print "%s: %s" % (key, test_dict[key])

	return test_dict


def mapper(n_itemlist,test_dict):
	#print test_dict
	#print n_itemlist
	#Mapper_list =[]
	for i in range(len(n_itemlist)):
		tem_list = []
		for j in range(len(n_itemlist[i])):
			print n_itemlist[i][j]
			#changed_list.append(n_itemlist[i][j])
			print test_dict[n_itemlist[i][j]]
			tem_list.append(test_dict[n_itemlist[i][j]])
		Mapper_list.append(tem_list)

	print "MAPPER LIST:\n",Mapper_list

	return Mapper_list


def binaryTransactionListBuilder(Mapper_list, result):
	#Transaction_list = []

	for i in range(len(Mapper_list)):
		t_list = [0 for k in range(len(result))]
		for j in range(len(Mapper_list[i])):
			#print t_list
			#print Mapper_list[i][j]
			for k in range(len(result)):
				if Mapper_list[i][j] == k+1:
					t_list.pop(Mapper_list[i][j]-1)
					t_list.insert(Mapper_list[i][j]-1,1)
					#print t_list
		Transaction_list.append(t_list)

	#print "MAPPER LIST:\n",Mapper_list
	print "Transaction_list:\n",Transaction_list
	return Transaction_list

# def reverseMapper(Mapper_list):
# 	#ReverseList = []
# 	print 'REVERSE LIST = \n', ReverseList
# 	return ReverseList

def reverseMapper(item, dict_list):
	# print 'Inside reverseMapper'
	# print 'item sent is ', item
	# print dict_list
	mapper_key = 'Null'
	for itemset in dict_list:
		#print 'Itemset = ',itemset
		if item in itemset:
			#print 'Item = ', item
			mapper_key = itemset[0]
			#print 'Mapper Key = ', mapper_key
			break
	return mapper_key






