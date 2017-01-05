from data.data_utils import DataUtils


class FieldsTransformer(object):
    @staticmethod
    def substitute_values(item, field_name, dictionary):
        value = item[field_name]
        item[field_name] = dictionary[value]
        return item

    @staticmethod
    def set_gender_binary(data):
        gender_dict = {'FEMALE': 0, 'MALE': 1}
        for item in data:
            FieldsTransformer.substitute_values(item, 'gender', gender_dict)

    @staticmethod
    def set_status_binary(data):
        status_dict = {'BAD': 0, 'GOOD': 1}
        for item in data:
            FieldsTransformer.substitute_values(item, 'status', status_dict)

    @staticmethod
    def replace_value(item, field_name, dictionary, default_value='OTHER'):
        if item[field_name] not in dictionary:
            item[field_name] = default_value
        return item

    @staticmethod
    def replace_rare_values(data, field_name, threshold, default_value='OTHER', verbose=False):
        values = [item[field_name] for item in data]
        merged_rel_f = DataUtils.count_relative_frequencies_and_merge_rare(values, threshold)
        if verbose:
            print(field_name, DataUtils.format_float_dict(merged_rel_f, 3))
        for item in data:
            FieldsTransformer.replace_value(item, field_name, merged_rel_f, default_value)

    @staticmethod
    def replace_all_rare_values(data, fields_thresholds, default_value='OTHER', verbose=False):
        for field_name, threshold in fields_thresholds.items():
            FieldsTransformer.replace_rare_values(data, field_name, threshold, default_value, verbose=verbose)

    @staticmethod
    def process_fields(data, fields_thresholds, verbose=False):
        FieldsTransformer.set_status_binary(data)
        FieldsTransformer.set_gender_binary(data)
        FieldsTransformer.replace_all_rare_values(data, fields_thresholds, verbose=verbose)
