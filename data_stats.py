from dao.clients_dao import get_clients_list

data = get_clients_list(verbose=True)
STATUS = 'status'

good_clients = [c for c in data if c[STATUS] == "GOOD"]
indetermined_clients = [c for c in data if c[STATUS] == "INDETERMINED"]
bad_clients = [c for c in data if c[STATUS] == "BAD"]

good_total = len(good_clients)
bad_total = len(bad_clients)

print("Good clients:", good_total)
print("Indetermined clients:", len(indetermined_clients))
print("Bad clients:", bad_total)

print("Good rate:", good_total / (good_total + bad_total))
