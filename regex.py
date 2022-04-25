#regex_pattern = r"[,.]"
# regex_pattern = r"[,|.]" #[a set of chars]
# import re
# #goal, to split at the ,  and .

# def split(s):
#     print("\n".join(re.split(regex_pattern, s)))
# split("100,000,000.000")

#result is 
# 100
# 000
# 000
# 000
#-----------------
#regex Group()
#pring first occurrence of the repeating character; if none, print -1
s = input()
import re
m = re.match(r'\d')

#..123456111213   # 1