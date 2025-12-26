# number 1
print("Hello world")

# number 2
name = input("Введите ваше имя ")
print("Hello,", name)

# number 3
a = int(input("Введите число "))
b = int(input("Введите число "))
print('Сумма =', a+b)

# number 4
a = int(input("Введите число "))
b = int(input("Введите число "))
print("a+b =", a+b, "a-b =", a-b, "a*b =", a*b, "a/b =", a/b, "a//b =", a//b, "a%b =", a%b, "a**b =", a**b)

# number 5
a = int(input("Введите число "))
if a % 2 == 0: print("Число четное")
else: print("Число нечетное")

# number 6
a = int(input("Введите число "))
if a < 0: print("Оно отрицательное")
elif a > 0: print("Оно положительное")
else: print("Это 0")

# number 7
a = int(input("Введите число "))
print("a*1 =", a*1, "a*2 =", a*2, "a*3 =", a*3, "a*4 =", a*4, "a*5 =", a*5, "a*6 =", a*6, "a*7 =", a*7, "a*8 =", a*8, "a*9 =", a*9, "a*10 =", a*10)

# number 8
a = int(input("Введите число "))
f = 1
for i in range(1, a+1):
    f *= i
print("Факториал данного числа =",f)

# number 9
a = int(input("Введите число "))
def justNumber(number):
    for i in range(2, number//2+1):
        if number%i==0: 
            print("Число не простое")
    print("Число простое")
justNumber(a)
# number 10
a = int(input("Введите число "))
b = int(input("Введите число "))
c = int(input("Введите число "))
print('min =', min(a,b,c), 'max =', max(a,b,c))
