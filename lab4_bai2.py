# Sinh tat ca tap con dac trung bang thuat toan Quay lui
def generate_subsets_backtracking(features):
    all_subsets = []

    def backtrack(start_index, current_path):
        # Luu tap con hien tai
        all_subsets.append(list(current_path))

        # Duyet qua cac dac trung tiep theo
        for i in range(start_index, len(features)):
            # 1. Chon dac trung
            current_path.append(features[i])
            # 2. De quy
            backtrack(i + 1, current_path)
            # 3. Quay lui (Undo)
            current_path.pop()

    backtrack(0, [])
    return all_subsets


if __name__ == "__main__":
    features = ['Age', 'Income', 'Score']
    subsets = generate_subsets_backtracking(features)
    print(f"Tong so tap con sinh duoc (2^3 = 8): {len(subsets)}")
    for s in subsets:
        print(s)
