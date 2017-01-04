from data.enum_feature_splitter import EnumFeatureSplitter
from data.fields_remover import FieldsRemover
from data.fields_transformer import FieldsTransformer
from data.records_filter import RecordsFilter


class DataPreprocessor(object):
    @staticmethod
    def pre_process_data(data, fields_thresholds, verbose=False):
        filtered_data = RecordsFilter.filter(data, verbose=verbose)
        FieldsRemover.remove_irrelevant_fields(filtered_data)
        FieldsTransformer.process_fields(filtered_data, fields_thresholds, verbose=verbose)
        split_data = EnumFeatureSplitter.split_features(filtered_data, verbose=verbose)
        without_nan = RecordsFilter.remove_records_with_nan_values(split_data, verbose=verbose)
        return without_nan
