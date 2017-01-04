from collections import Counter
from itertools import repeat
from math import isnan

import numpy


class DataUtils(object):
    @staticmethod
    def count_absolute_frequencies(values):
        return dict(Counter(values))

    @staticmethod
    def count_relative_frequencies(values):
        abs_f = DataUtils.count_absolute_frequencies(values)
        f_sum = sum(abs_f.values())
        return {key: value / f_sum for key, value in abs_f.items()}

    @staticmethod
    def count_relative_frequencies_and_merge_rare(values, threshold, default_key='OTHER'):
        rel_f = DataUtils.count_relative_frequencies(values)
        major_elements = {key: value for key, value in rel_f.items() if value >= threshold}
        minor_f_sum = sum(value for value in rel_f.values() if value < threshold)
        major_elements[default_key] = minor_f_sum
        return major_elements

    @staticmethod
    def map_list_to_single_value(fields, frequency_threshold):
        return dict(zip(fields, repeat(frequency_threshold)))

    @staticmethod
    def map_headers_to_data(headers, data):
        return [dict(zip(headers, item)) for item in data]

    @staticmethod
    def set_element_first(array, i):
        as_list = list(array)
        element = as_list.pop(i)
        head = [element]
        head.extend(as_list)
        return head

    @staticmethod
    def extract_keys(data):
        return list(data[0].keys())

    @staticmethod
    def extract_values(data):
        return [list(item.values()) for item in data]

    @staticmethod
    def sort_dict(d):
        sorted_keys = sorted(d, key=d.get, reverse=True)
        sorted_dict = {}
        for key in sorted_keys:
            sorted_dict[key] = d[key]
        return sorted_dict

    @staticmethod
    def format_float_dict(d, precision):
        return {k: round(v, precision) if isinstance(v, float) else v for k, v in d.items()}

    @staticmethod
    def list_to_chunks(l, k):
        arrays = numpy.array_split(numpy.array(l), k)
        return [list(a) for a in arrays]

    @staticmethod
    def list_without_element(l, i):
        return [l[j] for j in range(0, len(l)) if j != i]

    @staticmethod
    def merge_list_of_lists(l):
        return [item for sub_list in l for item in sub_list]
