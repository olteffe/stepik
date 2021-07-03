import re
from collections import Counter


def sum_word_in_string(iter_string: str, result_dict: dict) -> dict:
    string_to_list = re.sub(r"[^a-zA-Z]+", " ", iter_string).lower().split()
    temp_dict = dict(Counter(string_to_list))
    for key, value in temp_dict.items():
        if key in result_dict:
            result_dict[key] += temp_dict[key]
        else:
            result_dict[key] = value
    return result_dict


def check_max_value(some_dict: dict) -> dict:
    sorted_value = {k: v for k, v in sorted(some_dict.items(), key=lambda item: item[1], reverse=True)}
    count = 0
    temp_dict = {}
    for key, value in sorted_value.items():
        if sorted_value[key] >= count:
            temp_dict[key] = value
            count = sorted_value[key]
        else:
            break
    return temp_dict


def main():
    out_dict = {}
    with open('dataset_3363_3.txt') as file:
        for line in file:
            sum_word_in_string(line, out_dict)
    result_dict = check_max_value(out_dict)
    print(sorted(result_dict.items())[0])


if __name__ == '__main__':
    main()
