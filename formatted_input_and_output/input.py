# test1: input
# while 1:
#     a = input()
#     print(a)
# input:  3234 234
# output: 3234 234

# test2: 一个变量一行输入input()&raw_input()
'''
while True:
    try:
       a=input()
       temp=[]
       for i in range(int(a)):
           buff=input()
           temp.append(int(buff))
       temp=set(temp)
       temp=list(temp)
       temp.sort()
       for i in temp:
           print(i)
    except:
        break
'''


# test3: import sys + sys.stdin.readline()
import sys
# while(True):
#     try:
#         a = sys.stdin.readline()
#         b = sys.stdin.readline()
#         print(a, type(a))
#         print(b, type(b))
#     except:
#         break

# n = int(sys.stdin.readline().strip())
n = int(input())
point = []
for i in range(n):
    point.append(sys.stdin.readline().strip().split())
x = 1