#!/usr/bin/python3
def best_score(a_dictionary):
    max_score = 0
    if not a_dictionary:
        return (None)
    else:
        dic_keys = list(a_dictionary.keys())
        for i in dic_keys:
            score = a_dictionary.get(i)
            if score > max_score:
                max_score = score
    return (max_score)
