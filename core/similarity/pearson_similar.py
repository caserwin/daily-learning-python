# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 下午8:57
# @Author  : yidxue


def PearsonSimilarity(vec1, vec2):
    value = range(len(vec1))

    sum_vec1 = sum([vec1[i] for i in value])
    sum_vec2 = sum([vec2[i] for i in value])

    square_sum_vec1 = sum([pow(vec1[i], 2) for i in value])
    square_sum_vec2 = sum([pow(vec2[i], 2) for i in value])

    product = sum([vec1[i] * vec2[i] for i in value])

    numerator = product - (sum_vec1 * sum_vec2 / len(vec1))
    dominator = ((square_sum_vec1 - pow(sum_vec1, 2) / len(vec1)) * (
            square_sum_vec2 - pow(sum_vec2, 2) / len(vec2))) ** 0.5

    if dominator == 0:
        return 0
    result = numerator / (dominator * 1.0)

    return result


if __name__ == '__main__':
    vec1 = [5.0, 3.0, 2.5]
    vec2 = [2.0, 2.5, 5.0]

    print(PearsonSimilarity(vec1, vec2))
