x = -123

x_str = str(x)

if (x_str[0] == "-"):
    x_str = x_str[1:]
    output = "-" + (x_str[::-1])
else:
    output = x_str[::-1]

output_int = int(output)
if abs(output_int) <= (2**31)-1:
     print(output_int)
else: print("1")

