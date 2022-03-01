# https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=false

# Enter your code here. Read input from STDIN. Print output to STDOUT

#Num Commands
num_commands = int(input())
word_bank = dict()


for command in range(num_commands):
    get_word = input()
    if word_bank.get(get_word) != None:
        word_bank[get_word] += 1
    else:
        word_bank[get_word] = 1


int_result = list(word_bank.values())
string_results = [str(num) for num in int_result]

print(len(word_bank.keys()))
print(" ".join(string_results))
        
