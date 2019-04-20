import sys

# 定义函数不代表函数被执行
def exchange(a):
    (min_value, min_position) = (sys.maxsize, -1)
    for i in range(10):
        value = abs(a[i])
        if(value < min_value):
            min_position = i
            min_value = value
    end_position = len(a)-1
    t = a[min_position]
    a[min_position] = a[end_position]
    a[end_position] = t
    return a

a = input().split()
for i in range(10):
    a[i] = int(a[i])
a = exchange(a)   # 要调用函数，函数才会被执行
for i in range(10):
    print(a[i], end = " ")
