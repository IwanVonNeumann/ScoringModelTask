class FieldsRemover(object):
    @staticmethod
    def remove_ids(data):
        for item in data:
            del item['client_id']

    @staticmethod
    def remove_irrelevant_fields(data):
        FieldsRemover.remove_ids(data)
