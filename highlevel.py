# number 1
def variants(start, finish):
    if start > finish: return 0
    if start == finish: return 1
    return variants(start+1,finish) + variants(start+2, finish)
a = int(input("Введите количество ступеней лестницы "))
print("До верха лестницы можно подняться", variants(1, a), "способами")

# number 2
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maxi = finalmax = arr[0]
for i in range(1, len(arr)):
    maxi = max(arr[i], maxi + arr[i])
    finalmax = max(finalmax, maxi)
print(finalmax)

# number 3
a = int(input("Введите сколько у вас денег "))
print(f"Вам нужно взять {a // 4} монет номиналом 4, {(a%4)//3} монет номиналом 3 и {(a%4)%3} монет номиналом 1, всего необходимо {(a // 4)+((a%4)//3)+((a%4)%3)} монет")

# number 4
a = input("Введите первое слово ")
b = input("Введите второе слово ")
c=0
for i in range(len(a)):
    if a[i] != b[i]: c += 1
print("Необходимо количество операций ", c)

