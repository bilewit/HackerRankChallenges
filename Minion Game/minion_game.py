# https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=false

def minion_game(string):
    # your code goes here
    
    word = string
    string_len = len(word) 
    counter_1 = 0
    counter_2 = 1
    #print(string_len)
    vowels = ['A','E','I','O','U']
    v_player = 0
    c_player = 0
    
    for index,letter in enumerate(word):
        # print(letter,index)
        total = string_len 
        fun = str(index)
        if letter in vowels:
            v_player += (total) - index
        elif letter not in vowels:
            c_player += (total) - index
    
    # r = string[1:2]
    
    if v_player > c_player:
        print('Kevin '+str(v_player))
    elif v_player < c_player:
        print('Stuart '+str(c_player))
    elif v_player == c_player:
        print('Draw')
    
    
    

if __name__ == '__main__':
    s = input()
    minion_game(s)

