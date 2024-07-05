"""Arrow"""
n , k = int(input()) , int(input())
for i in range(int((k-1)/2) , 0 , -1) :
    print(" "*i + "*"*n)
for i in range(0 , int((k-1)/2)+1) :
    print(" "*i + "*"*n)
