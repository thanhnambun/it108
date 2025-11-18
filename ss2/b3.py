number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print("Số vừa nhập chia hết cho cả 3 và 5.")
elif number % 3 == 0:
    print("Số vừa nhập chia hết cho 3.")
elif number % 5 == 0:
    print("Số vừa nhập chia hết cho 5.")
else:
    print("Số vừa nhập không chia hết cho 3 và 5.")
