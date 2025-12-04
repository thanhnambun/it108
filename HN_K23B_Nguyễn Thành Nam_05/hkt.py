import csv
import os
import matplotlib.pyplot as plt

def load_data(filename="data.json"):
    players = []
    if not os.path.exists(filename):
        return players

    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["so_tran"] = int(row["so_tran"])
            row["ban_thang"] = int(row["ban_thang"])
            row["kien_tao"] = int(row["kien_tao"])
            row["diem_thanh_tich"] = int(row["diem_thanh_tich"])
            players.append(row)
    return players


def save_data(players, filename="data.json"):
    if not players:
        print("Danh sách trống!")
        return
    with open(filename, mode= "w", newline="", encoding="utf-8") as f:
        fieldnames = ["ma_ct", "ten_ct"," | ", "so_tran"," | ", "ban_thang"," | ",
                      "kien_tao"," | ", "diem_thanh_tich"," | ","danh_hieu"]

        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(players)



def tinh_danh_hieu(diem):
    if diem > 40:
        return "Vàng"
    elif diem > 20:
        return "Bạc"
    else:
        return "Đồng"


def hien_thi(players):
    print("\n=== DANH SÁCH CẦU THỦ ===")
    if not players:
        print("Danh sách trống!")
        return
    print(f"{'Mã':<8}{'Tên':<20}{'Trận':<8}{'BT':<5}{'KT':<5}{'Điểm':<8}{'Danh hiệu'}")
    print("-" * 70)
    for p in players:
        print(f"{p['ma_ct']:<8}{p['ten_ct']:<20}{p['so_tran']:<8}{p['ban_thang']:<5}{p['kien_tao']:<5}{p['diem_thanh_tich']:<8}{p['danh_hieu']}")


def them_moi(players):
    print("\n=== THÊM CẦU THỦ ===")
    ma = input("Mã cầu thủ: ")

    if any(p["ma_ct"] == ma for p in players):
        print(" Mã cầu thủ bị trùng!")
        return

    ten = input("Tên cầu thủ: ")
    so_tran = int(input("Số trận: "))
    ban = int(input("Bàn thắng: "))
    kt = int(input("Kiến tạo: "))

    if so_tran < 0 or ban < 0 or kt < 0:
        print(" Chỉ số phải >= 0")
        return

    diem = ban * 2 + kt
    danh_hieu = tinh_danh_hieu(diem)

    players.append({
        "ma_ct": ma,
        "ten_ct": ten,
        "so_tran": so_tran,
        "ban_thang": ban,
        "kien_tao": kt,
        "diem_thanh_tich": diem,
        "danh_hieu": danh_hieu
    })

    print(" Thêm cầu thủ thành công!")


def cap_nhat(players):
    print("\n=== CẬP NHẬT CẦU THỦ ===")
    ma = input("Nhập mã cầu thủ: ")

    for p in players:
        if p["ma_ct"] == ma:
            print(f"Đang cập nhật {p['ten_ct']}...")

            ban = int(input("Bàn thắng mới: "))
            kt = int(input("Kiến tạo mới: "))

            p["ban_thang"] = ban
            p["kien_tao"] = kt
            p["diem_thanh_tich"] = ban * 2 + kt
            p["danh_hieu"] = tinh_danh_hieu(p["diem_thanh_tich"])

            print(" Cập nhật thành công!")
            return

    print(" Không tìm thấy cầu thủ!")


def xoa(players):
    print("\n=== XÓA CẦU THỦ ===")
    ma = input("Nhập mã cầu thủ: ")

    for p in players:
        if p["ma_ct"] == ma:
            confirm = input("Bạn chắc muốn xóa? (y/n): ").lower()
            if confirm == "y":
                players.remove(p)
                print(" Đã xóa thành công!")
            else:
                print(" Đã hủy xóa")
            return
    
    print(" Không tìm thấy cầu thủ!")


def tim_kiem(players):
    print("\n=== TÌM KIẾM CẦU THỦ ===")
    keyword = input("Nhập tên hoặc mã: ").lower()

    results = [p for p in players if keyword in p["ten_ct"].lower() or keyword == p["ma_ct"]]

    if not results:
        print(" Không tìm thấy!")
        return

    print("Kết quả tìm kiếm:")
    hien_thi(results)


def sap_xep(players):
    print("\n=== SẮP XẾP CẦU THỦ ===")
    print("1. Điểm thành tích giảm dần")
    print("2. Bàn thắng giảm dần")
    choice = input("Chọn: ")

    if choice == "1":
        players.sort(key=lambda p: p["diem_thanh_tich"], reverse=True)
    elif choice == "2":
        players.sort(key=lambda p: p["ban_thang"], reverse=True)
    else:
        print(" Lựa chọn không hợp lệ!")
        return

    print(" Đã sắp xếp xong!")


def thong_ke(players):
    vang = sum(p["danh_hieu"] == "Vàng" for p in players)
    bac = sum(p["danh_hieu"] == "Bạc" for p in players)
    dong = sum(p["danh_hieu"] == "Đồng" for p in players)

    print("\n=== THỐNG KÊ DANH HIỆU ===")
    print(f"Vàng: {vang}")
    print(f"Bạc: {bac}")
    print(f"Đồng: {dong}")

    return vang, bac, dong


def ve_bieu_do(players):
    vang, bac, dong = thong_ke(players)
    
    labels = ['Vàng', 'Bạc', 'Đồng']
    sizes = [vang, bac, dong]

    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('Biểu đồ danh hiệu cầu thủ')
    plt.show()


def main():
    players = load_data()

    while True:
        print("\n====== MENU QUẢN LÝ CẦU THỦ ======")
        print("1. Hiển thị danh sách")
        print("2. Thêm mới cầu thủ")
        print("3. Cập nhật cầu thủ")
        print("4. Xóa cầu thủ")
        print("5. Tìm kiếm")
        print("6. Sắp xếp")
        print("7. Thống kê danh hiệu")
        print("8. Vẽ biểu đồ")
        print("9. Lưu file CSV")
        print("0. Thoát")
        
        ch = input("Chọn chức năng: ")

        if ch == "1": hien_thi(players)
        elif ch == "2": 
            while (True):
                them_moi(players)
                more = input(" Thêm tiếp? (y/n): ").lower()
                if more != "y":
                    break
        elif ch == "3": cap_nhat(players)
        elif ch == "4": xoa(players)
        elif ch == "5": tim_kiem(players)
        elif ch == "6": sap_xep(players)
        elif ch == "7": thong_ke(players)
        elif ch == "8": ve_bieu_do(players)
        elif ch == "9": 
            save_data(players)
            print(" Đã lưu vào CSV!")
        elif ch == "0":
            save_data(players)
            print(" Thoát chương trình...")
            break
        else:
            print(" Lựa chọn không hợp lệ!")


main()
