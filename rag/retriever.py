import math


def cosine(a, b):
    return sum(x*y for x, y in zip(a, b)) / (
        math.sqrt(sum(x*x for x in a)) * math.sqrt(sum(y*y for y in b))
    )


def retrieve(query_vec, index, k: int):
    scored = [
        (cosine(query_vec, v), m)
        for v, m in zip(index.vectors, index.meta)
    ]
    scored.sort(reverse=True, key=lambda x: x[0])
    return [m for _, m in scored[:k]]
