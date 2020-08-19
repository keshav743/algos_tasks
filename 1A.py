possiblities = []
numLength = int(input())
newNum = input()
numBinary= ""
avgNum1 = ""
avgNum2 = ""

def BinaryToDecimal(n): 
    return int(n,2) 
    
def DecimalToBinary(n): 
    return bin(n).replace("0b","") 
    
for i in newNum:
    if(i == "1" or i == "0"):
        numBinary+=i
        
if(newNum == numBinary):    
    if(numLength <= 100000 and numLength == len(numBinary)):

        numDecimal = BinaryToDecimal(numBinary)
        for i in range(0,2*numDecimal+1):
            for j in range(0,i):
                if(j+i == 2*numDecimal):
                    possiblities.append([j,i])
        for (i,j) in possiblities:

            if(len(DecimalToBinary(i)) == len(DecimalToBinary(j)) == len(numBinary)):
                if(i<j):
                    avgNum1 = DecimalToBinary(i)
                    avgNum2 = DecimalToBinary(j)
                else:
                    avgNum1 = DecimalToBinary(j)
                    avgNum2 = DecimalToBinary(i)
        if(not avgNum1 == "" and  not avgNum2 == ""):
            print(avgNum1+" "+avgNum2)
