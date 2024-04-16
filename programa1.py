def cambia(num):
    if num % 10 == 1:
        return cambia(num // 10), 0
    else:
        return cambia(num//10) and  num % 10
print(cambia(101210))