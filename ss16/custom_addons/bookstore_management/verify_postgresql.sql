-- SQL Script để kiểm tra bảng bookstore_book trong PostgreSQL
-- Chạy script này trong pgAdmin hoặc psql

-- 1. Kiểm tra bảng có tồn tại không
SELECT EXISTS (
    SELECT FROM information_schema.tables 
    WHERE table_schema = 'public' 
    AND table_name = 'bookstore_book'
) AS table_exists;

-- 2. Xem cấu trúc bảng
SELECT 
    column_name, 
    data_type, 
    character_maximum_length,
    is_nullable,
    column_default
FROM information_schema.columns
WHERE table_name = 'bookstore_book'
ORDER BY ordinal_position;

-- 3. Xem tất cả dữ liệu
SELECT 
    id,
    title,
    author,
    price,
    publish_date,
    isbn,
    stock_quantity,
    active,
    create_date,
    write_date
FROM bookstore_book
ORDER BY create_date DESC;

-- 4. Thống kê dữ liệu
SELECT 
    COUNT(*) as total_books,
    COUNT(CASE WHEN active = true THEN 1 END) as active_books,
    COUNT(CASE WHEN active = false THEN 1 END) as inactive_books,
    SUM(stock_quantity) as total_stock,
    AVG(price) as avg_price,
    MIN(price) as min_price,
    MAX(price) as max_price
FROM bookstore_book;

-- 5. Nhóm theo tác giả
SELECT 
    author,
    COUNT(*) as book_count,
    SUM(stock_quantity) as total_stock,
    AVG(price) as avg_price
FROM bookstore_book
GROUP BY author
ORDER BY book_count DESC;

-- 6. Kiểm tra constraints
SELECT
    tc.constraint_name,
    tc.constraint_type,
    kcu.column_name
FROM information_schema.table_constraints tc
JOIN information_schema.key_column_usage kcu
    ON tc.constraint_name = kcu.constraint_name
WHERE tc.table_name = 'bookstore_book';

-- 7. Kiểm tra indexes
SELECT
    indexname,
    indexdef
FROM pg_indexes
WHERE tablename = 'bookstore_book';
