from random import shuffle

from sklearn.ensemble import RandomForestClassifier

from dao.clients_dao import get_clients_list
from data.data_preprocessor import DataPreprocessor
from data.data_utils import DataUtils

data = get_clients_list(verbose=True)

STATUS = 'status'
GOOD = 'GOOD'
BAD = 'BAD'

good_clients = [c for c in data if c[STATUS] == GOOD]
bad_clients = [c for c in data if c[STATUS] == BAD]

bad_total = len(bad_clients)
good_equal = good_clients[:bad_total]

balanced_data = bad_clients + good_equal

print("Building evaluation model from %d clients...\n" % len(balanced_data))

string_fields = ['mobile_operator', 'email_domain', 'application_type', 'actual_city', 'bank', 'work_status']
FREQUENCY_THRESHOLD = 0.05
fields_thresholds = DataUtils.map_list_to_single_value(string_fields, FREQUENCY_THRESHOLD)

pre_processed_data = DataPreprocessor.pre_process_data(balanced_data, fields_thresholds)
shuffle(pre_processed_data)

feature_names = DataUtils.extract_keys(pre_processed_data)
only_values = DataUtils.extract_values(pre_processed_data)

k = 20
n = len(pre_processed_data)

known = only_values[:n - k]
test_records = only_values[-k:]

problem = [x[1:] for x in test_records]
answer = [x[0] for x in test_records]

target = [x[0] for x in known]
train = [x[1:] for x in known]

rfClassifier = RandomForestClassifier(n_estimators=50)
rfClassifier.fit(train, target)

class_probabilities = rfClassifier.predict_proba(problem)
good_probabilities = [x[1] for x in class_probabilities]

for i in range(k):
    print("Client:", dict(zip(feature_names, test_records[i])))
    print(GOOD if answer[i] == 1 else BAD)
    print("%.2f\n" % good_probabilities[i])
