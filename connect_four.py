# make the grid
rows, cols = 6, 7
array = []

for _ in range(rows):
    row = []
    for _ in range(cols):
        row.append(0)
    array.append(row)