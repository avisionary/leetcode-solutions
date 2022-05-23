strs = ["flower","flow","flight"]
#strs = ["dog","racecar","car"]

smallest_str = min(strs, key=len)
len_max = len(smallest_str)
print(len_max)
check = True
while len_max >0:
    for str_a in strs:
        x = str_a[:len_max]
        if x == smallest_str:
            #print(x)
            check = True
        else:
            check  = False
            break

    if check == False:
        len_max = len_max - 1
        smallest_str = smallest_str[:len_max]
    else:
        break

print(smallest_str)


#while len_max >0:
