from math import isnan

from numpy import sort


class RecordsFilter(object):
    @staticmethod
    def remove_clients_with_indetermined_status(clients, verbose=False):
        determined_clients = [client for client in clients if client['status'] != 'INDETERMINED']
        if verbose:
            print("Records filtered out due to status='INDETERMINED':", len(clients) - len(determined_clients))
        return determined_clients

    @staticmethod
    def filter(data, verbose=False):
        return RecordsFilter.remove_clients_with_indetermined_status(data, verbose=verbose)

    @staticmethod
    def contains_nan(item, verbose=False, missing_fields=None):
        for key in item.keys():
            value = item[key]
            if isnan(value):
                if verbose:
                    missing_fields.add(key)
                return True
        return False

    @staticmethod
    def remove_records_with_nan_values(data, verbose=False):
        missing_fields = set()
        without_nan = [item for item in data if
                       not RecordsFilter.contains_nan(item, verbose=verbose, missing_fields=missing_fields)]
        if verbose:
            print("Records filtered out due to nan values:", len(data) - len(without_nan))
            print("Records without values:", sort(list(missing_fields)))
        return without_nan
