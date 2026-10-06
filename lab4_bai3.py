# Sinh toan bo n! hoan vi cua {1, 2, ..., n} theo thu tu tu dien (thuat toan sinh)
def generate_permutations(n):
    a = list(range(1, n + 1))  # Cau hinh dau tien: 1 2 ... n
    results = []

    while True:
        results.append(a[:])

        # 1. Tim vi tri i lon nhat sao cho a[i] < a[i+1]
        i = n - 2
        while i >= 0 and a[i] > a[i + 1]:
            i -= 1

        # 2. Khong tim thay -> cau hinh cuoi cung (n ... 2 1)
        if i < 0:
            break

        # 3. Tim vi tri k lon nhat sao cho a[k] > a[i]
        k = n - 1
        while a[k] < a[i]:
            k -= 1

        # 4. Doi cho a[i] va a[k]
        a[i], a[k] = a[k], a[i]

        # 5. Lat nguoc doan a[i+1 .. n-1]
        left, right = i + 1, n - 1
        while left < right:
            a[left], a[right] = a[right], a[left]
            left += 1
            right -= 1

    return results


if __name__ == "__main__":
    perms = generate_permutations(3)
    print(f"Tong so hoan vi (3! = 6): {len(perms)}")
    for p in perms:
        print(p)
    print(f"So hoan vi voi n = 5 (5! = 120): {len(generate_permutations(5))}")
