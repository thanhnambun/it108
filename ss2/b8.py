a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))

if a > 0 and b > 0 and c > 0 and (a + b > c and a + c > b and b + c > a):
    print("La 3 canh tam giac")
else:
    print("Khong phai 3 canh tam giac")
