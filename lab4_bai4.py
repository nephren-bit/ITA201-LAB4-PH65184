# Giai bai toan N quan hau bang Quay lui + cat tia nhanh can voi 3 tap hop
def solve_n_queens(n, show_boards=True):
    solutions = []
    queens = [-1] * n  # queens[r] = cot dat quan hau o hang r
    cols, diag1, diag2 = set(), set(), set()

    def backtrack(row):
        if row == n:
            board = ["." * c + "Q" + "." * (n - c - 1) for c in queens]
            solutions.append(board)
            return
        for c in range(n):
            # Cat tia: kiem tra an toan O(1)
            if c in cols or (row - c) in diag1 or (row + c) in diag2:
                continue
            # Chon
            queens[row] = c
            cols.add(c)
            diag1.add(row - c)
            diag2.add(row + c)
            backtrack(row + 1)
            # Quay lui
            cols.remove(c)
            diag1.remove(row - c)
            diag2.remove(row + c)

    backtrack(0)

    if show_boards:
        for idx, board in enumerate(solutions, 1):
            print(f"Cach xep {idx}:")
            for line in board:
                print("  " + line)
    return len(solutions)


if __name__ == "__main__":
    print(f"Voi n = 4: Tong so cach xep la {solve_n_queens(4)}")
    print()
    print(f"Voi n = 8: Tong so cach xep la {solve_n_queens(8, show_boards=False)}")
