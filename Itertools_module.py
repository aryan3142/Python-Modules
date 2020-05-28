import itertools
# <!!!---------- python's itertools module implementation ----------!!!>

#there are  three types of iterators in python's itertools module
# 1. infinite iterators
# 2. combinatoric iterators
# 3. terminating iterators

# infinite iterators
# a. count(start,step) : it prints infinitely from the mentioned start with the step being default to 1


for i in itertools.count(1,5):
    if i==31 :
        break
    print(i,end=" ")

#b. cycle(iterable) : it prints all elements from the iterable repeatedly
count = 0
li=["A","B","C"]
for i in itertools.cycle(li):
    if count == 9 :
        break
    else:
        print(i,end = " ")
        count+=1

   #using next function
iterator = itertools.cycle(li)
for i in range(6):
    print(next(iterator),end=" ")
    
#c. repeat(val,num) : it prints a value infinite number of times, if optional parameter num is menetioned than it 
#prints the val num number of times

print(list(itertools.repeat(100,5)))

#combinatoric iterators
#a. product(): this tool computes the cartisian product of the input iterables. To compute the cartisian product 
#with itself, we use the repeat keyword argument to specify the number of keyword argument
from itertools import product
a = [1,2]
b = [3,4]
print(list(product(a,repeat=2)))
print(list(product(a,b)))

#b. permutations: this is used to generate all posssible permutations of an iterable. permutations are where the order
#position of the elements matter
from itertools import permutations
a = [1,2,3]
print(list(permutations(a,2)))
#if the value of the group size is not specified than the value of the group size becomes the size of the iterable
print(list(permutations(a)))

#c. combinations : this is used to generate all possible combinations of an iterable. combinations are where
#order dosen't matters, it prints all combinations of the iterable in sorted order
from itertools import combinations
print(list(combinations(a,3)))

#3. terminating itertors:
#a. accumulate: this functions take two arguments, iterable target and the function which would be followed at 
#each iteration of value in target. If no function is passed, addition takes place by default.
from itertools import accumulate
import operator
a = [1,2,5,10]
print(list(accumulate(a)))
print(list(accumulate(a,operator.mul)))

#b. chain(iter1, iter2..): This function is used to print all the values in iterable targets one after another 
#mentioned in its arguments.

from itertools import chain
a = [1,2,3]
b = [2,3,4]
c = [4,5,6]
print(list(chain(a,b,c)))

#c. filterfalse(func, seq): As the name suggests, this iterator prints only values that return false for the passed function.
from itertools import filterfalse
li = [2, 4, 5, 7, 8] 
  
# using filterfalse() to print false values  
print(list(filterfalse(lambda x : x % 2 == 0, li)))  

#d. islice(iterable, start, stop, step): This iterator selectively prints the values mentioned in its iterable container 
#passed as argument. This iterator takes 4 arguments, iterable container, starting pos., ending position and step.

from itertools import islice
a = [1,2,3,4,6,5,4,6,7,8]
print(list(islice(a,1,6,2)))

#e. starmap(func., tuple list): This iterator takes a function and tuple list as argument and returns the value according 
#to the function from each tuple of list.

from itertools import starmap
li = [ (1, 10, 5), (8, 4, 1), (5, 4, 9), (11, 10, 1) ]  
    
# using starmap() for selection value acc. to function  
# selects min of all tuple values  
print (list(starmap(min, li)))

#f. takewhile(func, iterable): This iterator is opposite of dropwhile(), it prints the values till the function returns 
#false for 1st time.

from itertools import takewhile
li = [2, 4, 6, 7, 8, 10, 20]  
    
# using takewhile() to print values till condition is false.  
print (list(takewhile(lambda x : x % 2 == 0, li ))) 

#g. zip_longest( iterable1, iterable2, fillval): This iterator prints the values of iterables alternatively in sequence. 
#If one of the iterables is printed fully, remaining values are filled by the values assigned to fillvalue.

from itertools import zip_longest
print(list(zip_longest('Ryan', 'Khan', fillvalue ='_' )))

#h. compress(iter, selector): This iterator selectively picks the values to print from the passed container according to 
#the boolean list value passed as other arguments. The arguments corresponding to boolean true are printed else all are skipped.

from itertools import compress
print (list(itertools.compress('GEEKSFORGEEKS', [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0])))


#<-------- These are the functions in itertools module -------->




    