N = 8

board = [-1] * N
solution_count = 0


def is_safe(row, col):
    for prev_row in range(row):
        prev_col = board[prev_row]

        # Check same column
        if prev_col == col:
            return False

        # Check diagonal
        if abs(prev_col - col) == abs(prev_row - row):
            return False

    return True


def solve(row):
    global solution_count

    # All queens have been placed
    if row == N:
        solution_count += 1

        print(f"\nSolution {solution_count}:")
        for r in range(N):
            for c in range(N):
                if board[r] == c:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print()

        return

    for col in range(N):
        if is_safe(row, col):
            board[row] = col

            solve(row + 1)

            # Backtrack
            board[row] = -1


solve(0)

print("\nTotal solutions:", solution_count)
