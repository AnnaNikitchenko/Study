from typing import List, Tuple


def find_sum(target: int, li: List[int]) -> Tuple[int, int]:
    for i in range(len(li)):
        for j in range(i + 1, len(li)):
            if li[i] + li[j] == target:
                return (i, j)


print(find_sum(5, [1, 2, 3, 4, 5]))


def find_sum_fast(target: int, li: List[int]) -> Tuple[int, int]:
    seen = {}
    for i, num in enumerate(li):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i


print(find_sum_fast(5, [1, 2, 3, 4, 5]))
