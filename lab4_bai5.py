import math


# Grid Search bang Quay lui: sinh moi cau hinh (dict) ma khong can for long nhau cung
def custom_grid_search(param_grid):
    keys = list(param_grid.keys())
    configs = []

    def backtrack(idx, current):
        if idx == len(keys):
            configs.append(dict(current))
            return
        key = keys[idx]
        for value in param_grid[key]:
            current[key] = value       # Chon gia tri cho tham so thu idx
            backtrack(idx + 1, current)
            del current[key]           # Quay lui

    backtrack(0, {})
    return configs


# Nguyen ly Nhan: |Configurations| = |V1| * |V2| * ... * |Vk|
def count_configurations(param_grid):
    total = 1
    for values in param_grid.values():
        total *= len(values)
    return total


# Dirichlet mo rong: N doi tuong vao k hop -> it nhat 1 hop chua >= ceil(N / k) doi tuong
def dirichlet_min_collision(N, k):
    return math.ceil(N / k)


if __name__ == "__main__":
    param_grid = {
        'learning_rate': [0.001, 0.01, 0.1],
        'batch_size': [16, 32, 64],
        'optimizer': ['Adam', 'SGD']
    }

    configs = custom_grid_search(param_grid)
    print(f"So cau hinh sinh boi Quay lui: {len(configs)}")
    for i, cfg in enumerate(configs, 1):
        print(f"  {i:2d}. {cfg}")
    print(f"So thi nghiem theo Nguyen ly Nhan (3 * 3 * 2): {count_configurations(param_grid)}")

    N, k = 105, 10
    print(f"Dirichlet: {N} mo hinh vao {k} cum may chu -> "
          f"it nhat 1 cum chua >= {dirichlet_min_collision(N, k)} cau hinh")

# Y nghia trong can bang tai he thong AI:
# - ceil(105 / 10) = 11: du ham bam phan bo tot den dau, chac chan co it nhat 1 cum may chu
#   phai luu tu 11 ket qua mo hinh tro len. Day la can duoi khong the tranh khoi cua tai lon
#   nhat tren 1 cum.
# - Khi thiet ke he thong, dung luong / bang thong moi cum phai chiu duoc toi thieu 11 ban ghi;
#   neu phan bo hoan hao thi 5 cum chua 11 va 5 cum chua 10 (5*11 + 5*10 = 105).
# - Neu 1 cum chua nhieu hon han 11 thi do la dau hieu ham bam bi lech (hot spot) -> can doi
#   ham bam, them cum may chu (tang k) hoac dung consistent hashing de giam dung do.
