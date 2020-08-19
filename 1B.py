l = int(input())
symString = input()
count = 0
if(l == len(symString) and l<=1000000):
    for i in range(0,20):
        if(l==2**i):
            if(l==1):
                print("0")
                break    
            else:
                while(l != 1 or (symString[0,l/2] == symString[l/2,l])):
                    m = int(l/2)
                    n = int(l)
                    y = slice(0,m,1)
                    z = slice(m,n,1)
                    if(symString[y] == symString[z]):
                        count+=1
                    l=int(l/2)
                    x = slice(0,l,1)
                    symString = symString[x]
                    if(l==1):
                        break
                    else:
                        continue
                print(count)
                break
        else:
            continue
