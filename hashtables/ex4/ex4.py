from typing import List


def has_negatives(a: List[int]) -> List[int]:
    pairs = {}

    result = []
    for num in a:
        if (num * -1) in pairs:
            result.append(abs(num))
        else:
            pairs[num] = num * -1

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
