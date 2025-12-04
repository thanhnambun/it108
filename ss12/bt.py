import json
import csv
import os
from tabulate import tabulate
import matplotlib.pyplot as plt

DATA_FILE = "data.json"


def load_data():
    """Tải dữ liệu từ file JSON"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []


def save_data(students):
    """Lưu dữ liệu vào file JSON"""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(students, f, ensure_ascii=False, indent=2)
    print("✓ Dữ liệu đã được lưu.")


def save_csv(students):
    """Lưu dữ liệu vào file CSV"""
    if not students:
        print("Danh sách trống!")
        return
    with open("data.csv", 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(
            f, fieldnames=['ma_sv', 'ten', 'toan', 'ly', 'hoa', 'diem_tb', 'xep_loai'])
        writer.writeheader()
        writer.writerows(students)
    print("✓ Dữ liệu đã được lưu vào data.csv")


def calculate_avg(toan, ly, hoa):
    """Tính điểm trung bình"""
    return round((toan + ly + hoa) / 3, 2)


def classify(diem_tb):
    """Xếp loại học lực"""
    if diem_tb >= 8.0:
        return "Giỏi"
    elif diem_tb >= 6.5:
        return "Khá"
    elif diem_tb >= 5.0:
        return "Trung Bình"
    else:
        return "Yếu"


def display_students(students):
    """Hiển thị danh sách sinh viên dưới dạng bảng"""
    if not students:
        print("Danh sách trống!")
        return
    headers = ["Mã SV", "Tên", "Toán", "Lý", "Hóa", "Điểm TB", "Xếp loại"]
    data = [[s['ma_sv'], s['ten'], s['toan'], s['ly'], s['hoa'], s['diem_tb'], s['xep_loai']]
            for s in students]
    print("\n" + tabulate(data, headers=headers, tablefmt="grid"))


def add_student(students):
    """Thêm sinh viên mới"""
    ma_sv = input("Nhập mã SV: ").strip()
    if any(s['ma_sv'] == ma_sv for s in students):
        print("⚠ Mã SV đã tồn tại!")
        return

    ten = input("Nhập tên: ").strip()
    try:
        toan = float(input("Điểm Toán (0-10): "))
        ly = float(input("Điểm Lý (0-10): "))
        hoa = float(input("Điểm Hóa (0-10): "))
        if not (0 <= toan <= 10 and 0 <= ly <= 10 and 0 <= hoa <= 10):
            print("⚠ Điểm phải trong khoảng 0-10!")
            return
    except ValueError:
        print("⚠ Vui lòng nhập số!")
        return

    diem_tb = calculate_avg(toan, ly, hoa)
    xep_loai = classify(diem_tb)
    students.append({
        'ma_sv': ma_sv, 'ten': ten, 'toan': toan, 'ly': ly, 'hoa': hoa,
        'diem_tb': diem_tb, 'xep_loai': xep_loai
    })
    print(f"✓ Thêm {ten} thành công!")


def update_student(students):
    """Cập nhật sinh viên"""
    ma_sv = input("Nhập mã SV cần cập nhật: ").strip()
    for s in students:
        if s['ma_sv'] == ma_sv:
            try:
                toan = float(
                    input(f"Điểm Toán mới ({s['toan']}): ") or s['toan'])
                ly = float(input(f"Điểm Lý mới ({s['ly']}): ") or s['ly'])
                hoa = float(input(f"Điểm Hóa mới ({s['hoa']}): ") or s['hoa'])
                if not (0 <= toan <= 10 and 0 <= ly <= 10 and 0 <= hoa <= 10):
                    print("⚠ Điểm phải trong khoảng 0-10!")
                    return
                s['toan'], s['ly'], s['hoa'] = toan, ly, hoa
                s['diem_tb'] = calculate_avg(toan, ly, hoa)
                s['xep_loai'] = classify(s['diem_tb'])
                print(f"✓ Cập nhật {s['ten']} thành công!")
                return
            except ValueError:
                print("⚠ Vui lòng nhập số!")
                return
    print("⚠ Không tìm thấy sinh viên!")


def delete_student(students):
    """Xoá sinh viên"""
    ma_sv = input("Nhập mã SV cần xoá: ").strip()
    for i, s in enumerate(students):
        if s['ma_sv'] == ma_sv:
            confirm = input(
                f"Bạn có chắc muốn xóa {s['ten']}? (y/n): ").lower()
            if confirm == 'y':
                del students[i]
                print("✓ Xoá thành công!")
            return
    print("⚠ Không tìm thấy sinh viên!")


def search_student(students):
    """Tìm kiếm sinh viên"""
    print("Tìm theo: 1. Mã SV  2. Tên")
    choice = input("Chọn (1/2): ").strip()
    results = []

    if choice == '1':
        ma_sv = input("Nhập mã SV: ").strip()
        results = [s for s in students if s['ma_sv'] == ma_sv]
    elif choice == '2':
        ten = input("Nhập tên: ").strip().lower()
        results = [s for s in students if ten in s['ten'].lower()]

    if results:
        display_students(results)
    else:
        print("⚠ Không tìm thấy!")


def sort_students(students):
    """Sắp xếp danh sách"""
    if not students:
        print("Danh sách trống!")
        return
    print("Sắp xếp theo: 1. Điểm TB (↓)  2. Tên (A-Z)")
    choice = input("Chọn (1/2): ").strip()

    if choice == '1':
        students.sort(key=lambda x: x['diem_tb'], reverse=True)
    elif choice == '2':
        students.sort(key=lambda x: x['ten'])

    print("✓ Đã sắp xếp!")
    display_students(students)


def stats(students):
    """Thống kê điểm"""
    if not students:
        print("Danh sách trống!")
        return

    counts = {'Giỏi': 0, 'Khá': 0, 'Trung Bình': 0, 'Yếu': 0}
    for s in students:
        counts[s['xep_loai']] += 1

    print("\n--- Thống kê xếp loại ---")
    for k, v in counts.items():
        print(f"{k}: {v} sinh viên")
    return counts


def plot_chart(counts):
    """Vẽ biểu đồ"""
    if not counts or sum(counts.values()) == 0:
        print("Không có dữ liệu để vẽ!")
        return

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    labels = list(counts.keys())
    values = list(counts.values())
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

    # Pie chart
    ax1.pie(values, labels=labels, autopct='%1.1f%%',
            colors=colors, startangle=90)
    ax1.set_title("Pie Chart - Xếp loại học lực")

    # Bar chart
    ax2.bar(labels, values, color=colors)
    ax2.set_title("Bar Chart - Xếp loại học lực")
    ax2.set_ylabel("Số lượng")

    plt.tight_layout()
    plt.show()


def menu():
    """Menu chính"""
    students = load_data()

    while True:
        print("\n" + "="*40)
        print("QUẢN LÝ SINH VIÊN")
        print("="*40)
        print("1. Hiển thị danh sách")
        print("2. Thêm sinh viên")
        print("3. Cập nhật sinh viên")
        print("4. Xoá sinh viên")
        print("5. Tìm kiếm sinh viên")
        print("6. Sắp xếp danh sách")
        print("7. Thống kê điểm")
        print("8. Vẽ biểu đồ")
        print("9. Lưu CSV")
        print("10. Thoát")
        print("="*40)

        choice = input("Chọn chức năng (1-10): ").strip()

        if choice == '1':
            display_students(students)
        elif choice == '2':
            add_student(students)
        elif choice == '3':
            update_student(students)
        elif choice == '4':
            delete_student(students)
        elif choice == '5':
            search_student(students)
        elif choice == '6':
            sort_students(students)
        elif choice == '7':
            counts = stats(students)
        elif choice == '8':
            counts = stats(students)
            plot_chart(counts)
        elif choice == '9':
            save_csv(students)
        elif choice == '10':
            save_data(students)
            print("✓ Thoát chương trình. Tạm biệt!")
            break
        else:
            print("⚠ Lựa chọn không hợp lệ!")


menu()