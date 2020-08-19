n,r,x,y = input().split()
c1_string = input()
c1_arr = c1_string.split()
c2_string = input()
c2_arr = c2_string.split()
c1 = []
c2 = []

for i in c1_arr:
    if(i=="1" or i=="0"):
        c1.append(i)
for i in c2_arr:
    if(i=="1" or i=="0"):
        c2.append(i)
        
if((int(n)>=1 and int(n)<=1000000) and (int(r)>=1 and int(r)<=3000) and (int(x)>=1 and int(x)<=100) and (int(y)>=1 and int(y)<=100) and (len(c1)==len(c1_arr)) and (len(c2)==len(c2_arr)) and (len(c1)==len(c2))):
    z = int(r)
    for i in range(int(n)):
        if(int(c1[i])==int(c2[i])==1):
            z += int(x)
        elif(int(c1[i])==1 and int(c2[i])==0):
            z -=int(y)
        else:
            pass
    if(z > int(r)):
        print("promoted")
    elif(z < int(r)):
        print("demoted")
    else:
        print("no change")
