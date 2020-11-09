"""
https://www.hackerrank.com/contests/w26/challenges/twins
"""

m,n = map(int, input().strip().split())

l_primes = []
prime = -99999999999
num = 0

for i in range(m, n-1):
    ##print("i", i)
    if i >= 5 :
        if i%6 == 5 or i%6 == 1:
             for x in range(2,4*i//5 +1):
                #print("loop1 x", x)
                if i%x == 0 or (i+2)%x == 0:
                    prime = 0
                    break
                else:
                    #print("this is prime", i)
                    prime = 1
        else:
            prime = 0
        
                

    else:
        for x in range(2,4*i//5 +1):
            #print("loop2 x", x)
            if i%x == 0 or (i+2)%x == 0:
                prime = 0
                break
            else:
                #print("this is prime", i)
                prime = 1
                
                    
    if prime == 1:
        num += 1
    #print("prime", prime)
    #print("number of prime pairs", num)
    
print(num)
