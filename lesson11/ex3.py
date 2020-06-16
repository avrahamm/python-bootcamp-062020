rows = ''
while True:
    row = input("Insert row, to quit insert empty row: ")
    if len(row) == 0:
        break
    rows = row + '\n' + rows


print(rows)



