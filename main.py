from random import shuffle

from sklearn.ensemble import RandomForestClassifier

from data.data_preprocessor import DataPreprocessor
from data.data_utils import DataUtils
from data.excel_parser import ExcelParser
from model.model_validator import ModelValidator

FILE_NAME = "Task_scoring_modeller_Nov2016.xlsx"
WORKSHEET_NUMBER = 3
excel_parser = ExcelParser(FILE_NAME, WORKSHEET_NUMBER)

data = excel_parser.extract_mapped_rows(verbose=True)

string_fields = ['mobile_operator', 'gender', 'email_domain', 'application_type', 'actual_city', 'bank', 'work_status']
FREQUENCY_THRESHOLD = 0.05
fields_thresholds = DataUtils.map_list_to_single_value(string_fields, FREQUENCY_THRESHOLD)

pre_processed_data = DataPreprocessor.pre_process_data(data, fields_thresholds)
shuffle(pre_processed_data)

feature_names = DataUtils.extract_keys(pre_processed_data)
only_values = DataUtils.extract_values(pre_processed_data)

# print("Records total:", len(pre_processed_data))

# PrintUtils.print_data(only_values)

# known = only_values[:10000]
# test_records = only_values[25000:25100]

# problem = [x[1:] for x in test_records]
# answer = [x[0] for x in test_records]

# target = [x[0] for x in known]
# train = [x[1:] for x in known]

# rfClassifier = RandomForestClassifier(n_estimators=100)
# rfClassifier = RandomForestClassifier(n_estimators=100)
# rf = RandomForestRegressor()
# rf.fit(train, target)
# rfClassifier.fit(train, target)

# prediction = rfClassifier.predict(problem)

# ModelValidator.compare_binary_vectors(prediction, answer)

precision = ModelValidator.cross_validate(only_values, 10, verbose=True)
print(precision)

# print(prediction)
# print(answer)

excel_parser.close()
