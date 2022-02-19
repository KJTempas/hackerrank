#given a string, s, find out if the string contains ANY alphanumeric characters,
# ANY alphabetical chars, ANY digits, ANY lowercase and ANYuppercase chars; print results onc per line
#True or False

def string_validators(s): #completed
  # any() returns True if any item in iterable is True, else False
  #map objects are iterators; they are the results after applyingn the given fx to each item of a list, tuple, etc
  #map(function, variable) so I am sending the variable s to the function/method  str.isdigit
    #the function str.isalnum, etc tests each element in s and makes a list of responses
   # print(map(str.isalnum, s)) # the result is [ True, True, True] for 'abc'

    print(any(map(str.isalnum, s)))
    print(any(map(str.isalpha, s)))
    print(any(map(str.isdigit, s)))
    print(any(map(str.islower, s)))
    print(any(map(str.isupper, s)))

#string_validators('qA2') #True True True True True (all on separate lines)
#string_validators('12abc') #True True True True False
#string_vaidators('abc') #True True False True False

#help from https://www.kite.com/python/answers/how-to-check-if-a-string-contains-a-number-in-python


if __name__ == '__main__':
    #s = input() # to make this work, must enter data with ' ' , like 'catS1'

   # import pdb; pdb.set_trace()
   
    string_validators(s)

  