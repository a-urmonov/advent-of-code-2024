with open("input.txt", "r") as file:
    data = file.readlines()

letters= []
for line in data:
    values = line.replace('\n','')
    letters.append(values)

grid = []
for item in letters:
    grid.append(list(item))

def count_words_in_grid(grid, word):
    word_lenght = len(word)
    rows = len(grid)
    cols = len(grid[0])
    total_count = 0

    DIRECTIONS = [
        (0, 1), 
        (0, -1), 
        (1, 0), 
        (-1, 0), 
        (1, 1),  
        (1, -1), 
        (-1, 1), 
        (-1, -1)
    ]

    def is_word_found(start_row, start_col, direction, word):
        for i in range(0,word_lenght):
            new_row = start_row + i*direction[0]
            new_col = start_col + i*direction[1]
            if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
                return False
            if grid[new_row][new_col] != word[i]:
                return False
        
        return True
    
    for row in range(0, rows):
        for col in range(0, cols):
            for direction in DIRECTIONS:
                if is_word_found(row, col, direction, word):
                    total_count += 1
    
    return total_count


# print(count_words_in_grid(grid=grid, word = 'XMAS'))
def count_X_pattern(grid, word):
    word_lenght = len(word)
    rows = len(grid)
    cols = len(grid[0])
    total_count = 0
    permutations = ['MAS', 'SAM']

    for row in range(1,rows-1):
        for col in range(1,cols-1):
            center = grid[row][col]
            if (
                center == word[1] and
                grid[row - 1][col - 1] == word[0] and
                grid[row + 1][col + 1] == word[2] and
                grid[row - 1][col + 1] == word[2] and
                grid[row + 1][col - 1] == word[0]
            ):
                total_count += 1

            if (
                center == word[1] and
                grid[row - 1][col - 1] == word[2] and # top left 
                grid[row + 1][col + 1] == word[0] and # bottom right
                grid[row - 1][col + 1] == word[2] and # top right
                grid[row + 1][col - 1] == word[0] # bottom left
            ):
                total_count += 1
            
            if (
                center == word[1] and
                grid[row - 1][col - 1] == word[2] and # top left 
                grid[row + 1][col + 1] == word[0] and # bottom right
                grid[row - 1][col + 1] == word[0] and # top right
                grid[row + 1][col - 1] == word[2] # bottom left
            ):
                total_count += 1
            if (
                center == word[1] and
                grid[row - 1][col - 1] == word[0] and # top left 
                grid[row + 1][col + 1] == word[2] and # bottom right
                grid[row - 1][col + 1] == word[0] and # top right
                grid[row + 1][col - 1] == word[2] # bottom left
            ):
                total_count += 1
    return total_count

print(count_X_pattern(grid, word="MAS"))