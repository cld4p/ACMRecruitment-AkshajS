#factorial digit sum
n=1

for i in range(1,101):
    n*=i

print(sum(list(map(int, list(str(n))))))


