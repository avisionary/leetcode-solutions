n = "00000010100101000001111010011100"
n_str = str(n)
number = 0
for i in range(len(n_str)):
    number = number + 2**i
print(number)