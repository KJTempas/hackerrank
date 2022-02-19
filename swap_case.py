#swap case of all letters
#completed
def swap_case(s):
    result = ''
    for x in s:
        if x.isupper():
            result = result + x.lower()
        elif x.islower():
            result = result + x.upper()
        else:
            result = result + x
    return result

#tried using ternary but was unsuccessful

#swap_case('Www.HackerRank.com') # 'sWW.hACKERrANK.COM'
#swap_case('Pythonist 2') #pYTHONIST 2'

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)