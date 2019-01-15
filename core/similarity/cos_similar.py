# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 下午8:53
# @Author  : yidxue


def CosSimilarity(vector1, vector2):
    dot_product = 0.0
    normA = 0.0
    normB = 0.0
    for a, b in zip(vector1, vector2):
        dot_product += a * b
        normA += a ** 2
        normB += b ** 2
    if normA == 0.0 or normB == 0.0:
        return None
    else:
        return dot_product / ((normA * normB) ** 0.5)


if __name__ == '__main__':
    vec1 = [5.0, 3.0, 2.5]
    vec2 = [2.0, 2.5, 5.0]

    print(CosSimilarity(vec1, vec2))
