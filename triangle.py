from typing import List


def get_triangle(rows: int) -> List[List[int]]:
    triangle = []
    for row in range(rows):
        if row == 0:
            triangle.append([1])
        else:
            prev_row = triangle[-1]  # попередній рядок
            new_row = [1]
            for i in range(1, len(prev_row)):
                new_row.append(prev_row[i - 1] + prev_row[i])
            new_row.append(1)
            triangle.append(new_row)
    return triangle


triangle = get_triangle(5)
for row in triangle:
    print(" ".join(map(str, row)))
