'''TO DO: You were given a map (2 dimensional grid) where each cell is either forest (marked as X) or 
grassland (marked as O). Write a script that gets number of isolated forests on the map. Forest is formed of 
cells X that are connected in one of 8 directions. 

Example:
There are two forests in the map bellow:
0X0X0
00XX0
00000
0XX00
'''


def count_isolated_forests(grid):
    def is_valid(x, y):
        # If the cell is within boundaries of the map
        return 0 <= x < rows and 0 <= y < cols

    def DFS(x, y):
        if not is_valid(x, y):
            return

        if grid[x][y] == 'X':
            # Current cell is marked visited
            visited[x][y] = True

            # All neighbors in 8 directions
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    next_x = x + dx
                    next_y = y + dy
                    if is_valid(next_x, next_y) and grid[next_x][next_y] == 'X' and not visited[next_x][next_y]:
                        DFS(next_x, next_y)

    rows, cols = len(grid), len(grid[0])

    # Keep track of visited cells
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    isolated_forests = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'X' and not visited[i][j]:
                # Conduct DFS from an unvisited X 
                DFS(i, j)
                isolated_forests += 1

    return isolated_forests

gridmap = [
    ['0', 'X', '0', 'X', '0'],
    ['0', '0', 'X', 'X', '0'],
    ['0', '0', '0', '0', '0'],
    ['0', 'X', 'X', '0', '0']
]

gridmap2 = [
    ['X', '0', '0', 'X', '0'],
    ['0', '0', 'X', 'X', '0'],
    ['0', '0', '0', '0', '0'],
    ['0', '0', 'X', 'X', '0'],
    ['0', '0', '0', '0', '0'],
    ['0', '0', 'X', 'X', '0'],
    ['0', '0', '0', '0', '0'],
    ['0', 'X', 'X', '0', '0']
]

def visualize_gridmap(grid, isolated_forests):
    print()
    print("Given map:")
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if grid[i][j] == 'X':
                print('X', end=' ')
            else:
                print('O', end=' ')
        print()
    print()
    print(f"Number of isolated forests: {isolated_forests}")
    print()

isolated_forests = count_isolated_forests(gridmap)

visualize_gridmap(gridmap, isolated_forests)

print("----------------------------")

isolated_forests2 = count_isolated_forests(gridmap2)

visualize_gridmap(gridmap2, isolated_forests2)
