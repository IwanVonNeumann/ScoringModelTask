from random import shuffle

from dao.clients_dao import get_clients_list
from data.data_preprocessor import DataPreprocessor
from data.data_utils import DataUtils
from stats.model_stats import ModelStats

data = get_clients_list(verbose=True)

string_fields = ['mobile_operator', 'email_domain', 'application_type', 'actual_city', 'bank', 'work_status']
FREQUENCY_THRESHOLD = 0.05
fields_thresholds = DataUtils.map_list_to_single_value(string_fields, FREQUENCY_THRESHOLD)

pre_processed_data = DataPreprocessor.pre_process_data(data, fields_thresholds, verbose=True)
shuffle(pre_processed_data)

feature_names = DataUtils.extract_keys(pre_processed_data)
only_values = DataUtils.extract_values(pre_processed_data)

feature_importances = ModelStats.calc_feature_importances(only_values, feature_names)
print(DataUtils.format_float_dict(feature_importances, 3))

# precision = ModelStats.cross_validate(only_values, 10, verbose=True)
precision = ModelStats.cross_validate_fast(only_values, 10, verbose=True)
print(precision)

oob_precision = ModelStats.oob_validate(only_values)
print(oob_precision)
