'''
https://www.hackerrank.com/challenges/pangrams/problem
Author: rbakshee
'''

inp = sorted(list(set((input().lower()))))

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
c = 0
for i in alpha:
    if i in inp: 
        c += 1
if c == 26 : print("pangram")
else: print("not pangram")

