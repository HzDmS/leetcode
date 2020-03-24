from typing import List
from random import randint

def randomized_select(nums: List[int], left: int, right: int, k: int):
    
    n = len(nums)
    if left == right:
        return nums[left]
    pivot = randomized_partition(nums, left, right)

    if pivot == k:
        return nums[pivot]
    elif pivot > k:
        return randomized_select(nums, left, pivot - 1, k)
    else:
        return randomized_select(nums, pivot + 1, right, k)


def randomized_partition(nums: List[int], left: int, right: int) -> int:
    i = randint(left, right)
    x = nums[i]
    swap(nums, i, right)
    i = left - 1
    for j in range(left, right):
        if nums[j] <= x:
            i += 1
            swap(nums, i, j)
    swap(nums, i + 1, right)
    return i + 1


def swap(nums: List[int], i: int, j: int) -> None:
    nums[i], nums[j] = nums[j], nums[i]


if __name__ == "__main__":
    arr = [1, 3, 2, 5, 4, -1]
    print(randomized_select(arr, 0, len(arr) - 1, 2))

