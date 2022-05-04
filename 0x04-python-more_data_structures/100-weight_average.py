#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    score_list = [item[0] * item[1] for item in my_list]
    weightings_list = [item[1] for item in my_list]
    weighted_score = sum(score_list) / sum(weightings_list)
    return weighted_score
