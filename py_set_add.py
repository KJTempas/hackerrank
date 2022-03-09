#input list of country stamps
#output total number of distinct country stamps

def py_set_add(countries):
    x = set(countries)
    return len(x)
   
#py_set_add(['UK', 'China', 'USA', 'France', 'New Zealand', 'UK', 'France']) #5

#STDIN
if __name__ == '__main__':
    N = int(input())
    countries =[]
    for x in range(N):
        countries.append(input())
    print(py_set_add(countries))