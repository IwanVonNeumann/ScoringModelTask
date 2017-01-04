# for c in clients:
#     c.print()

# good_clients = [c for c in clients if c.status == "GOOD"]
# indetermined_clients = [c for c in clients if c.status == "INDETERMINED"]
# bad_clients = [c for c in clients if c.status == "BAD"]

# print("Good clients:", len(good_clients))
# print("Indetermined clients:", len(indetermined_clients))
# print("Bad clients:", len(bad_clients))
import numpy


def list_to_chunks(l, k):
    arrays = numpy.array_split(numpy.array(l), k)
    return [list(a) for a in arrays]


a = [i for i in range(1, 26)]

print(a)
print(list_to_chunks(a, 4))
