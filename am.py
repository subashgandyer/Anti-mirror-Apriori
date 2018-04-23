import itertools
from utils import itemsets_generation as ig
from memory_profiler import profile
import CSVtoLIST_def as cs



#import CSVtoLIST


"""from collections import Counter

a = [[1, 1, 0, 0, 1], [0, 1, 0, 1, 0], [0, 1, 1, 0, 0], [1, 1, 0, 1, 0], [1, 0, 1, 0, 0], [0, 1, 1, 0, 0], [1, 0, 1, 0, 0], [1, 1, 1, 0, 1], [1, 1, 1, 0, 0]]
b_set = set(map(tuple,a))  #need to convert the inner lists to tuples so they are hashable
b = map(list,b_set) #Now convert tuples back into lists (maybe unnecessary?)
print a
print b

# for i in range(len(a)):
# 	#print len(a)
# 	cnt = 0
# 	for item in a[i]:
# 		if item == 1:
# 			cnt += 1
# 	print cnt
# print a


import itertools, time


class Timer(object):
    def __init__(self, name=None):
        self.name = name

    def __enter__(self):
        self.tstart = time.time()

    def __exit__(self, type, value, traceback):
        if self.name:
            print '[%s]' % self.name,
        print 'Elapsed: %s' % (time.time() - self.tstart)


k = [[1, 2], [4], [5, 6, 2], [1, 2], [3], [5, 2], [6], [8], [9]] * 5
N = 100000

print len(k)

with Timer('set'):
    for i in xrange(N):
        kt = [tuple(i) for i in k]
        skt = set(kt)
        kk = [list(i) for i in skt]


with Timer('sort'):
    for i in xrange(N):
        ks = sorted(k)
        dedup = [ks[i] for i in xrange(len(ks)) if i == 0 or ks[i] != ks[i-1]]


with Timer('groupby'):
    for i in xrange(N):
        k = sorted(k)
        dedup = list(k for k, _ in itertools.groupby(k))

with Timer('loop in'):
    for i in xrange(N):
        new_k = []
        for elem in k:
            if elem not in new_k:
                new_k.append(elem)

my_list = [3, 5, 2, 1, 4, 4, 1]
print my_list
my_list.sort()
for i in range(0,len(my_list)-1):
               if my_list[i] == my_list[i+1]:
                   print str(my_list[i]) + ' is a duplicate'

"""

#temp_lista = [[1, 1, 1, 2, 0], [1, 1, 0, 3, 0], [1, 1, 0, 2, 0],[1, 0, 1, 4, 0], [1, 0, 1, 0, 3], [1, 0, 0, 0, 2]]
#temp_list6 =  [[1, 1, 1, 1, 3, 0], [1, 1, 1, 0, 3, 0], [1, 1, 0, 1, 2, 0], [1, 0, 1, 0, 5, 0], [1, 0, 0, 0, 4, 0], [1, 0, 0, 0, 0, 4], [1, 0, 1, 0, 0, 3], [1, 0, 1, 1, 0, 2], [1, 1, 0, 0, 0, 6], [1, 1, 0, 1, 0, 1], [1, 1, 1, 0, 0, 3]]
#temp_list5 = [[1,1,0,0,1],[1,1,0,1,0],[1,0,1,0,0],[1,0,1,0,0],[1,1,1,0,1],[1,1,1,0,0],[0,1,0,1,0],[0,1,1,0,0],[0,1,1,0,0]]
#verysmall_temp_list = [[1, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [0, 1, 0, 0, 0, 0, 1, 1]]



def countTransactions(Transaction_list):
	""" A list like the following
				[
				[1,1,1],
				[0,0,0],
				[1,1,1],
				[1,1,0],
				[1,1,1]
				]
			should be converted to a list without any duplicates and
			count of each list should be appended to the list items

			[
			[1, 1, 0, 1], 
			[0, 0, 0, 1], 
			[1, 1, 1, 3]
			]
			The last element in each list is the Count of its occurence.
	"""
	#Appending count to the list
	t = Transaction_list[:]
	for i in range(len(t)):
		#print 'len = ',len(t)
		c = t.count(t[i])
		#print 'count of ',t[i], ' = ',c
		# d = a.index(a[i])
		# print d
		#yy = a[i]
		Transaction_list[i] = Transaction_list[i] + [c]  # important, do not use append
		#if c > 1:
			#print ''
			#print 'High count > 1'
		#print a
		
	#print 't = ', t
	print 'a after appending count with duplicates = \n', Transaction_list

	return Transaction_list
	
def remDupSortReverseList(Transaction_list2):
	"""Removes Duplicates from the list
		Parameters :
		----------

			Transaction_list2 :   Transaction List with duplicates involved

		Returns 

			b :  List with duplicates removed
	"""

	#print 'Inside remDupSortReverseList \n ',Transaction_list2
	b = map(list, set(map(tuple, Transaction_list2)))	#Removing Duplicates from the list
	print 'Duplicates are removed \n', b
	y = b[:]
	b.sort()	#Sorting the list
	print 'Sorted List is \n', b
	b.reverse() #Reversing the list
	print 'Reversed List is \n', b
	y = b[:]	#Taking a copy of the reversed working list
	#print 'y is : ', y

	return b


def addCountersTransactions(b):
	"""Step 2 : The above list with count as the last element should be 
					[
					[1, 1, 0, 1], 
					[0, 0, 0, 4], 
					[1, 1, 1, 3]
					]
			converted to the following way

					[
					[1, 1, 0, 1, 0], 
					 
					[1, 1, 1, 3, 4]
					]
			with cnt 1 and cnt 2 for anti-mirroring technique

			Algorithm
			=========
			Check for the first element in the listitem.
			If it is 1, 
				cnt2 = 0
			If it is 0,
				Not the values of the list except the last item (count)
				Check the Not valued list is matching with existing 1valued list
				If it is matching,
					then add the last count to cnt2 of that matched list
				else
					add a new entry with last count as cnt2 and cnt1 as 0

	"""
	# n = list(b)
	# x = b[:]

	# cnt1 = []
	# cnt2 = []
	temp_list2 = []
	t1list = []
	zlist = []
	for i in range(len(b)):
		#print b[i], b[i][0]
		if b[i][0] == 1:
			b[i] = b[i] + [0]
			#adding this list item to another list
			zlist = remove_counts(b[i],t1list)
			#print 'zlist = ',zlist 
			temp_list2.append(b[i])
			#print 'temp_list appended ', temp_list
			#print b
		if b[i][0] == 0:
			#print 'Found an item that starts with 0'
			for item in range(len(b[i])):
				#print b[i][item],i,item, len(b[i])
				if b[i][item] == 0:
					#print 'Found a 0 item, change it to 1'
					b[i][item] = 1
				else:
					#print 'Found a 1 item, change it to 0'
					if item != len(b[i])-1:
						#print 'Not the last element, so it is changed here (NOT)'
						b[i][item] = 0
					else:
						b[i] = b[i] + [b[i][item]]
						b[i][item] = 0
						#print 'Changed cos'
						
				#print 'Present list item inside loop is ', b[i]
			#print 'Present list item is ', b[i]
			temp = b[i]
			#print temp
			tlist = []
			
			telist = remove_counts(temp,tlist)
			temp_list2.append(b[i])
			#########print 'temp_list appended \n', temp_list2
			#print 'telist = ',telist
			#print 'y is ', y

			# if telist in temp_list2:

			# 	print 'HEY FOUND HIM'
			# 	#b[i] = b[i] + [b[i][item]]
			# else:
			# 	print'Else not found'

	return temp_list2
				

	'''Step 3:  Do {I1} {I2} and {In}
				Then check for support and prune the list
				Do the above step for all the subsets and prune with support
				To compute {I1}, {I2}, ... {In}
					1. For loop i to len(items) 
					2. Check for ith item in lists,
							If it is 1, 
								Sum up Cnt1 and put it in Ii
							If it is 0,
								Sum up Cnt2 and put it in Ii
					2. Print all Ii's
	'''

	
def antiMirroring(temp_list, minsup):	

	"""

	Computes the antimirroring algorithm 

	Parameters :
	----------

		temp_list : List as list
		minsup : minimum support count as number

	Returns
		not_to_be_pruned_items :  To be used list
		to_be_pruned_items_list : List with the itemsets to be pruned
		list1 : List one
		list2 : List Two
		support_data : Dictionary of Not_to_be_pruned_items with support count
	"""

	not_to_be_pruned_items = []
	to_be_pruned_items_list = []
	cnt = 0
	list1 = []
	list2 = []
	ilist = []
	support_data = {}
	l = len(temp_list[0]) - 2
	#print 'length = ', l
	for i in range(l):
		#print 'list item = ', temp_list[i], 'len = ',l
		cnt = 0
		for y in range(len(temp_list)):
			#print 'y=',y
			if temp_list[y][i] == 1:
				#print 'temp_list[y][i]= ',temp_list[y][i]
				cnt = cnt + temp_list[y][len(temp_list[0])-2]
				#print cnt
			elif temp_list[y][i] == 0:
				cnt = cnt + temp_list[y][len(temp_list[0])-1]
				#print cnt
		##################print 'I%d = %d'%(i+1,cnt)
		if cnt >= minsup:
			################print ' Min Support Count established '
			not_to_be_pruned_items.append(i+1)
			support_data[i+1] = cnt
		else:
			##############print 'No min support attained'
			to_be_pruned_items_list.append(i+1)
			#support_data[i+1] = cnt

		list1.append(cnt)
	print '1-item sets check : \n', list1
	print 'Not to be pruned itemsets   \n ',not_to_be_pruned_items 
	print 'To be pruned itemsets   \n ', to_be_pruned_items_list 
	print 'Support Data    \n',  support_data 


	print ' '
	print ' '
	print ' '
	print ' Length of Not to be pruned items = ', len(not_to_be_pruned_items), type(not_to_be_pruned_items)

	if len(not_to_be_pruned_items) != 0:
		print 'Itemsets generated are as follows: '
		ilist, list2, support_data = subsets_generator(temp_list,to_be_pruned_items_list,not_to_be_pruned_items,minsup, support_data)
		#print list2
		#print 'NEWWWWWWW printing ilist = \n', ilist

	print 'Outside Outside List Empty check and It is empty now and PROGRAM OVER !!!!'
	#print 'NEWWWWWWW printing ilist = \n', ilist


	return not_to_be_pruned_items, to_be_pruned_items_list, list1, list2, support_data

#### COMMENTED MAIN DUE TO SOME CONFLICTS

# def main():

# 	temp_list = [[1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
# 	list2 = []
# 	temp_list1 = []
# 	Transaction_list2 = []
# 	minsup = 3	
# 	#a = [[1,1,1],[0,0,0],[1,1,1],[1,1,0],[1,1,1],[0,0,0],[0,0,0],[0,0,0],[0,1,0]]
# 	#a3 = [[1,1,0],[0,1,0],[1,0,1],[1,1,1],[0,1,0],[1,0,1],[0,1,1],[1,1,1],[1,0,1],[1,1,0],[0,1,0],[1,1,0],[1,0,1],[0,1,1]]
# 	#a4 = [[1,1,1,0],[1,1,1,0],[1,1,1,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,1,0,1],[1,1,0,1],[1,0,1,0],[1,0,1,0],[1,0,1,0],[1,0,1,0],[1,0,1,0],[1,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,1],[0,0,1,1],[0,0,1,1],[0,0,1,1],[0,1,0,0],[0,1,0,0],[0,1,0,1],[0,1,0,1],[0,1,0,1],[0,1,1,1],[0,1,1,1],[0,1,1,1],[0,1,1,1],[0,0,1,0],[0,0,1,1],[0,0,1,1],[0,0,0,1],[0,0,0,1],[0,0,0,1]]
# 	#a5 = [[1,1,0,0,1],[1,1,0,1,0],[1,0,1,0,0],[1,0,1,0,0],[1,1,1,0,1],[1,1,1,0,0],[0,1,0,1,0],[0,1,1,0,0],[0,1,1,0,0]]
# 	#a_verysmall8 = [[1, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [0, 1, 0, 0, 0, 0, 1, 1]]
# 	a = [[1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
# 	print 'Input Transactions: \n',a
# 	t = a[:]
# 	Transaction_list = a[:]

# 	Transaction_list2 = countTransactions(Transaction_list)
# 	b = remDupSortReverseList(Transaction_list2)
# 	temp_list1 = addCountersTransactions(b)
# 	not_to_be_pruned_items, to_be_pruned_items_list, list1, list2 = antiMirroring(temp_list1,minsup)
# 	print 'OVER'
# 	''' Length of the Items is found out.
# 		Now, find the subsets of items.
# 	'''
	
 
# 	# print ' '
# 	# print ' '
# 	# print ' '
# 	# print ' Length of Not to be pruned items = ', len(not_to_be_pruned_items), type(not_to_be_pruned_items)

# 	# if len(not_to_be_pruned_items) != 0:
# 	# 	print 'Itemsets generated are as follows: '
# 	# 	list2 = subsets_generator(temp_list,to_be_pruned_items_list,not_to_be_pruned_items,minsup)
# 	# 	#print list2


# 	# print 'Outside List Empty check and It is empty now and PROGRAM OVER !!!!'
	
	




# def reverseMapper(Mapper_list, ):
# 	print 'DOES NOTHING'
# 	return 1


def tester(fulltemplate, template, no_of_items):
	if no_of_items == 2:
		condtn_string = template
		print condtn_string
	else:
		for x in range(no_of_items-1):
			condtn_string = fulltemplate + (template * x)
			print condtn_string

def subsets_generator1(temp_list,to_be_pruned_items_list,not_to_be_pruned_items):
	#to_be_pruned_items_list = []
	no_of_items = len(temp_list[0]) - 2
	print 'Finding out no_of_items from passing temp_list as argument = ',no_of_items
	list1 = [i+1 for i in range(no_of_items)]
	print 'LIST 1 =', list1, (list1)
	print 'Length of Temp_list = ', len(temp_list[0])
	cnt = 2
	while cnt <= (len(temp_list[0]) - 2) and len(not_to_be_pruned_items)!=0 :
		if len(not_to_be_pruned_items) != 0:
			print ' Length of Not to be pruned items = ', len(not_to_be_pruned_items)
			print len(temp_list[0]) - 2
			print 'Inside subsets_generator function and CNT is ', cnt
			list2 = list(itertools.combinations(list1, cnt))
			print 'LIST TO BE USED IS : ', list2

			list3 = prune_itemsets(list2,to_be_pruned_items_list)
			print 'PRUNED LIST IS : \n', list3
			nlist, to_be_pruned_items_list,not_to_be_pruned_items = ig(list3, temp_list,cnt,to_be_pruned_items_list,minsup)
			print 'nlist = ', nlist, '\n', 'to_be_pruned_items_list = \n',to_be_pruned_items_list
			#no_of_items = no_of_items + 1
			print 'subesets are generated quite successfully ................'
			
			cnt = cnt + 1
		else:
			break
	return list2

def subsets_generator_working(temp_list,to_be_pruned_items_list,not_to_be_pruned_items):
	#to_be_pruned_items_list = []
	no_of_items = len(temp_list[0]) - 2
	print 'Finding out no_of_items from passing temp_list as argument = ',no_of_items
	#list1 = [i+1 for i in range(no_of_items)]
	
	print 'NOT TO BE PRUNED LIST =  ', not_to_be_pruned_items, type(not_to_be_pruned_items)
	print 'Length of Temp_list = ', len(temp_list[0])
	cnt = 2
	while cnt <= (len(temp_list[0]) - 2) and len(not_to_be_pruned_items)!=0 :
		if len(not_to_be_pruned_items) != 0:
			print ' Length of Not to be pruned items = ', len(not_to_be_pruned_items)
			print len(temp_list[0]) - 2
			print 'Inside subsets_generator function and CNT is ', cnt
			print 'NOT TO BE PRUNED LIST =  ', not_to_be_pruned_items
			# Removing duplicates from pruned list
			if cnt >=3:
				z = []
				for k in range(len(not_to_be_pruned_items)):
					print k
					print not_to_be_pruned_items[k]
					z.extend(not_to_be_pruned_items[k])

				print 'BEFORE REMOVAL OF DUPLICATES z = ', z
				z1 = uniqify(z)
				print 'AFTER REMOVAL OF DUPLICATES z1 = ', z1
				z1.sort()
				print 'AFTER SORTING = ', z1
				not_to_be_pruned_items = z1

			list2 = list(itertools.combinations(not_to_be_pruned_items, cnt))
			print 'LIST TO BE USED IS : ', list2

			# list3 = prune_itemsets(list2,to_be_pruned_items_list)
			# print 'PRUNED LIST IS : \n', list3
			nlist, to_be_pruned_items_list,not_to_be_pruned_items = ig(list2, temp_list,cnt,to_be_pruned_items_list,minsup)
			#print 'nlist = ', nlist, '\n', 'to_be_pruned_items_list = \n',to_be_pruned_items_list
			#no_of_items = no_of_items + 1
			print 'subsets are generated quite successfully ................'
			
			cnt = cnt + 1
		else:
			break
	return list2

def subsets_generator(temp_list,to_be_pruned_items_list,not_to_be_pruned_items,minsup, support_data):
	#to_be_pruned_items_list = []
	no_of_items = len(temp_list[0]) - 2
	#print 'Finding out no_of_items from passing temp_list as argument = ',no_of_items
	#list1 = [i+1 for i in range(no_of_items)]
	
	#print 'NOT TO BE PRUNED LIST =  ', not_to_be_pruned_items, type(not_to_be_pruned_items)
	#print 'Length of Temp_list = ', len(temp_list[0]), type(temp_list)
	cnt = 2
	ilist = []
	while cnt <= (len(temp_list[0]) - 2) and len(not_to_be_pruned_items)!=0 :
		if len(not_to_be_pruned_items) != 0:
			#print ' Length of Not to be pruned items = ', len(not_to_be_pruned_items)
			#print len(temp_list[0]) - 2
			print 'Inside Inside Inside Inside subsets_generator function and CNT is ', cnt
			print ' '
			print ' '
			print 'NOT TO BE PRUNED LIST =  ', not_to_be_pruned_items
			# Removing duplicates from pruned list
			if cnt >=3:
				z = []
				for k in range(len(not_to_be_pruned_items)):
					#print k
					#print not_to_be_pruned_items[k]
					z.extend(not_to_be_pruned_items[k])

				print 'BEFORE REMOVAL OF DUPLICATES z = ', z
				z1 = uniqify(z)
				print 'AFTER REMOVAL OF DUPLICATES z1 = ', z1
				z1.sort()
				print 'AFTER SORTING = ', z1
				not_to_be_pruned_items = z1
				print 'LENGTH OF PRUNED LIST = ', len(z1)
			if len(not_to_be_pruned_items) < cnt:
				print 'No more further iterations'
				list2 = not_to_be_pruned_items
				print 'FINAL LIST IS = ', list2
				break
			else:
				list2 = list(itertools.combinations(not_to_be_pruned_items, cnt))
				print 'LIST TO BE USED IS : ', list2

				# list3 = prune_itemsets(list2,to_be_pruned_items_list)
				# print 'PRUNED LIST IS : \n', list3
				support_data, nlist, to_be_pruned_items_list,not_to_be_pruned_items = ig(list2, temp_list,cnt,to_be_pruned_items_list,minsup, support_data)
				#print 'nlist = ', nlist, '\n', 'to_be_pruned_items_list = \n',to_be_pruned_items_list
				#no_of_items = no_of_items + 1
				print 'subsets are generated quite successfully ................'
				print 'SUpport Data   :', support_data
				ilist.append(nlist)
			cnt = cnt + 1
		else:
			break

	return ilist, list2 , support_data

def remove_counts(temp,tlist):
	for i in range(len(temp)):
		#print temp[i], len(temp), i
		if i != len(temp) - 1:
			tlist.append(temp[i])
		#print 'tlist = ',tlist
	return tlist


def uniqify(seq, idfun=None): 
   # order preserving
   if idfun is None:
       def idfun(x): return x
   seen = {}
   result = []
   for item in seq:
       marker = idfun(item)
       # in old Python versions:
       # if seen.has_key(marker)
       # but in new ones:
       if marker in seen: continue
       seen[marker] = 1
       result.append(item)
   return result

def old_prune_itemsets(list2,to_be_pruned_items):
	for item in range(len(list2)):
		for pruned_item in to_be_pruned_items:
			if pruned_item in list2[item]:
				print 'Found'
			else:
				print 'Not Found'

def prune_itemsets(y, to_be_pruned_items):
	for item in to_be_pruned_items:
		y = [s for s in y if item not in s]
	return y

def rules_from_conseq(freq_set, H, support_data, rules, min_confidence=0.5, verbose=False):
    """Generates a set of candidate rules.

    Parameters
    ----------
    freq_set : frozenset
        The complete list of frequent itemsets.

    H : list
        A list of frequent itemsets (of a particular length).

    support_data : dict
        The support data for all candidate itemsets.

    rules : list
        A potentially incomplete set of candidate rules above the minimum 
        confidence threshold.

    min_confidence : float
        The minimum confidence threshold. Defaults to 0.5.
    """
    m = len(H[0])
    if m == 1:
        Hmp1 = calc_confidence(freq_set, H, support_data, rules, min_confidence, verbose)
    if (len(freq_set) > (m+1)):
        Hmp1 = apriori_gen(H, m+1) # generate candidate itemsets
        Hmp1 = calc_confidence(freq_set, Hmp1, support_data, rules, min_confidence, verbose)
        if len(Hmp1) > 1:
            # If there are candidate rules above the minimum confidence 
            # threshold, recurse on the list of these candidate rules.
            rules_from_conseq(freq_set, Hmp1, support_data, rules, min_confidence, verbose)

def calc_confidence(freq_set, H, support_data, rules, min_confidence=0.5, verbose=False):
    """Evaluates the generated rules.

    One measurement for quantifying the goodness of association rules is 
    confidence. The confidence for a rule 'P implies H' (P -> H) is defined as 
    the support for P and H divided by the support for P 
    (support (P|H) / support(P)), where the | symbol denotes the set union 
    (thus P|H means all the items in set P or in set H).

    To calculate the confidence, we iterate through the frequent itemsets and 
    associated support data. For each frequent itemset, we divide the support 
    of the itemset by the support of the antecedent (left-hand-side of the 
    rule).

    Parameters
    ----------
    freq_set : frozenset
        The complete list of frequent itemsets.

    H : list
        A list of frequent itemsets (of a particular length).

    min_support : float
        The minimum support threshold.

    rules : list
        A potentially incomplete set of candidate rules above the minimum 
        confidence threshold.

    min_confidence : float
        The minimum confidence threshold. Defaults to 0.5.

    Returns
    -------
    pruned_H : list
        The list of candidate rules above the minimum confidence threshold.
    """
    pruned_H = [] # list of candidate rules above the minimum confidence threshold
    for conseq in H: # iterate over the frequent itemsets
        conf = support_data[freq_set] / support_data[freq_set - conseq]
        if conf >= min_confidence:
            rules.append((freq_set - conseq, conseq, conf))
            pruned_H.append(conseq)

            if verbose:
                print("" \
                    + "{" \
                    + "".join([str(i) + ", " for i in iter(freq_set-conseq)]).rstrip(', ') \
                    + "}" \
                    + " ---> " \
                    + "{" \
                    + "".join([str(i) + ", " for i in iter(conseq)]).rstrip(', ') \
                    + "}" \
                    + ":  conf = " + str(round(conf, 3)) \
                    + ", sup = " + str(round(support_data[freq_set], 3)))

    return pruned_H

def generate_rules(F, support_data, min_confidence=0.5, verbose=True):
    """Generates a set of candidate rules from a list of frequent itemsets.

    For each frequent itemset, we calculate the confidence of using a
    particular item as the rule consequent (right-hand-side of the rule). By 
    testing and merging the remaining rules, we recursively create a list of 
    pruned rules.

    Parameters
    ----------
    F : list
        A list of frequent itemsets.

    support_data : dict
        The corresponding support data for the frequent itemsets (L).

    min_confidence : float
        The minimum confidence threshold. Defaults to 0.5.

    Returns
    -------
    rules : list
        The list of candidate rules above the minimum confidence threshold.
    """
    rules = []
    for i in range(1, len(F)):
        for freq_set in F[i]:
            H1 = [frozenset([itemset]) for itemset in freq_set]
            if (i > 1):
                rules_from_conseq(freq_set, H1, support_data, rules, min_confidence, verbose)
            else:
                calc_confidence(freq_set, H1, support_data, rules, min_confidence, verbose)

    return rules


def rules_generator(list2, minsup, min_confidence, support_data):
	rules = []
	i=0
	counter = 0
	# for itemset in list2:
	# 	for i in range(len(itemset)):
	# 		print itemset[i]
	list2 = tuple(list2)
	# for i in len(list2):
	# 	counter += 1
	# 	print counter
	for itemset in list2:
		print 'ITEMSET, type, len of list2 :',itemset, type(itemset), len(list2)
		if type(itemset) is int:
			print'Caught the exceptional case with 1 tuple'
			print'Need to write the special case for this'
			print list2
			if len(list2) == 4:
				for i in range(len(list2)):
					print (list2[i],list2[i-3],list2[i-2]),'--->',(list2[i-1])
					#print float(support_data[list2])
					#print float(support_data[(list2[i],list2[i-2])])
					if list2 not in support_data:
						a = 0.0
					else:
						a = float(support_data[list2])
						print 'a = ', float(support_data[list2])
					if (list2[i],list2[i-3],list2[i-2]) in support_data:
						#print 'Found'
						print 'b = ', float(support_data[(list2[i],list2[i-3],list2[i-2])])
						b = float(support_data[(list2[i],list2[i-3],list2[i-2])])
					elif (list2[i],list2[i-2],list2[i-3]) in support_data:
						print 'b = ', float(support_data[(list2[i],list2[i-2],list2[i-3])])
						b = float(support_data[(list2[i],list2[i-2],list2[i-3])])
					elif (list2[i-3],list2[i-2],list2[i]) in support_data:
						print 'b = ', float(support_data[(list2[i-3],list2[i-2],list2[i])])
						b = float(support_data[(list2[i-3],list2[i-2],list2[i])])
					elif (list2[i-3],list2[i],list2[i-2]) in support_data:
						print 'b = ', float(support_data[(list2[i-3],list2[i],list2[i-2])])
						b = float(support_data[(list2[i-3],list2[i],list2[i-2])])
					elif (list2[i-2],list2[i],list2[i-3]) in support_data:
						print 'b = ', float(support_data[(list2[i-2],list2[i],list2[i-3])])
						b = float(support_data[(list2[i-2],list2[i],list2[i-3])])
					else:
						print 'b = ', float(support_data[(list2[i-2],list2[i-3],list2[i])])
						b = float(support_data[(list2[i-2],list2[i-3],list2[i])])
					
					d = float(support_data[list2[i-1]])
					try:
						c = a/b
						print 'c = ', c
					except:
						print 'Division by Zero error'
					finally:
						print ' '
						if c >= min_confidence:
							rules.append(list2[i])
							rules.append(list2[i-3])
							rules.append(list2[i-2])
							rules.append('--->')
							rules.append(list2[i-1])
							rules.append(c)	
							rules.append('|')
						e = a/d
						print 'e = ', e
						if e >= min_confidence:
							rules.append(list2[i-1])
							rules.append('--->')
							rules.append(list2[i])
							rules.append(list2[i-3])
							rules.append(list2[i-2])
							rules.append(e)
							rules.append('|')

						print 'a = ', float(support_data[list2])
						a = float(support_data[list2])
						if (list2[i],list2[i-3]) in support_data:
							print 'b = ', float(support_data[(list2[i],list2[i-3])])
							b = float(support_data[(list2[i],list2[i-3])])
						else:
							print 'b = ', float(support_data[(list2[i-3],list2[i])])
							b = float(support_data[(list2[i-3],list2[i])])

						try:
							c = a/b
							print 'c = ', c
						except:
							print 'Division by Zero error'
						finally:
							print ' '
							if c >= min_confidence:
								rules.append(list2[i])
								rules.append(list2[i-3])
								rules.append('--->')
								rules.append(list2[i-2])
								rules.append(list2[i-1])
								rules.append(c)
								rules.append('|')
				break
			if len(list2) == 3:
				for i in range(len(list2)):
					print (list2[i],list2[i-2]),'--->',(list2[i-1])
					#print float(support_data[list2])
					#print float(support_data[(list2[i],list2[i-2])])
					if list2 not in support_data:
						a = 0.0
					else:
						a = float(support_data[list2])
						print 'a = ', float(support_data[list2])
					if (list2[i],list2[i-2]) in support_data:
						#print 'Found'
						print 'b = ', float(support_data[(list2[i],list2[i-2])])
						b = float(support_data[(list2[i],list2[i-2])])
					else:
						print 'Key not found in dictionary'
						print 'b = ', float(support_data[(list2[i-2],list2[i])])
						b = float(support_data[(list2[i-2],list2[i])])
					try:
						c = a/b
					except:
						print 'Division by Zero error'
					finally:
						print ' '
						#rules.append(eval((list2[i],list2[i-2]),'--->',(list2[i-1]),'=',a/b))
						if c >= min_confidence:
							rules.append(list2[i])
							rules.append(list2[i-2])
							rules.append('--->')
							rules.append(list2[i-1])
							rules.append(c)
							rules.append('|')
				break
			elif len(list2) == 2:
				for i in range(len(list2)):
					print (list2[i]),'-->',(list2[i-1])
					a = float(support_data[list2])
					b = float(support_data[list2[i-1]])
					c = a/b
					print c
					#rules.append(eval((list2[i]),'--->',(list2[i-1]),'=',a/b))
					if c >= min_confidence:
						rules.append(list2[i])
						rules.append('--->')
						rules.append(list2[i-1])
						rules.append(c)
						rules.append('|')
				break
		elif len(itemset) == 2:
			#print (itemset[i]), '-->',(itemset[i+1])
			#print float(support_data[itemset])
			#print float(support_data[(itemset[i+1])])
			a = float(support_data[itemset])
			b = float(support_data[(itemset[i+1])])
			c = a/b
			print c
			print '{',(itemset[i]),'}', '-->','{',(itemset[i+1]),'}', '=', a/b
			#rule = [itemset[i]
			#rules.append(eval(print '{',(itemset[i]),'}', '-->','{',(itemset[i+1]),'}', '=', a/b))
			#rules.append(eval("print '{',itemset[i],'}', '-->','{',itemset[i+1],'}', '=', a/b"))
			if c >= min_confidence:
				rules.append(itemset[i])
				rules.append('--->')
				rules.append(itemset[i+1])
				rules.append(c)
				rules.append('|')
			#####
			print '{',(itemset[i+1]),'}', '-->','{',(itemset[i]),'}'
			print float(support_data[(itemset[i+1])])
			print float(support_data[itemset])
			a = float(support_data[itemset])
			b = float(support_data[(itemset[i])])
			c = a/b
			print c
			print '{',(itemset[i+1]),'}', '-->','{',(itemset[i]),'}', '=', a/b
			#rules.append((itemset[i+1]),(itemset[i]),'=',a/b)
			if c >= min_confidence:
				rules.append(itemset[i+1])
				rules.append('--->')
				rules.append(itemset[i])
				rules.append(c)
				rules.append('|')
		elif len(itemset) == 3:
			for i in range(len(itemset)):
				#print (cs.reverseMapper(itemset[i]),cs.reverseMapper(itemset[i-2])),'--->',cs.reverseMapper((itemset[i-1]))
				print (itemset[i])
				print 'a = ', float(support_data[itemset])
				a = float(support_data[itemset])
				if (itemset[i],itemset[i-2]) in support_data:
					print 'b = ', float(support_data[(itemset[i],itemset[i-2])])
					b = float(support_data[(itemset[i],itemset[i-2])])
				else:
					print 'b = ', float(support_data[(itemset[i-2],itemset[i])])
					b = float(support_data[(itemset[i-2],itemset[i])])

				d = float(support_data[itemset[i-1]])
				try:
					c = a/b
					print c
				except:
					print 'Division by Zero error'
				finally:
					print ' '
					if c >= min_confidence:
						rules.append(itemset[i])
						rules.append(itemset[i-2])
						rules.append('--->')
						rules.append(itemset[i-1])
						rules.append(c)
						rules.append('|')
					e = a/d
					print 'e = ', e
					if e >= min_confidence:
						rules.append(itemset[i-1])
						rules.append('--->')
						rules.append(itemset[i])
						rules.append(itemset[i-2])
						rules.append(e)
						rules.append('|')

		elif len(itemset) == 4:
			for i in range(len(itemset)):
				#print (cs.reverseMapper(itemset[i]),cs.reverseMapper(itemset[i-2])),'--->',cs.reverseMapper((itemset[i-1]))
				print (itemset[i])
				print 'a = ', float(support_data[itemset])
				a = float(support_data[itemset])
				if (itemset[i],itemset[i-3],itemset[i-2]) in support_data:
					print 'b = ', float(support_data[(itemset[i],itemset[i-3],itemset[i-2])])
					b = float(support_data[(itemset[i],itemset[i-3],itemset[i-2])])
				elif (itemset[i],itemset[i-2],itemset[i-3]) in support_data:
					print 'b = ', float(support_data[(itemset[i],itemset[i-2],itemset[i-3])])
					b = float(support_data[(itemset[i],itemset[i-2],itemset[i-3])])
				elif (itemset[i-3],itemset[i-2],itemset[i]) in support_data:
					print 'b = ', float(support_data[(itemset[i-3],itemset[i-2],itemset[i])])
					b = float(support_data[(itemset[i-3],itemset[i-2],itemset[i])])
				elif (itemset[i-3],itemset[i],itemset[i-2]) in support_data:
					print 'b = ', float(support_data[(itemset[i-3],itemset[i],itemset[i-2])])
					b = float(support_data[(itemset[i-3],itemset[i],itemset[i-2])])
				elif (itemset[i-2],itemset[i],itemset[i-3]) in support_data:
					print 'b = ', float(support_data[(itemset[i-2],itemset[i],itemset[i-3])])
					b = float(support_data[(itemset[i-2],itemset[i],itemset[i-3])])
				else:
					print 'b = ', float(support_data[(itemset[i-2],itemset[i-3],itemset[i])])
					b = float(support_data[(itemset[i-2],itemset[i-3],itemset[i])])
				
				d = float(support_data[itemset[i-1]])
				try:
					c = a/b
					print 'c = ', c
				except:
					print 'Division by Zero error'
				finally:
					print ' '
					if c >= min_confidence:
						rules.append(itemset[i])
						rules.append(itemset[i-3])
						rules.append(itemset[i-2])
						rules.append('--->')
						rules.append(itemset[i-1])
						rules.append(c)
						rules.append('|')
					e = a/d
					print 'e = ', e
					if e >= min_confidence:
						rules.append(itemset[i-1])
						rules.append('--->')
						rules.append(itemset[i])
						rules.append(itemset[i-3])
						rules.append(itemset[i-2])
						rules.append(e)
						rules.append('|')

					print 'a = ', float(support_data[itemset])
					a = float(support_data[itemset])
					if (itemset[i],itemset[i-3]) in support_data:
						print 'b = ', float(support_data[(itemset[i],itemset[i-3])])
						b = float(support_data[(itemset[i],itemset[i-3])])
					else:
						print 'b = ', float(support_data[(itemset[i-3],itemset[i])])
						b = float(support_data[(itemset[i-3],itemset[i])])

					try:
						c = a/b
						print 'c = ', c
					except:
						print 'Division by Zero error'
					finally:
						print ' '
						if c >= min_confidence:
							rules.append(itemset[i])
							rules.append(itemset[i-3])
							rules.append('--->')
							rules.append(itemset[i-2])
							rules.append(itemset[i-1])
							rules.append(c)
							rules.append('|')



		"""Generates a set of candidate rules from a list of frequent itemsets.

    For each frequent itemset, we calculate the confidence of using a
    particular item as the rule consequent (right-hand-side of the rule). By 
    testing and merging the remaining rules, we recursively create a list of 
    pruned rules.

    Parameters
    ----------
    list2 : list
        A list of frequent itemsets.

    support_data : dict
        The corresponding support data for the frequent itemsets (L).

    min_confidence : float
        The minimum confidence threshold. Defaults to 0.5.

    minsup : float
    	The minimum support count. Defaults to 0.5.
    Returns
    -------
    rules : list
        The list of candidate rules above the minimum confidence threshold.
    	"""
	return rules


def cleanRules(rules):
	r1 = []
	r2 = []
	for i in range(len(rules)):
		if rules[i] != '|':
			r1.append(rules[i])
		else:
			r2.append(r1)
			r1 = []

	return r2

def reversed(rules, final, test_dict):
	dict_list = test_dict.items()
	for list_item in rules:
		f = []
		for i in range(len(list_item)):
			if type(list_item[i]) is int :
				f.append(' {')
				f.append(cs.reverseMapper(list_item[i],dict_list))
				f.append('} ')
				#print  'Reverse Mapper item = ', cs.reverseMapper(list_item[i])
			elif type(list_item[i]) is float:
				f.append(' Confidence = ')
				f.append(list_item[i])
			else:
				f.append(list_item[i])
		final.append(f)
		#print final
	return final

'''Usage: reverse(rules)

[['tropical fruit', '--->', 'yogurt', 0.5], ['yogurt', '--->', 'tropical fruit', 0.5], ['whole milk', '--->', 'yogurt', 0.5], ['yogurt', '--->', 'butter', 0.6666666666666666], ['butter', '--->', 'yogurt', 0.5], ['whole milk', '--->', 'butter', 0.6666666666666666]] '''


def formattedRules(final):
	f1 = []
	for list_item in final:
		f = []
		f = ''.join(str(e) for e in list_item)
		f1.append(f)
	return f1


if __name__ == '__main__':
	main()


#  TIME PROFILER 1 USAGE: $ python -m cProfile -s cumulative antimirror.py
#  TIME PROFILER 2 USAGE: $ time -p python antimirror.py   MEMORY PROFILER 1 USAGE: $ mprof run antimirror.py
#  TIME PROFILER 3 USAGE: $ python -m timeit -n 4 -r 5 -s "import antimirror" "antimirror.main()"