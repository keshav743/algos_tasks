import sys
x = input()
x_arr = x.split()
test_arr = {}
count = 0
while(count<4):
    y,z = input().split()
    arr_y = x_arr[int(y)]
    arr_z = x_arr[int(z)]
    print(int(arr_y)*int(arr_z))
    sys.stdout.flush()
    for i in (10,8,7,16,9,43):
        for j in (10,8,7,16,9,43):
            if(i*j == int(arr_y)*int(arr_z)):
                if(not y in test_arr or not z in test_arr):
                    test_arr[y] = i
                    test_arr[z] = j
                    break
    count+=1
print(test_arr)
