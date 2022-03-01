# https://www.hackerrank.com/challenges/validating-credit-card-number/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

u_i_num = int(input())

a_str = ''
#gets all valid cc's but doesn't filter repeating nums
pattern = re.compile(r'^([4-6]\d{3})-?(\d{4})-?(\d{4}-?\d{4})$')

bad_pattern = re.compile(r'(\d)\1+-?(\1){2}')

#bool(re.search(pattern, txt))

for inputs in range(u_i_num):
    
    a_str = input()
    #print(a_str)
    if bool(bad_pattern.search(a_str)) == False:
        if bool(pattern.search(a_str)) == True:
            print("Valid")
            #print(pattern.search(a_str))
        else:
            print("Invalid")
    else:
        print("Invalid")



