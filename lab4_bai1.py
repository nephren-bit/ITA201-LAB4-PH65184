# Thuat toan sinh toan bo 2^n chuoi nhi phan theo thu tu tu dien (khong de quy)
def generate_binary_strings(n):
    results = []
    a = [0] * n  # Cau hinh dau tien: 000...0

    while True:
        # 1. Luu cau hinh hien tai
        results.append("".join(str(bit) for bit in a))

        # 2. Tim bit 0 dau tien tu phai sang trai
        i = n - 1
        while i >= 0 and a[i] == 1:
            a[i] = 0
            i -= 1

        # 3. Dieu kien dung: khong con bit 0 nao
        if i < 0:
            break

        # 4. Doi bit 0 thanh 1
        a[i] = 1

    return results


if __name__ == "__main__":
    binary_list = generate_binary_strings(3)
    print(f"Tong so chuoi nhi phan sinh duoc (2^3 = 8): {len(binary_list)}")
    print("Danh sach chuoi:", binary_list)
