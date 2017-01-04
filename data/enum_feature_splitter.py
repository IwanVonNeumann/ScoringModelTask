from sklearn.feature_extraction import DictVectorizer

from data.data_utils import DataUtils


class EnumFeatureSplitter(object):
    @staticmethod
    def split_features(data, key_feature='status', verbose=False):
        dict_vectorizer = DictVectorizer()

        transformed_data = list(dict_vectorizer.fit_transform(data).toarray())
        feature_names = dict_vectorizer.get_feature_names()

        if verbose:
            print("Features before:", len(data[0]))
            print("Features after:", len(feature_names))
            print(feature_names)

        index_of_key = feature_names.index(key_feature)

        feature_names = DataUtils.set_element_first(feature_names, index_of_key)
        transformed_data = [DataUtils.set_element_first(item, index_of_key) for item in transformed_data]

        return DataUtils.map_headers_to_data(feature_names, transformed_data)
