
testGrid = [
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [2, 2, 2, 2]
]


def greatest_product(grid):
    rows = len(grid)
    cols = len(grid[0])
    max_product = 0
    
    # Check horizontally
    for i in range(rows):
        for j in range(cols-3):
            product = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]
            max_product = max(max_product, product)

    # Check vertically
    for i in range(rows-3):
        for j in range(cols):
            product = grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]
            max_product = max(max_product, product)

    # Check diagonally (top-left to bottom-right)
    for i in range(rows-3):
        for j in range(cols-3):
            product = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
            max_product = max(max_product, product)

    # Check diagonally (top-right to bottom-left)
    for i in range(3, rows):
        for j in range(cols-3):
            product = grid[i][j] * grid[i-1][j+1] * grid[i-2][j+2] * grid[i-3][j+3]
            max_product = max(max_product, product)

    return max_product

print(greatest_product(testGrid))
