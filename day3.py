
def mark_taken(grid, hstart, hend, vstart, vend, id):
    for a_row_idx in range(vstart, vstart+vend):
        for a_column_idx in range(hstart, hstart+hend):
            if grid[a_row_idx][a_column_idx] == 0:
                grid[a_row_idx][a_column_idx] = id
            else:
                grid[a_row_idx][a_column_idx] = 'x'


def part_1(input='day3.txt'):
    with open(input, 'r') as f:
        lines = f.readlines()
        grid = [[0]* 1000 for i in range(1000)]
        for a_line in lines:
            a_line = a_line.replace('#', '').replace(' ', '')
            id = int(a_line.split('@')[0])
            lr = a_line.split(',')
            left = int(lr[0].split('@')[1])
            top = int(lr[1].split(':')[0])
            wh = a_line.split(':')[1]
            width = int(wh.split('x')[0])
            height = int(wh.split('x')[1])
            mark_taken(grid, left, width, top, height, id)
        return sum(1 for a_row in grid for a_column in a_row if a_column == 'x')

# print(part_1())


def mark_taken2(grid, hstart, width, vstart, height, id):
    borked = set()
    for a_row_idx in range(vstart, vstart + height):
        for a_column_idx in range(hstart, hstart + width):
            if grid[a_row_idx][a_column_idx] != 0:
                borked.add(grid[a_row_idx][a_column_idx])
                borked.add(id)
            grid[a_row_idx][a_column_idx] = id
    return borked

# test_grid = [[1, 1, 1, 1],
#              [5, 2, 3, 3],
#              [6, 4, 8, 2],
#              [7, 8, 9, 3]]
#
# print(mark_taken2(test_grid, 1, 2, 1, 1, 16), test_grid)

def part_2(input='day3.txt'):
    with open(input, 'r') as f:
        lines = f.readlines()
        grid = [[0]* 1000 for i in range(1000)]
        rekt_claims = set()
        claims = set()
        count = 0
        for a_line in lines:
            a_line = a_line.replace('#', '').replace(' ', '')
            id = int(a_line.split('@')[0])
            claims.add(id)
            lr = a_line.split(',')
            left = int(lr[0].split('@')[1])
            top = int(lr[1].split(':')[0])
            wh = a_line.split(':')[1]
            width = int(wh.split('x')[0])
            height = int(wh.split('x')[1])
            claimed = mark_taken2(grid, left, width, top, height, id)
            # print(claimed)
            # count +=1
            # if count == 100:
            #     exit(1)
            for a_claim_num in claimed:
                rekt_claims.add(a_claim_num)
        return claims.difference(rekt_claims)

print(part_2())

