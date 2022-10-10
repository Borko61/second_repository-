hour = int(input())
min = int(input())
min = min + 15
if min > 59:
    hour = hour + 1
    min = min - 60
if hour > 23:
    hour = 0
if min > 9:
    print(f'{hour}:{min}')
else:
    print(f"{hour}:0{min}")

