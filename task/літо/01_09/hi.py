numbers = [1, 4, 6, 8, 10, 13, 18, 23, 45, 73, 3]
for h in numbers:
    n = h % 2
    if n == 0:
        print(f"{h} - парне число")
    else:
        print(f"{h} - непарне число")