from sklearn.ensemble import RandomForestClassifier

from data.data_utils import DataUtils


class ModelValidator(object):

    @staticmethod
    def compare_binary_vectors(a, b):
        mistakes = 0
        for i in range(0, len(a)):
            if a[i] != b[i]:
                mistakes += 1
        return 1 - mistakes / len(a)

    @staticmethod
    def cross_validate(data, k, verbose=False):
        data_chunks = DataUtils.list_to_chunks(data, k)
        acc_precision = 0

        for i in range(0, k):
            test = data_chunks[i]
            known_chunks = DataUtils.list_without_element(data_chunks, i)
            known = DataUtils.merge_list_of_lists(known_chunks)

            problem = [x[1:] for x in test]
            answer = [x[0] for x in test]

            target = [x[0] for x in known]
            train = [x[1:] for x in known]

            rf_classifier = RandomForestClassifier(n_estimators=100)
            rf_classifier.fit(train, target)
            prediction = rf_classifier.predict(problem)

            precision = ModelValidator.compare_binary_vectors(prediction, answer)
            acc_precision += precision

            if verbose:
                print(i, round(precision, 3))

        return acc_precision / k


    @staticmethod
    def calc_feature_importances(data, feature_names):
        target = [x[0] for x in data]
        train = [x[1:] for x in data]

        rf_classifier = RandomForestClassifier(n_estimators=100)
        rf_classifier.fit(train, target)
        feature_importances = [float(x) for x in rf_classifier.feature_importances_]
        return DataUtils.sort_dict(dict(zip(feature_names[1:], feature_importances)))
