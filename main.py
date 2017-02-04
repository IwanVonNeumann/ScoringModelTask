from random import shuffle

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor

from dao.clients_dao import get_clients_list
from data.data_preprocessor import DataPreprocessor
from data.data_utils import DataUtils

data = get_clients_list(verbose=True)

string_fields = ['mobile_operator', 'email_domain', 'application_type', 'actual_city', 'bank', 'work_status']
FREQUENCY_THRESHOLD = 0.05
fields_thresholds = DataUtils.map_list_to_single_value(string_fields, FREQUENCY_THRESHOLD)

pre_processed_data = DataPreprocessor.pre_process_data(data, fields_thresholds)
shuffle(pre_processed_data)

feature_names = DataUtils.extract_keys(pre_processed_data)
only_values = DataUtils.extract_values(pre_processed_data)

known = only_values[:10000]
test_records = only_values[25000:25100]

problem = [x[1:] for x in test_records]
answer = [x[0] for x in test_records]

target = [x[0] for x in known]
train = [x[1:] for x in known]

rfClassifier = RandomForestClassifier(n_estimators=100)
rfClassifier.fit(train, target)

prediction = rfClassifier.predict(problem)

print(prediction)

# ModelStats.compare_binary_vectors(prediction, answer, verbose=True)
