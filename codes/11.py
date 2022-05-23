# from collections import deque


height = [1,8,6,2,5,4,8,3,7]
# height = deque(height)
# area = 0
# while height:
#     a = height.popleft()
#     for i in range(len(height)):
#         print(height[i])
#         y = min(a,height[i])
#         x = i+1
#         area = max(area,y*x)

# print(area)
area =0
window_end = len(height) -1
window_start = 0

while window_start > window_end:
    h2 = height[window_end]
    h1 = height[window_start]
    w = window_end - window_start

    area = max(area,min(h2, h1) * w)
    if h2 > h1:
        window_start += window_start
    else:
        window_end -= window_end
print(area)
