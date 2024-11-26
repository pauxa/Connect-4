def won_horiz(array, row_num, col_num, rows, cols):
    counter = 0 
    track_col = 0

    while track_col < cols and counter != 4:

# 1. Make the grid
rows, cols = 6, 7
array = []

for _ in range(rows):
    row = []
    for _ in range(cols):
        row.append(0)
    array.append(row)

# 2. Get input from the user
col_num = input("Choose a column.")
col_num = int(col_num)

# 3. Check if the column is full
row_num = rows - 1
user1 = True

while array [0][col_num] != 0:
    col_num = input("Please select a new column.")
    col_num = int(col_num)

# 4. Find an available row

while array [row_num][col_num] != 0:
    row_num = row_num - 1

# 5. Update the grid

if user1:
    array[row_num][col_num] = 'X'
else:
    array[row_num][col_num] = 'Y'

# 5. Figure out who won

if won_vert(array, row_num, col_num, rows, cols)
    or won_diag(array, row_num, col_num, rows, cols)
    or won_horiz(array, row_num, col_num, rows, cols):
    print("Congrats! You're the winner.")

