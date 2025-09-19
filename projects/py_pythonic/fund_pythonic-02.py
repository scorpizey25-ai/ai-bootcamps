orders = [
    # order_id, customer, date (YYYY-MM-DD), items: list of (product_id, product_name, qty, price_per_unit)
    (1001, "Andi", "2025-07-02", [(1, "Pensil", 10, 1500), (2, "Pulpen", 2, 5000)]),
    (1002, "Budi", "2025-07-15", [(2, "Pulpen", 5, 5000), (3, "Buku", 1, 25000)]),
    (1003, "Citra", "2025-08-01", [(1, "Pensil", 3, 1500)]),
    (1004, "Andi", "2025-08-18", [(3, "Buku", 2, 25000), (4, "Penggaris", 1, 8000)]),
    (1005, "Dina", "2025-09-03", [(2, "Pulpen", 10, 4500)]),
    (1006, "Eko", "2025-09-10", [(5, "Marker", 4, 12000), (2, "Pulpen", 1, 4500)]),
    (1007, "Budi", "2025-09-12", [(3, "Buku", 3, 24000)]),
    (1008, "Fajar", "2025-09-18", [(1, "Pensil", 20, 1400)]),
]

# ================================== Unpacking Tuple ==================================
# Proses menetapkan elemen-elemen dari sebuah tuple ke dalam variabel-variabel terpisah
# =====================================================================================

# Ambil Semua subtotal (qty * price)
subtotal_list = [qty * price for *_, items in orders for (_, _, qty, price) in items]
# print(f"List Subtotal : {subtotal_list}")

# Total revenue (pendapatan total)
total_revenue = sum(subtotal_list)
# print(f"Total Revenue : {total_revenue}")

# ================================= Dictionary Mapping =================================
# proses di mana Anda membuat sebuah kamus (dictionary) baru berdasarkan sebuah iterable 
# (seperti list atau tuple) yang sudah ada.
# ======================================================================================

# Total unit terjual per produk, misalkan (pensil) => 10 + 3 + 20 => 33
from collections import defaultdict

sold = defaultdict(int)
for *_, items_ in orders:
    for _, produk_name, qty, _ in items_:
        sold[produk_name] += qty 

# print(f"Product Name {sold.items()}") 

# gunakan items() untuk menampilkan pasangan key & values
# jika tanpa itu, maka hanya menampilkan default key
# key=lambda x:x[1] => mengurutkan element ke-1 yaitu qty
sold_product_unit = sorted(sold.items(), key=lambda x:x[1], reverse=True);   
print(f"List Unit Terjual Tertinggi : {sold_product_unit}") 