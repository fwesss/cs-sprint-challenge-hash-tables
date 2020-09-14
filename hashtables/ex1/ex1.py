from typing import List, Optional


def get_indices_of_item_weights(
    weights: List[int], _: int, limit: int
) -> Optional[List[int]]:
    pairs = {}
    for index, weight in enumerate(weights):
        if (limit - weight) not in pairs:
            pairs[weight] = index
        else:
            return [index, pairs[limit - weight]]
