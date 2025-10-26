total = 0
for i in range(1, 51):
    if i == 1:
        print(f"{i}やで")
    else:
        print(f"{total}足す{i}は{total + i}やで")
    total += i
