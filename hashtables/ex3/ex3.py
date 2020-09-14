from typing import List


def intersection(arrays: List[List[int]]) -> List[int]:
    counts = {}

    for array in arrays:
        for num in array:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1

    return list({key for (key, value) in counts.items() if value == len(arrays)})


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
