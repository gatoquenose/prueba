def cambia(num):
    if num % 10 == 1:
        return  0 + cambia(num // 10)*10
    else:
        return cambia(num//10) and  num % 10
print(cambia(101210))
