# -*- coding: utf-8 -*-
"""
Script để kiểm tra dữ liệu Book trong PostgreSQL
Chạy script này từ Odoo shell để xem dữ liệu trong database
"""

# Chạy script này bằng lệnh:
# docker exec -it odoo17_dev_container odoo shell -d odoo --db_host=db --db_user=donut --db_password=donut

# Hoặc tạo file Python và import trong Odoo

def check_book_data():
    """Kiểm tra dữ liệu sách trong database"""
    
    # Lấy tất cả sách
    books = env['bookstore.book'].search([])
    
    print(f"\n{'='*80}")
    print(f"TỔNG SỐ SÁCH TRONG DATABASE: {len(books)}")
    print(f"{'='*80}\n")
    
    if not books:
        print("⚠️  Chưa có sách nào trong database!")
        print("Hãy tạo sách mới trong Odoo UI: Menu 'Cửa hàng sách' → 'Sách'\n")
        return
    
    # Hiển thị thông tin từng sách
    for book in books:
        print(f"📚 ID: {book.id}")
        print(f"   Tên sách: {book.title}")
        print(f"   Tác giả: {book.author}")
        print(f"   Giá: {book.price:,.0f} VNĐ")
        print(f"   Ngày xuất bản: {book.publish_date}")
        print(f"   ISBN: {book.isbn or 'N/A'}")
        print(f"   Tồn kho: {book.stock_quantity}")
        print(f"   Trạng thái: {'Đang bán' if book.active else 'Ngừng bán'}")
        print(f"   Ngày tạo: {book.create_date}")
        print(f"   Người tạo: {book.create_uid.name}")
        print(f"{'-'*80}\n")
    
    # Thống kê
    total_value = sum(book.price * book.stock_quantity for book in books)
    print(f"\n📊 THỐNG KÊ:")
    print(f"   Tổng giá trị kho: {total_value:,.0f} VNĐ")
    print(f"   Sách đang bán: {len(books.filtered(lambda b: b.active))}")
    print(f"   Sách ngừng bán: {len(books.filtered(lambda b: not b.active))}")
    print(f"   Tổng tồn kho: {sum(book.stock_quantity for book in books)}")

# Gọi hàm
if __name__ == '__main__':
    check_book_data()
