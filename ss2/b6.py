n = int(input("Nhập số n: "))

factorial = 1   

for i in range(1, n + 1):
    factorial *= i   

print("Giai thừa của", n, "là:", factorial)
