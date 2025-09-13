#sum of multiples of 3 or 5

a=0

for i in range(1,1001):
    if i%3==0:
        a+=i
    elif i%5==0:
        a+=i
        
print(a)

#factorial digit sum
n=1

for i in range(1,101):
    n*=i

print(sum(list(map(int, list(str(n))))))



