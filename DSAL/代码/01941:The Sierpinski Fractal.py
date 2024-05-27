def draw(n, x=0, y=0, grid=None):
    if grid is None:
        size = 2 ** n
        grid = [[' ' for _ in range(size * 2)] for _ in range(size)]
    if n == 1:
        grid[y][x+1] = '/'
        grid[y][x+2] = '\\'
        grid[y+1][x+0] = '/'
        grid[y+1][x+1] = '_'
        grid[y+1][x+2] = '_'
        grid[y+1][x+3] = '\\'
    else:
        half = 2 ** (n - 1)
        draw(n - 1, x, y + half, grid)
        draw(n - 1, x + half * 2, y + half, grid)
        draw(n - 1, x + half, y, grid)
    return grid

def print_grid(grid):
    for row in grid:
        print(''.join(row).rstrip())

while True:
    n = int(input())
    if n == 0:
        break
    grid = draw(n)
    print_grid(grid)
    print()