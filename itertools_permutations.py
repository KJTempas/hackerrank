#itertools.permutations(interable[,r]) returns successive r length
# permutations of elements in an iterable;
# if r is not specified or is None, r defaults to length of iterable

#given S, find all possible permutations of size k of the string in 
#lexicographic sorted order
#help from https://www.tutorialspoint.com/python-join-tuple-elements-in-a-list
from itertools import permutations
def iter_perm(s,k):
    string_tuples = list(permutations(s,k)) 

    def join_tuple_string(string_tuple):
       return  ''.join(string_tuple) #remove space between elements
    #join all tuples - call the function join_tuple_string on each string tuple in string_tuples
    result = map(join_tuple_string, string_tuples)

    a = list(result)
    x = sorted(a)
    print('\n'.join(str(i) for i in x)) #join with new line between elements

#iter_perm('HACK', 2) #AC AH AK CA CH....there are 12 combos

#input format - single line containing space separated string and integer value k
if __name__ == '__main__':
    s, k = input().split()
    k = int(k)
    iter_perm(s,k)