from typing import List, Tuple


def find_min_max(nums: List[int]) -> Tuple[int]:
    n = len(nums)
    if n % 2:
        cur_min, cur_max, i = nums[0], nums[0], 1
    else:
        cur_min, cur_max, i = nums[0], nums[1], 2

    while i < n:
        x, y = nums[i], nums[i + 1]
        if x < y:
            cur_min = min(cur_min, x)
            cur_max = max(cur_max, y)
        else:
            cur_min = min(cur_min, y)
            cur_max = max(cur_max, x)
        i += 2
    
    return (cur_min, cur_max)


if __name__ == "__main__":
    nums = [1, 4, 2, 5, 6, 3, 10, 8]
    min_, max_ = find_min_max(nums)
    print(min_, max_)    
    
