import textwrap
#interesting library to report; can do things like textwrap.shorten((end with ]...]))
def wrap(string,max_width):
   #create textwrapper instance
    wrapper = textwrap.TextWrapper(width=max_width)
    word_list = wrapper.wrap(text=string)
    #this works, but not with print(result below)
    # for el in word_list:
    #     print(el)
    return '\n'.join(word_list)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)