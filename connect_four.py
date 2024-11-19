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

while array [0][col_num] ! = 0:
    col_num = input("Please select a new column.")
    col_num = int(col_num)

# 4. Update the grid

if user1:
    array[row_num][col_num] = X
        else = y

# 5. Figure out who won