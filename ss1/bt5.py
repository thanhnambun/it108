s = input("Nhập 1 chuỗi số (1 hoặc 0): ")

if s == "1":
    b = True
elif s == "0":
    b = False
else:
    print("Giá trị không hợp lệ!")
    exit()

print("Giá trị boolean là:", b)
