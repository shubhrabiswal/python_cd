'''
Find Reachability 

JS newbie "A" wants to check if he can
reach out to a React expert "B" using his network of React
developers. If he can then return 1 else return 0. 
INPUT FORMAT Total members in React Developer Community = N 
Memberld1 = N1 
Memberld2 = N2 
Memberld3 = N3 
MemberldN = Nn 
Total possible edges = E 
<follower 1 (member ID> <following 1 (member ID)>= u1,v1 
<follower 2 (member ID> <following 2 (member ID)> = u2,12 
<follower N> <following N> = un, vn 
Follower = A 
Following = B 
OUTPUT FORMAT 
If A can reach B then output is 1, else 0. 
Sample Input 
4 
2 
5 
7 
9 
4 
2 9 
7 2 
7 9 
9 5    
7 
9

Sample Output 1 
'''

#####
try:
    L=[]
    while True:
        name=input()
        L.append(name)
except:
    pass

follower = []
following = []
rel = []
for ele in L:
    if len(ele) > 1:
        rel.append(ele)
        follower.append(ele[0])
        following.append(ele[2])
    else:
        follower.append(ele)
op = 0 #initilize op
for ind in range(1,len(follower)):    ##### to check whether the follower can approach the following or not
    if ind ==0:
        if follower[ind] in following or follower[ind+1] in following:
            op =1
    elif ind == len(follower):
        if follower[ind] in following or follower[ind-1] in following:
            op = 1
    elif follower[ind] in following or follower[ind+1] in following or follower[ind-1] in following:
        op=1
    
print(op)
