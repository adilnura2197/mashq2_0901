#1-misol
for i in range(1, 11):
    print(i)

#2-misol
n = int(input("n = "))
yigindi = 0
for i in range(1, n + 1):
    yigindi += i
print(yigindi)

#3-misol
n = int(input("n = "))
i = 2
while i <= n:
    print(i)
    i += 2

#4-misol
son = int(input("Son kiriting: "))
count = 0
while son > 0:
    count += 1
    son //= 10
print(count)

#5-misol
i = 1
while i <= 5:
    print("Salom")
    i += 1
