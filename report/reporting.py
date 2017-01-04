from random import shuffle

from data.data_preprocessor import DataPreprocessor
from data.data_utils import DataUtils
from data.excel_parser import ExcelParser
from model.model_validator import ModelValidator

FILE_NAME = "Task_scoring_modeller_Nov2016.xlsx"
WORKSHEET_NUMBER = 3
excel_parser = ExcelParser(FILE_NAME, WORKSHEET_NUMBER)

data = excel_parser.extract_mapped_rows(verbose=True)

string_fields = ['mobile_operator', 'email_domain', 'application_type', 'actual_city', 'bank', 'work_status']
FREQUENCY_THRESHOLD = 0.05
fields_thresholds = DataUtils.map_list_to_single_value(string_fields, FREQUENCY_THRESHOLD)

pre_processed_data = DataPreprocessor.pre_process_data(data, fields_thresholds, verbose=True)
shuffle(pre_processed_data)

feature_names = DataUtils.extract_keys(pre_processed_data)
only_values = DataUtils.extract_values(pre_processed_data)

feature_importances = ModelValidator.calc_feature_importances(only_values, feature_names)
print(DataUtils.format_float_dict(feature_importances, 3))

excel_parser.close()
